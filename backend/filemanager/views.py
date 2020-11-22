from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework import status

from filemanager.models import Meme
from filemanager.serializers import MemeSerializer
from filemanager.forms import UploadFileForm
from rest_framework.decorators import api_view
from django.conf import settings
import os
from django.http import HttpResponse, Http404


@api_view(['GET', 'POST', 'DELETE'])
def MemeViewSet(request):
    if request.method == 'GET':
        memes = Meme.objects.all()

        user = request.query_params.get('user', None)
        if user is not None:
            users = memes.filter(user=user)

            meme_serializer = MemeSerializer(users, many=True)
        return JsonResponse(meme_serializer.data, safe=False)

    # POST request handler
    elif request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data.get("file")
            title = form.cleaned_data.get("title")
            instance = Meme(image=file, user=request.user, title=title)
            instance.save()
            return JsonResponse({'message': 'File saved!'}, status=status.HTTP_202_ACCEPTED)
        return JsonResponse({'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

    # DELETE request handler
    elif request.method == 'DELETE':
        meme = Meme.objects.all()

        image_id = request.query_params.get('id', None)

        if image_id is not None:
            entry = meme.filter(id=image_id)
            count = entry.delete()
            return JsonResponse({'message': '{} meme entries were deleted successfully!'.format(count[0])},
                                status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({'message': 'Invalid meme entry!'}, status=status.HTTP_400_BAD_REQUEST)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read())
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from filemanager.models import Meme
from filemanager.serializers import MemeSerializer
from rest_framework.decorators import api_view


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
        meme_data = JSONParser().parse(request)
        if 'id' in meme_data.keys():
            meme_id = meme_data['id']
        else:
            meme_id = None
        # check if id is provided, then run update
        if meme_id is not None:
            meme_f = Meme.objects.all().filter(photo=meme_id)[0]
            meme_serializer = MemeSerializer(meme_f, data=meme_data)
        else:
            meme_serializer = MemeSerializer(data=meme_data)
        if meme_serializer.is_valid():
            meme_serializer.save()
            return JsonResponse(meme_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(meme_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
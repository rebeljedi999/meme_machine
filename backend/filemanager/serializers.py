from rest_framework import serializers
from filemanager.models import Meme

class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meme
        fields = ('id', 'title', 'user', 'image')

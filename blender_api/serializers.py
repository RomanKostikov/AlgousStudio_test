from rest_framework import serializers
from .models import SceneData


class SceneDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SceneData
        fields = ['username', 'save_time', 'filepath']

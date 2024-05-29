from rest_framework import serializers
from backend.api.models import News


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

from rest_framework import serializers
from backend.api.models import News


class NewsTimelineSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['pid', 'headline', 'author', 'date_published', 'publisher']


class NewsDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

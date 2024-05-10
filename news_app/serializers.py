from rest_framework import serializers
from .models import (
    Tag,
    News
)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            'name',
        ]


class NewsSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    image = serializers.ImageField(required=False, allow_null=True)
    viewers = serializers.SerializerMethodField()
    class Meta:
        model = News
        fields = [
            'id',
            'title',
            'text',
            'image',
            'tags',
            'image',
            'viewers'
        ]
        extra_kwargs = {
            'tags': {'write_only': True}
        }

    def get_viewers(self, obj):
        count = obj.viewers.count()
        return count

    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        news = News.objects.create(**validated_data)
        for tag in tags:
            tag, _ = Tag.objects.get_or_create(**tag)
            news.tags.add(tag)
        return news

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])  # Получаем данные о тегах

        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        if 'image' in validated_data:
            instance.image = validated_data['image']
        instance.save()

        instance.tags.clear()
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(**tag_data)
            instance.tags.add(tag)

        return instance



'''
create news
{
    "title": "qwe",
    "text": "qwe",
    "image": null,
    "tags": [
        {
            "id": 4,
            "name": "sport1"
        }
    ]
}

'''
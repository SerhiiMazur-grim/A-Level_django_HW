from rest_framework import serializers

from .models import Category, Article


""" Звикористанням класу: ModelSerializer """
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'category', 'content', 'added', 'updated')
        read_only_fields = ('added', 'updated')


""" Звикористанням класу: HyperlinkedModelSerializer """
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'id', 'category')

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Article
        fields = ('url', 'id', 'title', 'category', 'content', 'added', 'updated')
        read_only_fields = ('added', 'updated')
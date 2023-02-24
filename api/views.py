from rest_framework.generics import (ListAPIView,
                                    RetrieveAPIView,
                                    CreateAPIView,
                                    UpdateAPIView,
                                    DestroyAPIView)

from blog.serializers import ArticleSerializer
from blog.models import Article


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleCreateAPIView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleUpdateAPIView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDeleteAPIView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
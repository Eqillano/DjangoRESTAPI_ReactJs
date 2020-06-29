from rest_framework.generics import ListAPIView,RetrieveAPIView
from .serializers import ArticleSerializer
from articles.models import Article

class ArticleListView(ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()



class ArticleRetrieveView(ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

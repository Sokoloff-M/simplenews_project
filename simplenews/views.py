from rest_framework import viewsets
from .models import News, Comment
from .serializers import NewsSerializer, CommentSerializer
from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import redirect
from .forms import CommentForm


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'

class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


def add_comment(request, pk):
    news = News.objects.get(pk=pk)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.news = news
            comment.save()
            return redirect('news_detail', pk=pk)

    # В случае ошибок или GET-запроса
    return redirect('news_detail', pk=pk)
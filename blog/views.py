from django.views.generic import ListView,DetailView

# Create your views here.
from .models import Post


class ModelPostView:
    """docstring for PostView"""
    def __init_subclass__(cls, *args, **kwargs):
        super().__init_subclass__(*args, **kwargs)
        cls.model = Post
        cls.context_object_name = 'this_post'
        

class BlogListView(ListView, ModelPostView):
    """docstring for BlogListView
    возвращает в шаблон список объектов модели Post
    """
    # model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView, ModelPostView):
    """docstring for BlogDetailView
    возвращает в шаблон один объект модели Post
    context_object_name не обязательно, но на всякий указал явно
    """
    # model = Post
    # context_object_name = 'this_post'
    template_name = 'post_detail.html'
        
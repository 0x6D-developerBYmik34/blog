from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

# Create your views here.
from django.urls import reverse_lazy
from .models import Post
from .this_utils import to_path


class ModelPostView:
    """docstring for PostView"""
    def __init_subclass__(cls, *args, **kwargs):
        super().__init_subclass__(*args, **kwargs)
        cls.model = Post
        cls.context_object_name = 'this_post'
        

@to_path('', name='home')
class BlogListView(ListView, ModelPostView):
    """docstring for BlogListView
    возвращает в шаблон список объектов модели Post
    """
    template_name = 'home.html'


@to_path('post/<int:pk>/', name='post_detail', model_abs_url=True)
class BlogDetailView(DetailView, ModelPostView):
    """docstring for BlogDetailView
    возвращает в шаблон один объект модели Post
    context_object_name не обязательно, но на всякий указал явно
    """
    template_name = 'post_detail.html'


@to_path('post/new/', name='post_new')
class BlogCreateView(CreateView, ModelPostView):
    """docstring for BlogCreateView
    делает форму в шаблоне в задаваемом в урле id объекта модели(Post)
    fields - какие поля в форме
    """
    template_name = 'post_new.html'
    fields = '__all__'


@to_path('post/<int:pk>/edit/', name='post_edit')
class BlogUpdateView(UpdateView, ModelPostView):
    """docstring for BlogUpdateView
    изменяет форму в шаблоне в задаваемом в урле id объекта модели(Post)
    fields - какие поля в форме
    """
    template_name = 'post_edit.html'
    fields = ['title', 'body']


@to_path('post/<int:pk>/delete/', name='post_delete')
class BlogDeleteView(DeleteView, ModelPostView):
    """docstring for BlogDeleteView
    удаляет форму в шаблоне в задаваемом в урле id объекта модели(Post)
    """
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
        
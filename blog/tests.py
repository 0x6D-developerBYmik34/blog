from django.test import Client, TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post

class BlogTests(TestCase):
    """docstring for BlogTests"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',
        )
        self.post = Post.objects.create(
            title='Все плохо',
            body='fffffdddsdsddd',
            author = self.user,
        )

    def test_str_represent(self):
        post = Post(title='pro suslin')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'Все плохо')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'fffffdddsdsddd')

    def test_post_list_view(self):
        resp = self.client.get(reverse('home'))

        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'fffffdddsdsddd')
        self.assertTemplateUsed(resp, 'home.html')

    def test_post_detail_view(self):
        resp = self.client.get('/post/1/')
        error_resp = self.client.get('/post/10001/')

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(error_resp.status_code, 404)
        self.assertContains(resp, 'Все плохо')
        self.assertTemplateUsed(resp, 'post_detail.html')

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_post_create_view(self):
        resp = self.client.post(reverse('post_new'), {
                'title': 'pro suslin',
                'body': 'some suslin dead for humans rush',
                'author': self.user,
            })
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'pro suslin')
        self.assertContains(resp, 'some suslin dead for humans rush')

    def test_post_update_view(self):
        resp = self.client.post(reverse('post_edit', args='1'), {
                'title': 'new suslin',
                'body': 'new some suslin dead for humans rush',
            })
        self.assertEqual(resp.status_code, 302)

    def test_post_delete_view(self):
        resp = self.client.get(reverse('post_delete', args='1'))
        self.assertEqual(resp.status_code, 200)


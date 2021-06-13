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


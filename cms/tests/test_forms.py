from django.test import TestCase
from django.contrib.auth.models import User
from ..forms import ArticleForm


class ArticleFormTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username='username',
            password='password'
        )
        user.save()

    def test_valid_AddArticle(self):
        title = 'title for article'
        content = 'article new content'
        author = User.objects.get(username='username')
        pub_date = "2011-09-01T13:20:30+03:00"
        form = ArticleForm(
            data={
                'title': title,
                'content': content,
                'author': author,
                'pub_date': pub_date
            }
        )
        self.assertTrue(form.is_valid())

    def test_invalid_AddArticle(self):
        form = ArticleForm(
            data={
                'title': '',
                'content': '',
                'author': '',
                'pub_date': ''
            }
        )
        self.assertFalse(form.is_valid())

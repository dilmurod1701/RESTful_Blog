from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User

from .models import Blog
# Create your tests here.


class TestModels(TestCase):
    def setUp(self) -> None:
        Blog.objects.create(title='chingiz', content='streamer', date='2023-01-01')
        Blog.objects.create(title='serikboy', content='businessmen', date='2020-04-23')
        Blog.objects.create(title='cbum', content='kachka', date='2021-11-11')
        Blog.objects.create(title='speed', content='xaroshiy paren', date='2014-09-24')

    def test_title(self):
        obj1 = Blog.objects.get(title='chingiz')
        obj2 = Blog.objects.get(title='serikboy')
        obj3 = Blog.objects.get(title='cbum')
        obj4 = Blog.objects.get(title='speed')
        self.assertEquals(obj1.title, 'chingiz')
        self.assertEquals(obj2.title, 'serikboy')
        self.assertEquals(obj3.title, 'cbum')
        self.assertEquals(obj4.title, 'speed')

    def test_content(self):
        obj1 = Blog.objects.get(content='streamer')
        obj2 = Blog.objects.get(content='businessmen')
        obj3 = Blog.objects.get(content='kachka')
        obj4 = Blog.objects.get(content='xaroshiy paren')
        self.assertEquals(obj1.content, 'streamer')
        self.assertEquals(obj2.content, 'businessmen')
        self.assertEquals(obj3.content, 'kachka')
        self.assertEquals(obj4.content, 'xaroshiy paren')


class TestView(TestCase):
    def setUp(self) -> None:
        Blog.objects.create(title='chingiz', content='streamer', date='2023-01-01')
        Blog.objects.create(title='serikboy', content='businessmen', date='2020-04-23')
        Blog.objects.create(title='cbum', content='kachka', date='2021-11-11')
        Blog.objects.create(title='speed', content='xaroshiy paren', date='2014-09-24')

    def test_website(self):
        self.client = APIClient()
        response = self.client.get('api/')
        print(response.json())
        return self.assertEquals(response.json()[1]['title'], 'serikboy')

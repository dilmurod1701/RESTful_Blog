from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from selenium import webdriver

from .models import Blog


# Create your tests here.


class TestModels(TestCase):
    def setUp(self) -> None:
        Blog.objects.create(user=User.objects.create_user(username='alabay', password='alabay01'), title='chingiz', content='streamer', date='2023-01-01')
        Blog.objects.create(user=User.objects.create_user(username='alabay1', password='alabay01'), title='serikboy', content='businessmen', date='2020-04-23')
        Blog.objects.create(user=User.objects.create_user(username='alabay2', password='alabay01'), title='cbum', content='kachka', date='2021-11-11')
        Blog.objects.create(user=User.objects.create_user(username='alabay3', password='alabay01'), title='speed', content='xaroshiy paren', date='2014-09-24')

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
        self.client = APIClient()
        Blog.objects.create(user=User.objects.create_user(username='alabay4', password='alabay01'), title='chingiz', content='streamer', date='2023-01-01')
        Blog.objects.create(user=User.objects.create_user(username='alabay5', password='alabay01'), title='serikboy', content='businessmen', date='2020-04-23')
        Blog.objects.create(user=User.objects.create_user(username='alabay6', password='alabay01'), title='cbum', content='kachka', date='2021-11-11')
        Blog.objects.create(user=User.objects.create_user(username='alabay7', password='alabay01'), title='speed', content='xaroshiy paren', date='2014-09-24')

    def test_website(self):
        response = self.client.get('http://127.0.0.1:8000/api/')
        return self.assertEquals(response.json()[1]['title'], 'serikboy')


class BlogSelenium(TestCase):
    def setUp(self) -> None:
        Blog.objects.create(user=User.objects.create_user(username='alabay4', password='alabay01'), title='chingiz', content='streamer', date='2023-01-01')
        Blog.objects.create(user=User.objects.create_user(username='alabay5', password='alabay01'), title='serikboy', content='businessmen', date='2020-04-23')
        Blog.objects.create(user=User.objects.create_user(username='alabay6', password='alabay01'), title='cbum', content='kachka', date='2021-11-11')
        Blog.objects.create(user=User.objects.create_user(username='alabay7', password='alabay01'), title='speed', content='xaroshiy paren', date='2014-09-24')

    def test_selenium(self):
        self.client = APIClient()
        site = webdriver.Chrome()
        site.get('http://127.0.0.1:8000/api')
        assert 'title' in site.page_source

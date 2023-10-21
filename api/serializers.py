from rest_framework import serializers
from django import forms
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class ForListView(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'user',  'title']

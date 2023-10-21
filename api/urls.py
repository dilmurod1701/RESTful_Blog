from django.urls import path

from . import views

urlpatterns = [
    path('', views.Blogs.as_view()),
    path('new', views.CreateBlog.as_view()),
    path('<int:id>', views.DetailBlog.as_view()),
    path('<int:id>/delete', views.DeleteBlog.as_view()),
    path('<int:id>/update', views.UpdateBlog.as_view()),
    path('<str:username>', views.UserDetail.as_view()),
    path('sort/<str:field>', views.SortByName.as_view())
]

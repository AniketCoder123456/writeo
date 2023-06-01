from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerUser, name="register"),

    path("add-article/", views.addarticle, name="add-article"),

    path("single-article/<str:pk>", views.singleArticle, name="single-article"),

    path("delete-message/<str:pk>", views.deleteMessage, name="delete-message"),

    path("user-articles/<str:pk>", views.userArticles, name="user-articles"),

    path("delete-article/<str:pk>", views.deleteArticle, name="delete-article"),

    path("update-article/<str:pk>", views.updateArticle, name="update-article"),



]

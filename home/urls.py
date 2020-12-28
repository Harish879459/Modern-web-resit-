from django.urls import path
from home import views
urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('login',views.login),
    path('logout',views.logout),
    path('blog',views.blog),
    path('blog_details',views.blog_details),
    path('contact',views.contact),
    path('main',views.main),
    path('product',views.product),
    path('shop',views.shop),
]
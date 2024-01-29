from django.urls import path
from my_project import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
]

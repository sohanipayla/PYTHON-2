from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('welcome/',views.welcome,name='welcome'),
    path('add/',views.add_player,name='add_player'),
    path('edit/<int:id>',views.edit_player,name='edit_player'),
    path('delete/<int:id>',views.delete_player,name='delete_player'),
]
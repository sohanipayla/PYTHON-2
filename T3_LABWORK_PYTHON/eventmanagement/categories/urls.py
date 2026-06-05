from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.event_categories, name='event_categories'),
]

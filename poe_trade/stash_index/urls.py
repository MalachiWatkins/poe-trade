from django.urls import path
from stash_index import views

urlpatterns = [
    path('', views.stash_index, name='stash_index'),
]

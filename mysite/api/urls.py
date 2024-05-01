from django.urls import path
from . import views

urlpatterns = [
    path('blogs', views.BlogPostListCreate.as_view(), name='blogpost-view-craete'),
    path('blogs/<int:pk>', views.BlogPostRetrieveUpdateDestroy.as_view(), name='blogpost-view-retrieve-update-destroy')
]
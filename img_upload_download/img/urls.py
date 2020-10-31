from django.urls import path
from .views import ImgFormView, ImgListView, ImgDetail

urlpatterns = [
    path('', ImgListView.as_view(), name='index'),
    path('upload/', ImgFormView.as_view(), name='upload'),
    path('img/<pk>', ImgDetail.as_view(), name='img-detail'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('membre/<str:id_membre>/', views.post_detail, name='post_detail'),
    path('membre/<str:id_membre>/?<str:message>', views.post_detail, name='post_detail_mes'),
]





from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('Membre/<str:id_membre>/', views.post_detail, name='post_detail'),
    path('Membre/<str:id_membre>/?<str:message>', views.post_detail, name='post_detail_mes'),
]





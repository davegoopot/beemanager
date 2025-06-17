from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('hives/', views.hive_list, name='hive_list'),
    path('hives/<int:hive_id>/', views.hive_detail, name='hive_detail'),
    path('hives/<int:hive_id>/add-note/', views.add_note, name='add_note'),
]
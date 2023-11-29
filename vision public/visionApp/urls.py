from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat_view, name='chat_view'),  
    path('purpose/', views.purpose, name='purpose'),
    path('delete_all_messages/', views.delete_all_messages, name='delete_all_messages'),
    path('', views.index, name='index'),
    path('new-bots/', views.new_bots, name='new_bots'),
    path('chat/<str:character>/', views.chat_view, name='chat'),
]

from django.urls import path
from . import views


urlpatterns = [
    # 전체 read, create 
    path('financial/memo/', views.create_or_read),
    # detail, update, delete 
    path('financial/memo/<int:memo_pk>/', views.put_delete_get),
]
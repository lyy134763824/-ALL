from django.urls import re_path,path
from . import views

urlpatterns = [
    re_path(r'index',views.index),
    re_path(r'all_book/',views.all_book),
    path('update/<int:book_id>',views.update),
    path('delete/<int:book_id>',views.delete),
]


# booklib/urls.py
from django.urls import path
from booklib import views

app_name = 'booklib'

# from booklib.views import index
urlpatterns = [
    path('',views.index, name='index'),
    path('bookdetail/',views.bookdetail,name='bookdetail'),
    path('addBook/',views.addBook,name='addBook'),
    path('delBook/<int:book_id>',views.delBook,name='delBook'),
]
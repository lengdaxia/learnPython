from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# from booklib import models
from booklib.models import *

from django.urls import reverse

# Create your views here.
def index(request):
    return HttpResponse('Hello Django!')

def bookdetail(request):
    book_list = Book.objects.order_by('-pub_date')[:5]
    context = {'book_list':book_list}
    return render(request,'booklib/bookdetail.html',context)


def addBook(request):
    if request.method == 'POST':
        tmp_name = request.POST['name']
        tmp_author = request.POST['author']
        tmp_pub_house = request.POST['pub_house']

    from django.utils import timezone
    tmp_book = Book(name=tmp_name,author=tmp_author,pub_house=tmp_pub_house,pub_date=timezone.now())
    tmp_book.save()

    # redirect
    return HttpResponseRedirect(reverse('booklib:bookdetail'))

def delBook(request,book_id):
    bookID = book_id
    Book.objects.filter(id=bookID).delete()
    return HttpResponseRedirect(reverse('booklib:bookdetail'))
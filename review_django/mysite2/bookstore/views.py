from django.shortcuts import render
from bookstore.models import Book
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request,'books/book.html',locals())

def all_book(request):
    if request.method == 'GET':
        books = Book.objects.filter(is_active__exact=True)
        return render(request,'books/all_book.html',locals())

def update(request,book_id):
    book = Book.objects.filter(id__exact=book_id,is_active=True)[0]
    if book:
        if request.method == 'GET':
            # id = request.META['QUERY_STRING']
                # book = Book.objects.filter(id__exat=id)
                return render(request,'books/book_update.html',locals())
        elif request.method == 'POST':
            price = request.POST["price"]
            make_price = request.POST["make_price"]
            book.price = price
            book.make_price = make_price
            book.save()
            return HttpResponseRedirect('/books/all_book')
    else:
        return HttpResponse('no id')

def delete(request,book_id):
    try:
        book = Book.objects.filter(id__exact=book_id)[0]
        if book:
            if request.method == 'GET':
                if book.is_active:
                    book.is_active = False
                    book.save()
                    return HttpResponseRedirect('/books/all_book')
                else:
                    return HttpResponse("is alerady delete")
        else:
            return HttpResponse('no id')
    except Exception as e:
        print(f'--delete book error {e}')
        return HttpResponse('数据库 error')






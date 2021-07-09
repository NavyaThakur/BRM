from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import NewBookForm,SearchForm
from . import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def UserLogin(request):
    data={}
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username ,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect('http://localhost:8000/')
        else:
           data['error']='Username or password incorrect'
           return render(request,'books/user_login.html',data)
    else:
         return render(request,'books/user_login.html',data)
def UserLogout(request):
    logout(request)
    return HttpResponseRedirect('http://localhost:8000/books/login')

@login_required(login_url='http://localhost:8000/books/login')
def viewBooks(request):
    books=models.Book.objects.all()
    res = render(request,'books/view_books.html',{'books':books})
    return res

@login_required(login_url='http://localhost:8000/books/login')
def deleteBooks(request):
    bookid=request.GET['bookid']
    book=models.Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('http://localhost:8000/books/view')

@login_required(login_url='http://localhost:8000/books/login')
def editBooks(request):
    book=models.Book.objects.get(id=request.GET['bookid'])
    fields={'title':book.title,'price':book.price,'author':book.author,'publisher':book.publisher}
    form=NewBookForm(initial=fields)
    res=render(request,'books/edit_books.html',{'form':form,'book':book})
    return res

@login_required(login_url='http://localhost:8000/books/login')
def edit(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.id=request.POST['bookid']
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
        return HttpResponseRedirect('http://localhost:8000/books/view')

@login_required(login_url='http://localhost:8000/books/login')
def searchBooks(request):
    form=SearchForm()
    res=render(request,'books/search_book.html',{'form':form})
    return res

@login_required(login_url='http://localhost:8000/books/login')
def search(request):
    form=SearchForm(request.POST)
    books=models.Book.objects.filter(title=form.data['title'])
    res=render(request,'books/search_book.html',{'form':form,'books':books})
    return res

@login_required(login_url='http://localhost:8000/books/login')
def insertBook(request):
   form=NewBookForm()
   res=render(request,'books/insert_books.html',{'form': form})
   return res

@login_required(login_url='http://localhost:8000/books/login')
def insert(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    s="Record Inserted Successfully <a href='http://localhost:8000/books/view/'>View Books</a>"
    return HttpResponse(s)

@login_required(login_url='http://localhost:8000/books/login')
def homepage(request):
     return render(request,'books/home_page.html')

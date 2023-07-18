from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    context = {
        'books':Book.objects.all()
    }
    return render (request,'books.html',context) 

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        Book.objects.create(
            title = title,
            desc = desc
        )
        return redirect('/') 
def authors(request):
    context = {
        'authors':Author.objects.all()
    }
    return render(request,'authors.html',context)

def add_author(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        notes = request.POST['notes']
        Author.objects.create(
            first_name  = first_name,
            last_name = last_name,
            notes = notes
        )
        return redirect('/authors') 
def connection(request,id):
    book_id = id 
    if request.method == 'POST':
        this_book = Book.objects.get(id = book_id)
        this_author = Author.objects.get(id = request.POST['authors_to_add'])
        this_author.books.add(this_book)
        return redirect('/books/' + str(book_id)) 
def description(request, id):
    context = {
        'book':Book.objects.get(id = id),
        'authors':Author.objects.all()
    }
    return render (request,'description.html',context)    


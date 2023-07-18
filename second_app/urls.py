from django.urls import path     
from . import views
urlpatterns = [ path('', views.index),
               path('add_book', views.add_book, name='add_book'),
               path('authors', views.authors),
               path('add_author', views.add_author, name='add_author'), 
               path('connection/<int:id>', views.connection, name='connection'),
               path('books/<int:id>', views.description, name='desc_page'),

               
                ]
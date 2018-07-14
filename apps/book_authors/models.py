from __future__ import unicode_literals
from django.db import models
# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField("placeholder text")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

#   1. Create 5 books with the following names: C sharp, Java, Python, PHP, Ruby
    # Book.objects.create(name="C sharp")

#   2. Create 5 different authors: Mike, Speros, John, Jadee, Jay
    # Author.objects.create(first_name="Jay")
# 
#   1. Change the name of the 5th book to C#
    # b=Book.objects.last()
    # b.name="C#"
    # b.save()

#   2. Change the first_name of the 5th author to Ketul
    # b=Author.objects.last()
    # b.first_name="Ketul"
    # b.save()

#   3. Assign the first author to the first 2 books
    # this_book = Book.objects.get(id=1)
    # this_author = Author.objects.get(id=1)
    # this_author.books.add(this_book)
    # this_book = Book.objects.get(id=2)
    # this_author.books.add(this_book)

#   4. Assign the second author to the first 3 books
    # this_book1 = Book.objects.get(id=1)
    # this_book2 = Book.objects.get(id=2)
    # this_book3 = Book.objects.get(id=3)
    # this_author = Author.objects.get(id=2)
    # this_author.books.add(this_book1)
    # this_author.books.add(this_book2)
    # this_author.books.add(this_book3)

#   5. Assign the third author to the first 4 books
    # this_book1 = Book.objects.get(id=1)
    # this_book2 = Book.objects.get(id=2)
    # this_book3 = Book.objects.get(id=3)
    # this_book4 = Book.objects.get(id=4)
    # this_author = Author.objects.get(id=3)
    # this_author.books.add(this_book1)
    # this_author.books.add(this_book2)
    # this_author.books.add(this_book3)
    # this_author.books.add(this_book4)

#   6. Assign the fourth author to the first 5 books (or in other words, all the books)
    # this_book1 = Book.objects.get(id=1)
    # this_book2 = Book.objects.get(id=2)
    # this_book3 = Book.objects.get(id=3)
    # this_book4 = Book.objects.get(id=4)
    # this_book5 = Book.objects.get(id=5)
    # this_author = Author.objects.get(id=4)
    # this_author.books.add(this_book1)
    # this_author.books.add(this_book2)
    # this_author.books.add(this_book3)
    # this_author.books.add(this_book4)
    # this_author.books.add(this_book5)

#   7. For the 3rd book, retrieve all the authors
#   this_book = Book.objects.get(id=3)
#   authors = Author.objects.filter(books=this_book)

#   8. For the 3rd book, remove the first author
#   this_book = Book.objects.get(id=3)
#   this_author = Author.objects.get(id=1)
#   this_book.this_author.delete()

#   9. For the 2nd book, add the 5th author as one of the authors
    # this_book = Book.objects.get(id=2)
    # this_author = Author.objects.get(id=5)
    # this_author.books.add(this_book)

#   10. Find all the books that the 3rd author is part of
#   this_author = Author.objects.get(id=3)
#   books = Book.objects.filter(authors=this_author)

#   11. Find all the books that the 2nd author is part of
#   this_author = Author.objects.get(id=2)
#   books = Book.objects.filter(authors=this_author)
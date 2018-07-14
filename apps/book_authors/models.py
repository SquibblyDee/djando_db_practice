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

# 1. Create 5 books with the following names: C sharp, Java, Python, PHP, Ruby
    # Book.objects.create(name="C sharp")
# 2. Create 5 different authors: Mike, Speros, John, Jadee, Jay
    # Author.objects.create(first_name="Jay")
# 
# 1. Change the name of the 5th book to C#
    # b=Book.objects.last()
    # b.name="C#"
    # b.save()

# 2. Change the first_name of the 5th author to Ketul
    # b=Author.objects.last()
    # b.first_name="Ketul"
    # b.save()

# 3. Assign the first author to the first 2 books

# 4. Assign the second author to the first 3 books
# 5. Assign the third author to the first 4 books
# 6. Assign the fourth author to the first 5 books (or in other words, all the books)
# 7. For the 3rd book, retrieve all the authors
# 8. For the 3rd book, remove the first author
# 9. For the 2nd book, add the 5th author as one of the authors
# 10. Find all the books that the 3rd author is part of
# 11. Find all the books that the 2nd author is part of
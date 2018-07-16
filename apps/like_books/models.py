from __future__ import unicode_literals
from django.db import models
# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    # The Many to Many link
    liked_users = models.ManyToManyField(Book, related_name="liked_books")
    # The One to Many Link
    uploader = models.ForeignKey(Book, related_name="uploaded_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
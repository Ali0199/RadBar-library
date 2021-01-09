from django.db import models
from django.contrib.auth.models import User
import os
from .storage import  *

def reader_img_name(instance, filename):
    filename=filename.split('.')
    return '/'.join(['images/reader', "User(id-"+str(instance.id)+")."+filename[-1]])

class Reader(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    phone=models.CharField(max_length=50, null=True)
    user_img=models.ImageField(upload_to=reader_img_name, blank=True)


    def __srt__(self):
        return self.user.username


def book_file_name(instance, filename):
    filename=filename.split('.')
    return '/'.join(['books', "ReadPad"+str(instance.id)+"."+filename[-1]])
def book_img_name(instance, filename):
    filename=filename.split('.')
    return '/'.join(['images/books',  "ReadPad"+str(instance.id)+"."+filename[-1]])
def janr_img_name(instance, filename):
    filename=filename.split('.')
    return '/'.join(['images/janr',  "ReadPadJanr"+str(instance.id)+"."+filename[-1]])

class Janr(models.Model):
    janr=models.CharField(max_length=50) 
    janr_img=models.ImageField(upload_to=janr_img_name,  blank=True)
    class Meta:
        ordering=['janr']
    def __str__(self):
        return self.janr

class Books(models.Model):
    name = models.CharField(max_length=50, default='Anonymous')
    title=models.TextField()
    book_img=models.ImageField(upload_to=book_img_name, null=False,  blank=True)
    bookfile=models.FileField(upload_to=book_file_name, null=False, blank=True)
    aftor=models.CharField(max_length=200)
    cost=models.FloatField(max_length=10)
    janr=models.ForeignKey(Janr, on_delete=models.CASCADE)
    user_id=models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


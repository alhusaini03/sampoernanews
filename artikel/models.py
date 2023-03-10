from django.db import models

from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
# Create your models here.
class Kategori(models.Model):
    nama = models.CharField(max_length=100)
    
    def __str__(self):
         return self.nama
    
    class meta :
        verbose_name_plural = "Kategori"

class Artikel(models.Model):
    nama = models.CharField(max_length=100,blank=True,null=True)
    judul = models.CharField(max_length=100)
    body = models.TextField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{} - {}".format(self.nama, self.judul)
    
    class meta :
        ordering = ['-id']
        verbose_name_plural = "Artikel"


class Info(models.Model):
    title = models.CharField(max_length=1000,primary_key=True)
    description = models.TextField(blank=True,null=True)
    author = models.CharField(max_length=100,blank=True,null=True)
    link = models.CharField(max_length=1000,blank=True,null=True)
    isodate = models.CharField(max_length=1000,blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    image = models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return "{} - {}".format(self.nama, self.judul)

# Create your models here.

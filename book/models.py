from django.db import models
# from django.contrib import admin
# Create your models here.
class Book(models.Model) :
    title = models.CharField(max_length=100, verbose_name="书名")
    description = models.TextField(verbose_name="书籍简介")
    image = models.ImageField(upload_to='book/images/', verbose_name="书籍封面" )
    url = models.URLField(blank=True, verbose_name="电子书链接")

    class Meta:
        verbose_name = "读书"
        verbose_name_plural = "读书"


def __str__(self):
    return self.title
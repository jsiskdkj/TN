from django.contrib import admin
from .models import Movie,Review
# Register your models here.

# admin.site.site_header='自定义标题'
# admin.site.site_title='Python Web开发'

admin.site.register(Movie)
admin.site.register(Review)
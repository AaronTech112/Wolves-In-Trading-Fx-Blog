from django.contrib import admin

# Register your models here.
from . models import Post, Comment, Category, User

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(User)
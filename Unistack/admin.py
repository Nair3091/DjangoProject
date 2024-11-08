from django.contrib import admin
from .models import Post, Answer  # Assuming you have Post and Answer models

# Register your models here
admin.site.register(Post)
admin.site.register(Answer)

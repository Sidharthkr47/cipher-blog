

# Register your models here.
from django.contrib import admin
from .models import Signup, Theory, Post

admin.site.register(Signup)
admin.site.register(Post)
admin.site.register(Theory)
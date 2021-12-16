from django.contrib import admin
from .models import Post, Comments, Events

admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Events)
# admin.site.register(Like)
from django.contrib import admin
from .models import Post, Comments, Events, EventComments, Chat

admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Events)
admin.site.register(EventComments)
admin.site.register(Chat)
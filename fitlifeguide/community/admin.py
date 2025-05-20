
from django.contrib import admin
from .models import Forum, Thread, ForumPost

admin.site.register(Forum)
admin.site.register(Thread)
admin.site.register(ForumPost)

from django.contrib import admin
from .models import BlogPost, Forum, Thread, ForumPost

admin.site.register(BlogPost)
admin.site.register(Forum)
admin.site.register(Thread)
admin.site.register(ForumPost)

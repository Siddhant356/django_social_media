from django.contrib import admin
from home.models import Friend, Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('post','user','updated')

admin.site.register(Post, PostAdmin)
admin.site.register(Friend)

# Register your models here.

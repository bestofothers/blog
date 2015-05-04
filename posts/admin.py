from django.contrib import admin

from .models import Category, Post, Comment, Reply

class PostAdmin(admin.ModelAdmin):
	change_form_template = 'posts/admin/change_form.html'

admin.site.register(Category)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(Reply)
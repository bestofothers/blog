from django.contrib import admin
from django.forms import ModelForm
from .models import Category, Post, Comment, Reply


class PostAdmin(admin.ModelAdmin):
    
    change_form_template = 'posts/admin/change_form.html'
    list_display = (
        'title',
        'slug',
    )
   # prepopulated_fields = {'slug': ('title',)}
    class Meta:
        exclude = ('slug',)
        abstract = True


admin.site.register(Category)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(Reply)
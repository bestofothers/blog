from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import gettext as _



class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(_('slug'), max_length=50, unique=True, populate_from=('category_name',))

    class Meta:
        verbose_name_plural = "categories"

    
    def get_absolute_url(self):
        return 'posts:category', (self.slug,)

    def __str__(self):
        return self.category_name

class Post(models.Model):

    title = models.CharField(max_length=200)
    slug = AutoSlugField(_('slug'), max_length=50, unique=True, populate_from=('title',))
    body = models.TextField()
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField('Created on', auto_now_add=False)
    updated_at = models.DateTimeField( 'Updated on')
    category = models.ForeignKey(Category)
    author = models.ForeignKey(User)
    exclude = ('slug',)

    def get_absolute_url(self):
        return 'posts:post', (self.slug,)

    def __str__(self):
        return self.title

class Comment(models.Model):
    created_at = models.DateTimeField('Created on')
    updated_at = models.DateTimeField( 'Updated on')
    body = models.TextField()
    post = models.ForeignKey(Post)

    def __str__(self):
        return "{}".format(self.post)

class Reply(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    content = models.TextField()
    comment = models.ForeignKey(Comment)

    class Meta:
        verbose_name_plural = "replies"

    def __str__(self):
        return self.name

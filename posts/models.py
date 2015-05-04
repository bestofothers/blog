from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User



class Category(models.Model):
    category_name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse('all_categories')

    def recent_posts(self):
        allp = self.post_set.all().order_by('-created_at')
        return allp[0:1]

    def __str__(self):
        return self.category_name

class Post(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField('Created on', auto_now_add=False)
    updated_at = models.DateTimeField( 'Updated on')
    category = models.ForeignKey(Category)
    author = models.ForeignKey(User)

    def get_absolute_url(self):
        return reverse('index')

    def save(self, *args, **kargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kargs)

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

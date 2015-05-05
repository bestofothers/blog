from django import template

from ..models import Post 

register = template.Library()

@register.inclusion_tag('posts/recent_post.html')
def recent_post():
    latest_posts = Post.objects.all().order_by('-created_at')[0:2]
    return {'latest_posts': latest_posts}
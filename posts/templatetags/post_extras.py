from django import template
register = template.Library()


@register.inclusion_tag('posts/recent_post.html')
def recent_post():
    latest_posts = Post.objects.all().order_by('-id')[1:2]
    return {'latest_posts': latest_posts}
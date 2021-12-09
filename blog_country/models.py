from django.db import models
from post_user import models as post_model
def upload_to(instance, filename):
    return '%s' % filename

class Country(models.Model):
    name = models.CharField(max_length=255)


class Post(models.Model):
    country = models.ForeignKey(Country,
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name='country_post')
    user = models.ForeignKey(post_model.UserPost,
                             on_delete=models.SET_NULL,
                             null=True,
                             related_name='user_post')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='')


class PostImage(models.Model):
    news = models.ForeignKey(Post, on_delete=models.SET_NULL,
                             null=True,
                             related_name='images')
    image = models.ImageField(null=True,
                              blank=True,
                              upload_to=upload_to)


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.DO_NOTHING,
                             related_name='comment_model')
    text = models.TextField()
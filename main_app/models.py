from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
   description = models.TextField(max_length=100)
   user = models.ForeignKey(User, on_delete=models.CASCADE)

   def __str__(self):
        return self.name


class Like(models.Model):
    likes = models.ManyToManyField(User, name='post_like')

    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    description = models.TextField(max_length=100)

    post = models.ForeignKey(Post,on_delete=models.CASCADE, name='comments')

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class Photo(models.Model):
  url = models.CharField(max_length=200)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for post_id: {self.post_id} @{self.url}"
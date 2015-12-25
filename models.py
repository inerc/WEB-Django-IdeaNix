from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
       class Meta():
         db_table = "tag"
       word = models.CharField(max_length=50)

class Profile_User(models.Model):
       class Meta():
          db_table = "profile_user"
       user = models.OneToOneField(User)
       rating = models.IntegerField(default=0)
       avatar_url = models.CharField(max_length=60)

class Article(models.Model):
       class Meta():
            db_table = "article"
      # article_author = models.ForeignKey(Profile_User)
       article_title = models.CharField(max_length=200)
       #article_tag = models.ManyToManyField(Tag)
       article_text = models.TextField()
       article_date = models.DateTimeField(default= datetime.now())
       article_likes = models.IntegerField(default=0)

class Comments(models.Model):
        class Meta():
            db_table = "comments"
        comments_author = models.ForeignKey(Profile_User)
        comments_text = models.TextField()
        comments_date = models.TextField()
        comments_best = models.BooleanField(default=False)
        comments_article = models.ForeignKey(Article)
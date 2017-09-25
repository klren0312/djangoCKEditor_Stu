from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    time = models.CharField(max_length=50)

class Article(models.Model):
    title = models.CharField('标题',max_length=100)
    content = RichTextUploadingField('正文')
    img = models.ImageField('封面图片')
    people = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    def admin_image(self):
        return '<img src="/media/%s" width="100px"/>' % self.img
    admin_image.allow_tags = True
    admin_image.short_description = u'封面图片展示'


class Content(models.Model):
    title = models.CharField(max_length=100)



class Pushcontent(models.Model):
    title = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    people = models.CharField(max_length=100)
    maincontent = RichTextUploadingField('正文')
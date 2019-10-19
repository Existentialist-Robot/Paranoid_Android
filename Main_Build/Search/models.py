from django.db import models

# Create your models here.

class Search(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField() # url friendly string
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)
    thumb = models.ImageField(default="default.png",blank=True)
    author = models.CharField(max_length=30)
    active = models.BooleanField(default=True)
#    tags = TaggableManager()

    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:50] + "..."

class People(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField() # url friendly string
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)
    thumb = models.ImageField(default="default.png",blank=True)
    active = models.BooleanField(default=True)
    # role = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    def snippet(self):
        return self.body[:50] + "..."
    
class Contact(models.Model):
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    from_email = models.EmailField(max_length=256)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    receive_newsletter = models.BooleanField()

from django.db import models
from taggit.managers import TaggableManager
#from .managers import PersonManager

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
 # call with user.profile.bio
 
'''
from django.db.models.signals import post_save
from django.dispatch import receiver
## this is if we are overriding the default user creation forms and adding new fields 
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''


# Create your models here.
class Metadata(models.Model):
    name = models.CharField(max_length=100) # name
    slug = models.SlugField() # url friendly string
    body = models.TextField()
    x_coord = models.IntegerField(max_length=10)
    y_coord = models.IntegerField(max_length=10)
    z_coord = models.IntegerField(max_length=10)
    year = models.CharField(max_length=10)
    month = models.CharField(max_length=10)
    day = models.CharField(max_length=10)
    thumb = models.ImageField(models.ImageField(upload_to='blah', default='assets'))
    date = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    
    def __str__(self):
        return self.name
    def snippet(self):
        return self.body[:50] + "..."

# This is a shitty way of trying to associate one model's objects with another
#class Person(User):
##    objects = PersonManager()
##    class Meta:
##        proxy = True
#    ordering = ('first_name', )
#    widget_group_ids = models.CommaSeparatedIntegerField(max_length=200)
##    base_field=models.IntegerField(),
##    size=100,)
#    # population like this --> f = Foo(int_list="1,2,3,4,5")


'''
# this is a not shitty way - two examples

from django.db import models

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)

'''
#and
'''
#In Django, a one-to-many relationship is called ForeignKey. It only works in one direction, however, so rather than having a number attribute of class Dude you will need

class Dude(models.Model):
    ...

class PhoneNumber(models.Model):
    dude = models.ForeignKey(Dude)
    
#Many models can have a ForeignKey to one other model, so it would be valid to have a second attribute of PhoneNumber such that

class Business(models.Model):
    ...
class Dude(models.Model):
    ...
class PhoneNumber(models.Model):
    dude = models.ForeignKey(Dude)
    business = models.ForeignKey(Business)
    
You can access the PhoneNumbers for a Dude object d with d.phonenumber_set.objects.all(), and then do similarly for a Business object.
'''

# in case this is needed - on_delete=models.CASCADE - as a second ardguement for foreign key function


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

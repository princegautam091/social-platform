from typing import Text
# from django.db.models import *
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='images.png', upload_to='storage')

    def __str__(self):
        return '{}'.format(self.user.username + " Profile")

    @property
    def followers(self):
        return Follow.objects.filter(follow_user=self.user).count()

    @property
    def following(self):
        return Follow.objects.filter(user=self.user).count()

    @property
    def followers_list(self):
        return Follow.objects.filter(user=self.user)

    @classmethod
    def search(cls,username):
        profiles=cls.objects.filter(user__username__icontains=username)
        return profiles

    def __str__(self):
        return self.user.username


class Follow(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    follow_user = models.ForeignKey(User, related_name='follow_user', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    post = models.ImageField(upload_to="storage")
    profileuser = models.ForeignKey(Customer, related_name="profile", on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="likes", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# class User(Model):
# 	email=CharField(max_length=50)
# 	name=CharField(max_length=50,default='')
# 	mobile  = IntegerField(default=0)
# 	password = CharField(max_length=50,default="")

from django.db import models

from django.contrib.auth.models import AbstractUser

class Custom_User(AbstractUser):
    USER=[
        ('bloggers','Bloggers'),('viewers','Viewers')
    ]
    display_name=models.CharField(max_length=100)
    email=models.EmailField(blank=True, null=True)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    user_type=models.CharField(choices=USER,max_length=120)
    def __str__(self):
        return self.display_name
    

class BlogHub(models.Model):

    blog_title=models.CharField(max_length=100,null=True)
    blogger_bio=models.CharField(max_length=100,null=True)
    location=models.CharField(max_length=100,null=True)
    description=models.TextField()
    create_at = models.DateTimeField(auto_now_add=True,null=True)
    blog_creator = models.ForeignKey(Custom_User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.blog_title
    

class BloggersProfile(models.Model):
    user = models.OneToOneField(Custom_User,on_delete=models.CASCADE,null=True, related_name='bloggers')
    profile_picture=models.ImageField(upload_to='media/profile_pic',null=True)

    def __str__(self):
        return self.user.display_name
    

class ViewersProfile(models.Model):
    user = models.OneToOneField(Custom_User,on_delete=models.CASCADE,null=True,related_name='viewers')
    profile_picture=models.ImageField(upload_to='media/profile_pic',null=True)
    
    skills=models.CharField(max_length=100,null=True)


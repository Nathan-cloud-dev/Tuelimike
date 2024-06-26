from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# create profile model
class Profile(models.Model):
    user                    = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name              = models.CharField(max_length=30, blank=False)
    last_name               = models.CharField(max_length=30, blank=True)
    secondary_email         = models.EmailField(blank=False, unique=True)
    website                 = models.URLField(blank=True)
    phone                   = models.CharField(max_length=30, blank=True)
    gender                  = models.CharField(max_length=30, blank=True)
    language                = models.CharField(max_length=30, blank=True)
    bio                     = models.TextField(max_length=500, blank=True)
    birth_date              = models.DateField(null=True, blank=True)
    photo_url               = models.URLField(blank=True)
    # photo                 = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.user.username
    
class Course(models.Model):
    # relation between user and course many to many
    user                   = models.ManyToManyField(User, related_name='courses')
    id                      = models.AutoField(primary_key=True)
    title                   = models.TextField(max_length=50, blank=False)
    category                = models.TextField(max_length=50, blank=False)
    description             = models.TextField(max_length=500, blank=False)
    image                   = models.URLField(blank=False)
    price                   = models.IntegerField(blank=False)
    duration                = models.IntegerField(blank=False)
    created_at              = models.DateTimeField(auto_now_add=True)
    updated_at              = models.DateTimeField(auto_now=True)

    

    def __str__(self):
        return self.user.Course


class Cart(models.Model):
    price                   = models.IntegerField(blank=False)
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    course                  = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at              = models.DateTimeField(auto_now_add=True)
    updated_at              = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
class Feedback(models.Model):
     title = models.TextField(max_length=50 , blank=False)
     description =models.TextField(max_length=200 , blank=False)
     created_at  =models.DateTimeField(auto_now_add=True)

     def __str__(self):
        return self.title
     

class UserCourse(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.userCourse
    

class Event(models.Model):
    title                   = models.CharField(max_length=100)
    capacity                = models.IntegerField()             
    description             = models.TextField()
    start_date              = models.DateTimeField()
    end_date                = models.DateTimeField()
    created_at              = models.DateTimeField(auto_now_add=True)
    updated_at              = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
from django.contrib import admin

# Register your models here.

from .models import Profile, Course, Feedback, Cart, UserCourse

admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Feedback)
admin.site.register(Cart)
admin.site.register(UserCourse)

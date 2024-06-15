from rest_framework import serializers
from django.contrib.auth.models import User

from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    email = serializers.EmailField(required=True)


    def validate_username(self, value):
        if User.objects.filter(username=value.lower()).exists():
            raise serializers.ValidationError("User with this username already exists")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email already exists")
        return value

    def create(self, validated_data):
        self.validate_username(validated_data['username'])
        self.validate_email(validated_data['email'])
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Course
        fields = '__all__'
        courses =User.courses
        


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class meta:
        model = models.Feedback
        fields = '__all__'

class UserCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserCourse
        fields = '__all__'
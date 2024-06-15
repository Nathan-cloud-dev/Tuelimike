from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from . import serializers
from .models import Profile, Course, Feedback, Cart, UserCourse
from . import models
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated



# Create your views here.
class User_ListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

# user by id
class User_RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class Profile_ListCreate(generics.ListCreateAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

class Profile_RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

class Course_ListCreate(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

class Course_RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

class Cart_ListCreate(generics.ListCreateAPIView):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer

class Cart_RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer

class Feedback_ListCreate(generics.ListCreateAPIView):
    queryset = models.Feedback.objects.all()
    serializer_class = serializers.FeedbackSerializer

class Feedback_RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Feedback.objects.all()
    serializer_class = serializers.FeedbackSerializer
# usercourse
class UserCourse_ListCreate(generics.ListCreateAPIView):
    queryset = models.UserCourse.objects.all()
    serializer_class = serializers.UserCourseSerializer

class UserCourse_RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.UserCourse.objects.all()
    serializer_class = serializers.UserCourseSerializer

    
class UserCoursesView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_courses = models.UserCourse.objects.filter(user=request.user)
        serializer = serializers.UserCourseSerializer(user_courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        course_id = request.data.get('course_id')
        if not course_id:
            return Response({'message': 'Course ID is required'}, status=400)

        course = Course.objects.filter(id=course_id).first()
        if not course:
            return Response({'message': 'Course not found'}, status=404)

        existing_booking = UserCourse.objects.filter(user=request.user, course=course).first()
        if existing_booking:
            return Response({'message': 'You have already booked for this Course'}, status=400)

        user_course = UserCourse(user=request.user, course=course)
        user_course.save()
        return Response({'message': 'Course booked successfully'}, status=201)

    def patch(self, request, pk):
        user_course = UserCourse.objects.filter(id=pk).first()
        if not user_course:
            return Response({'message': 'UserCourse not found'}, status=404)

        serializer = serializers.UserCourseSerializer(user_course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'UserCourse updated successfully'})
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        user_course = UserCourse.objects.filter(id=pk).first()
        if not user_course:
            return Response({'message': 'UserCourse not found'}, status=404)

        user_course.delete()
        return Response({'message': 'UserCourse deleted'})
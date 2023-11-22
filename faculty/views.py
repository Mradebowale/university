from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import studentserials

# Create your views here.

@api_view(["GET"])
def homepage(request):
    all_student = Student.objects.all()
    studentlizers = studentserials(all_student, many=True)
    return Response(studentlizers.data)


@api_view(["GET"])
def singles(request, id):
    single_student = Student.objects.get(id=id)
    studentlizer = studentserials(single_student)
    return Response(studentlizer.data)



@api_view(["POST"])
def create_student(request):
    new_student = studentserials(data=request.data)
    if new_student.is_valid():
        new_student.save()
        return Response("New student created successfully")
    return Response(new_student.errors)
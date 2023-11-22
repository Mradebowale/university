from django.db import models

# Create your models here.

faculty_choices = [
    ("SC", "FACULTY OF SCIENCE"),
    ("SMS", "FACULTY OF SOCIAL AND MANAGEMENT SCIENCES"),
    ("ART", "FACULTY OF ART")
]

GENDER_CHOICES = [
    ("M", "MALE"),
    ("F", "FEMALE"),
    ("NB", "NON BINARY")
]

class Student(models.Model):
    name = models.CharField(max_length=200)
    images = models.ImageField(upload_to="studentimages", blank=False, null=False)
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES)
    Matric_number = models.IntegerField()
    faculty = models.CharField(max_length=200, choices=faculty_choices)
    department = models.CharField(max_length=200)
    DOB = models.DateField(auto_now=None)
    # slug = models.SlugField(update=True, blank=True)

    def __str__(self):
        return self.name
    
    


    
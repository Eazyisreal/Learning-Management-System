from django.db import models

# Create your models here.
# Teachers model

class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField
    password = models.CharField(max_length=100)
    class meta:
        verbose_name_plural='Teachers'
    


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length = 100)
    password = models.CharField(max_length=100) 
    interested_categories = models.TextField()
    
    class meta:
        verbose_name_plural='Students'
    
class CourseCategory(models.Model):
    title =  models.CharField(max_length=100)
    description: models.TextField()
    
    class meta:
        verbose_name_plural='Course Categories'
    
    
    
    
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)
    course_description = models.TextField()
    course_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course_student = models.ManyToManyField(Student)
    course_price = models.IntegerField()
    # course_image = models.ImageField(upload_to='course_images')
    course_duration = models.IntegerField()
    course_start_date = models.DateField()
    course_end_date = models.DateField()
    course_status = models.BooleanField(default=False)
    category =  models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    
    class meta:
        verbose_name_plural='Courses'
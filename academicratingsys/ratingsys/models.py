from django.db import models

# Create your models here.
class Lecture(models.Model):
    employee_id = models.IntegerField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)

def __str__(self):
    return f"{self.name} {self.surname} ({self.employee_id})"

class Student(models.Model):
    student_id = models.IntegerField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    qualification = models.ForeignKey('Qualification', on_delete=models.CASCADE)
    year_of_study = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.surname} ({self.student_id})"

class marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam_mark = models.IntegerField(max_length=100)
    semster_mark = models.IntegerField()
    re_exam_mark = models.IntegerField()
    final_mark = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} {self.student.surname} - Total Marks: {self.final_mark}"

class Module(models.Model):
    module_code = models.CharField(max_length=10, unique=True)
    module_name = models.CharField(max_length=100)
    NQF_level = models.IntegerField()
    credits = models.IntegerField()

    def __str__(self):
        return f"{self.module_code} - {self.module_name}"

class modulerating(models.Model):
    rating = models.CharField()
    rating_Description = models.TextField()

    def __str__(self):
        return f"{self.rating} - {self.rating_Description}"

class AnnualCode(models.Model):
    rating = models.ForeignKey(modulerating, on_delete=models.CASCADE)
    Annual_code_Description = models.TextField()

    def __str__(self):
        return f"{self.rating} - {self.Annual_code_Description}"

class Qualification(models.Model):
    qualification_name = models.CharField(max_length=100, unique=True)
    qualification_id = models.CharField()
    qualification_duration = models.IntegerField()
    qualification_minimum_credits = models.IntegerField()

    def __str__(self):
        return f"{self.qualification_name} ({self.qualification_id}) - Duration: {self.qualification_duration} years, Min Credits: {self.qualification_minimum_credits}"
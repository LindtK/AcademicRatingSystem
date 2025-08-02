from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from .models import Module, Lecture, Student, marks

class StudentdetailsForm(forms.Form):
    Qualifications = [
        ('Bachelors', 'BSc Mathematical Sciences')
    ]
    Years_of_Study = [
        (1, 'First Year'),
        (2, 'Second Year'),
        (3, 'Third Year'),
        (4, 'Fourth Year'),
        (5, 'Fifth Year')]
    student_id = forms.IntegerField(label='Student ID', max_value=9999999999)
    name = forms.CharField(label='Name', max_length=100)
    surname = forms.CharField(label='Surname', max_length=100)
    email = forms.EmailField(label='Email', max_length=254)
    Qualification_name = forms.ChoiceField(label='Qualification', choices=Qualifications)
    year_of_study = forms.ChoiceField(choices=Years_of_Study,label='Year of Study')

class studentMarksForm(forms.Form):
    student_id = forms.IntegerField(label='Student ID', max_value=9999999999)
    exam_mark = forms.IntegerField(label='Exam Mark', max_value=100)
    semster_mark = forms.IntegerField(label='Semester Mark')
    re_exam_mark = forms.IntegerField(label='Re-Exam Mark')
    final_mark = forms.IntegerField(label='Final Mark')

# Create your views here.
def index(request):
    return render(request, "ratingsys/index.html")

def captureMarks(request):
    return render(request, "ratingsys/capture_marks.html", {"form": studentMarksForm()})

def captureDetails(request):
    return render(request, "ratingsys/capture_details.html", {"form": StudentdetailsForm()})

def updateResults(request):
    pass

def updateDetails(request):
    pass

def deleteStudent(request):
    pass

def getExamList(request):
    pass 

def performanceReport(request):
    pass

def getClassList(request):
    students = Student.objects.all()
    return render(request, "ratingsys/class_list.html", {"students": students})

def accessAcademicRecord(request):
    pass

def lectureHomescreen(request):
    modules = Module.objects.all()
    return render(request, "ratingsys/lectureview.html", {"modules": modules})
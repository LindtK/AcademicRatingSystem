# from django import forms
# from django.http import HttpResponse
# from django.shortcuts import render
# from .models import Module, Lecture, Student, marks

# class StudentdetailsForm(forms.Form):
#     Qualifications = [
#         ('Bachelors', 'BSc Mathematical Sciences')
#     ]
#     Years_of_Study = [
#         (1, 'First Year'),
#         (2, 'Second Year'),
#         (3, 'Third Year'),
#         (4, 'Fourth Year'),
#         (5, 'Fifth Year')]
#     student_id = forms.IntegerField(label='Student ID', max_value=9999999999)
#     name = forms.CharField(label='Name', max_length=100)
#     surname = forms.CharField(label='Surname', max_length=100)
#     email = forms.EmailField(label='Email', max_length=254)
#     Qualification_name = forms.ChoiceField(label='Qualification', choices=Qualifications)
#     year_of_study = forms.ChoiceField(choices=Years_of_Study,label='Year of Study')

# class studentMarksForm(forms.Form):
#     student_id = forms.IntegerField(label='Student ID', max_value=9999999999)
#     exam_mark = forms.IntegerField(label='Exam Mark', max_value=100)
#     semster_mark = forms.IntegerField(label='Semester Mark')
#     re_exam_mark = forms.IntegerField(label='Re-Exam Mark')
#     final_mark = forms.IntegerField(label='Final Mark')

# # Create your views here.
# def index(request):
#     return render(request, "ratingsys/index.html")

# def captureMarks(request):
#     return render(request, "ratingsys/capture_marks.html", {"form": studentMarksForm()})

# def captureDetails(request):
#     return render(request, "ratingsys/capture_details.html", {"form": StudentdetailsForm()})

# def updateResults(request):
#     pass

# def updateDetails(request):
#     pass

# def deleteStudent(request):
#     pass

# def getExamList(request):
#     pass 

# def performanceReport(request):
#     pass

# def getClassList(request):
#     students = Student.objects.all()
#     return render(request, "ratingsys/class_list.html", {"students": students})

# def accessAcademicRecord(request):
#     pass

# def lectureHomescreen(request):
#     modules = Module.objects.all()
#     return render(request, "ratingsys/lectureview.html", {"modules": modules})


from django import forms
from django.shortcuts import render, get_object_or_404
from django.db.models import Count
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
        (5, 'Fifth Year')
    ]
    student_id = forms.IntegerField(label='Student ID', max_value=9999999999)
    name = forms.CharField(label='Name', max_length=100)
    surname = forms.CharField(label='Surname', max_length=100)
    email = forms.EmailField(label='Email', max_length=254)
    Qualification_name = forms.ChoiceField(label='Qualification', choices=Qualifications)
    year_of_study = forms.ChoiceField(choices=Years_of_Study, label='Year of Study')

class studentMarksForm(forms.Form):
    student_id = forms.IntegerField(label='Student ID', max_value=9999999999)
    exam_mark = forms.IntegerField(label='Exam Mark', max_value=100)
    semster_mark = forms.IntegerField(label='Semester Mark')
    re_exam_mark = forms.IntegerField(label='Re-Exam Mark')
    final_mark = forms.IntegerField(label='Final Mark')

def index(request):
    return render(request, "ratingsys/index.html")

def captureMarks(request):
    if request.method == 'POST':
        form = studentMarksForm(request.POST)
        if form.is_valid():
            # Process the marks data
            student_id = form.cleaned_data['student_id']
            exam_mark = form.cleaned_data['exam_mark']
            semester_mark = form.cleaned_data['semster_mark']
            re_exam_mark = form.cleaned_data['re_exam_mark']
            final_mark = form.cleaned_data['final_mark']
            
            # Save to database (update your model accordingly)
            # marks.objects.create(...)
            
            return render(request, "ratingsys/capture_marks.html", {
                "form": studentMarksForm(),
                "success": True
            })
    return render(request, "ratingsys/capture_marks.html", {"form": studentMarksForm()})

def captureDetails(request):
    if request.method == 'POST':
        form = StudentdetailsForm(request.POST)
        if form.is_valid():
            # Process the student details
            student_id = form.cleaned_data['student_id']
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            qualification = form.cleaned_data['Qualification_name']
            year_of_study = form.cleaned_data['year_of_study']
            
            # Save to database
            # Student.objects.create(...)
            
            return render(request, "ratingsys/capture_details.html", {
                "form": StudentdetailsForm(),
                "success": True
            })
    return render(request, "ratingsys/capture_details.html", {"form": StudentdetailsForm()})

def lecturerHomeScreen(request):
    # Get lecturer's modules with student counts
    lecturer = get_object_or_404(Lecture, name=request.user)
    modules = Module.objects.filter(lecturer=lecturer).annotate(
        student_count=Count('students')
    ).order_by('code')
    
    return render(request, "ratingsys/lectureview.html", {
        "lecturer": lecturer,
        "modules": modules
    })

def getClassList(request, module_id):
    # Get the specific module and its students
    module = get_object_or_404(Module, id=module_id)
    students = Student.objects.filter(modules=module).order_by('surname', 'name')
    
    return render(request, "ratingsys/class_list.html", {
        "module": module,
        "students": students
    })

# Keep your other views as they are
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

def accessAcademicRecord(request):
    pass
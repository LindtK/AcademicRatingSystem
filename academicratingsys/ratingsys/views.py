from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "ratingsys/index.html")

def captureMarks(request):
    pass

def captureDetails(request):
    pass

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

def viewResults(request):
    pass

def accessAcademicRecord(request):
    pass
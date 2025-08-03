# from django.urls import path
# from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
#     path("capture_marks/", views.captureMarks, name="capture_marks"),
#     path("capture_details/", views.captureDetails, name="capture_details"),
#     path("lectureview/", views.lectureHomescreen, name = "lectureview"),
#     path("class_list/",views.getClassList, name="class_list")
# ]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("capture_marks/", views.captureMarks, name="capture_marks"),
    path("capture_details/", views.captureDetails, name="capture_details"),
    path("lecture/", views.lecturerHomeScreen, name="lecturer_view"),
    path("modules/", views.getClassList, name="class_list"),
    
    # Your other URLs
    path("update_results/", views.updateResults, name="update_results"),
    path("update_details/", views.updateDetails, name="update_details"),
    path("delete_student/", views.deleteStudent, name="delete_student"),
    path("exam_list/", views.getExamList, name="exam_list"),
    path("performance_report/", views.performanceReport, name="performance_report"),
    path("academic_record/", views.accessAcademicRecord, name="academic_record"),
]
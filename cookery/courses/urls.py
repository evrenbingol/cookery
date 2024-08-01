from django.urls import path

from . import views

app_name = "courses"


urlpatterns = [
    path("", views.CoursesView.as_view(), name="course"),
    path("<int:pk>/", views.CoutsesDetailsView.as_view(), name="course_details"),
    path("instructor", views.InstructorView.as_view(), name="instructor"),
    path("instructor/<int:pk>/", views.InstructorDetailsView.as_view(), name="instructor_details"),
    path("<int:course_id>/add/", views.add, name="add"),
]
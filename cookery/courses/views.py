from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from courses.models import Course
from django.urls import reverse
# Create your views here.
from django.views import generic
from django.template import loader
from users.models import UserAccount

class CoursesView(generic.ListView):
    template_name = "courses/courses.html"
    context_object_name = "latest_courses_list"
    def get_queryset(self):
        """Return the last five published questions."""
        return  Course.objects.order_by("-date_created")[:5]
    
class InstructorView(generic.ListView):
    template_name = "courses/instructors.html"
    context_object_name = "instructor_list"

    def get_queryset(self):
        return  UserAccount.objects.all()
    
class CoutsesDetailsView(generic.DetailView):
    model = Course
    template_name = "courses/course_details.html"

class InstructorDetailsView(generic.DetailView):
    model = UserAccount
    template_name = "courses/instructor_details.html"


def add(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    course.details = request.POST["details"]
    course.name = request.POST["name"]
    course.save()
    print("Hello")
    return HttpResponseRedirect(reverse("courses:details", args=(course_id,)))
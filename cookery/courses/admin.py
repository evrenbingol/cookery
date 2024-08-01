from django.contrib import admin
from courses.models import Course



class CourseAdmin(admin.ModelAdmin):
    list_display = ["name","instructor"]
    fieldsets = [
        ("Name", {"fields": ["name"]}),
        ("Details", {"fields": ["details"]}),
        ("Instructor", {"fields": ["instructor"]}),
       
    ]

admin.site.register(Course, CourseAdmin)


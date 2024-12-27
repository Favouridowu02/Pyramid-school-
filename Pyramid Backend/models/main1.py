#!/usr/bin/python3
"""
    This Model is used to test the created model
"""
from models.user import User
from models.project import Project
from models.course import Course
from models import storage

storage.reload()

user = User("Favour")
user.save()



course = Course()
course.name = "Pyrmid testing"
course.save()


project = Project()
project.name = "Softwre Engineering"
project.description = "Say cheese"
project.course = course
project.save()


print(project)
#!/usr/bin/python3
"""
    This Model contains the project Class
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship


class Project(BaseModel, Base):
    """
        This Class is used to Create the Project Schema
        It defines the relationship of the Project 
    """
    __tablename__ = "projects"
    name = Column(String(128), nullable=False)
    description = Column(Text, nullable=False)
    duration = Column(Integer, nullable=True)
    estimated_time = Column(Integer, nullable=True)
    markdown = Column(Text, nullable=True)
    course_id = Column(String(60), ForeignKey('courses.id', ondelete="CASCADE"), nullable=False)

    course = relationship("Course", back_populates="projects")
    student_projects = relationship("StudentProject", back_populates="project", cascade="all, delete-orphan")
    tasks = relationship("Task", back_populates="project", cascade="all, delete-orphan")

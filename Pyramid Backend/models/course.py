#!/usr/bin/python3
"""
    This Model contains the Course class
"""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Course(BaseModel, Base):
    """
        This Class is used to create the database Schema of the Course
    """
    __tablename__ = "courses"
    name = Column(String(128), nullable=False)
    projects = relationship("Project", back_populates="course")
    program_id = Column(String(60), ForeignKey('programs.id'), nullable=False)
    program = relationship("Program", back_populates='courses')
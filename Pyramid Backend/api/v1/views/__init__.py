#!/usr/bin/env python3
"""
    This Module is used to set up the blueprint for the models
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from flask import render_template, flash, redirect
from app import app, db, models
import json
import data_handler

@app.after_request
def apply_caching(response):
    '''hide the app version from anything being nosey'''
    response.headers["Server"] = ""
    return response

# -----------------------------
# API route definitions
# -----------------------------
import views_api
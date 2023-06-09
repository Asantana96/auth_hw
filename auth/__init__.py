from flask import Blueprint, render_template

bp =Blueprint('auth', __name__,static_folder="static",template_folder="templates")

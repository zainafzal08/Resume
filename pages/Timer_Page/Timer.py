from flask import Blueprint, request, render_template, abort
import time
from ..API import nav
import json

timer = Blueprint('timer', __name__, template_folder='templates', static_folder='static')

@timer.route('/')
def index():
	navBar = nav.getNav().render("projects",'Timer')
	return render_template('timer.html',navBar=navBar,t=str(time.time()))
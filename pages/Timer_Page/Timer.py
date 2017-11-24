from flask import Blueprint, request, render_template, abort
import time
from ..Common import pexelScraper
from ..Common import nav
import json

nav.register("projects","Timer","/timer")
timer = Blueprint('timer', __name__, template_folder='templates', static_folder='static')

@timer.route('/')
def index():
	navBar = nav.getNav().render("projects",'Timer')
	return render_template('timer.html',navBar=navBar,t=str(time.time()))

@timer.route('/imgRequest')
def imgRequest():
	try:
		w = int(request.args['w'])
		h = int(request.args['h'])
	except:
		abort(404)
	img = pexelScraper.simpleSearch(w,h)
	if img != None:
		return json.dumps(img)
	else:
		abort(404)
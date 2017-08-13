from flask import Blueprint, request, render_template
import time
from ..Common import redditImageScraper
from ..Common import nav
import json

nav.register("projects","DIC","/dic")
dic = Blueprint('dic', __name__, template_folder='templates', static_folder='static')

@dic.route('/')
def index():
	navBar = nav.getNav().render("projects",'DIC')
	if "top" in request.args and "bot" in request.args:
		top = request.args["top"]
		bot = request.args["bot"]
	else:
		top = "CLICK ME"
		bot = "EDIT ME"
	return render_template('DIC.html',top=top,bot=bot,navBar=navBar,t=str(time.time()))

@dic.route('/imgRequest')
def imgRequest():
	try:
		w = int(request.args['w'])
		h = int(request.args['h'])
	except:
		abort(404)
	img = redditImageScraper.simpleSearch(w,h)
	if img != None:
		return json.dumps(img)
	else:
		abort(404)
from flask import Blueprint, request, render_template
import time
from ..Common import redditImageScraper
from ..Common import nav

nav.register("projects","Timer","/timer")
timer = Blueprint('timer', __name__, template_folder='templates', static_folder='static')

@timer.route('/')
def index():
	navBar = nav.getNav().render("projects",'Timer')
	if "offline" in request.args:
		img = {
			"src":"/static/test.jpg",
			"credit":"google"
		}
	else:
		img = redditImageScraper.getSimpleBackImage()
	return render_template('timer.html',backImg=img,navBar=navBar,t=str(time.time()))

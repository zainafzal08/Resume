from flask import Blueprint, request, render_template
import time
from ..Common import redditImageScraper
from ..Common import nav

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

	if "offline" in request.args:
		img = {
			"src":"/static/test.jpg",
			"credit":"google"
		}
	else:
		img = redditImageScraper.getSimpleBackImage()
	return render_template('DIC.html',top=top,bot=bot,backImg=img,navBar=navBar,t=str(time.time()))


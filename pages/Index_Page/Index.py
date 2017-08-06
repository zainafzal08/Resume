from flask import Blueprint, request, render_template
import time
from ..Common import redditImageScraper
from ..Common import nav


nav.initalise("Zain Afzal","/index")
nav.register("index","Home","#welcome-block")
nav.register("index","About","#about-block")
nav.register("index","Projects","#project-block")

indexPage = Blueprint('indexPage', __name__, template_folder='templates', static_folder='static')

@indexPage.route('/')
def index():
	navBar = nav.getNav().render('index','Home')
	projects = nav.getNav().projectList()
	img = None
	if "offline" in request.args:
		img = {
			"src":"/static/test.jpg",
			"credit":"google"
		}
	else:
		img = redditImageScraper.getSimpleBackImage()
	return render_template('index.html',navBar=navBar,backImg=img,projects=projects,prjLen=len(projects),t=str(time.time()))
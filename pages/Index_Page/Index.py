from flask import Blueprint, request, render_template
import time
from ..Common import redditImageScraper
from ..Common import nav
import json
from flask import abort

nav.initalise("Zain Afzal","/index")
nav.register("index","Home","#welcome-block")
nav.register("index","About","#about-block")
nav.register("index","Projects","#project-block")

indexPage = Blueprint('indexPage', __name__, template_folder='templates', static_folder='static')

@indexPage.route('/')
def index():
	navBar = nav.getNav().render('index','Home')
	projects = nav.getNav().projectList()
	return render_template('index.html',navBar=navBar,projects=projects,prjLen=len(projects),t=str(time.time()))

@indexPage.route('/imgRequest')
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

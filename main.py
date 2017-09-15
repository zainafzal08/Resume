from flask import Flask, render_template, request, g, session, redirect
from pages.DIC_Page.DIC import dic
from pages.Timer_Page.Timer import timer
from pages.Index_Page.Index import indexPage
from pages.Flashcard_Page.Flashcard import flashcard
from pages.BFD_Page.BF_Machine import bfd
from pages.API import Api

app = Flask(__name__)
app.secret_key = 'B3Dvm1BJF1'

# Helper Functions

def addPage(bp,urlp,*args):
	global app
	app.register_blueprint(bp,url_prefix=urlp)
	navTitle = None
	if len(args) >= 1:
		navTitle = args[0]
	if navTitle:
		Api.registerPage(navTitle,urlp)

def addSubPage(page, title, link):
	Api.addSubPage(page, title, link)

# project pages

addPage(dic,'/dic',"Dic")
addPage(timer,'/timer',"Timer")
addPage(flashcard,'/flashcard',"Flashcard")
addPage(bfd,'/bfd',"BFD")
addPage(indexPage,'/index')

# bind the api system to a route
addPage(Api.api,'/api')

# subpage links
addSubPage("main","Home","#welcome-block")
addSubPage("main","About","#about-block")
addSubPage("main","Projects","#project-block")


# Flask Routes

@app.route('/')
def index():
	return redirect("/index", code=302)


if __name__ == "__main__":
	app.run(debug=True)

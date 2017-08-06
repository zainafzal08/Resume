from flask import Flask, render_template, request, g, session, redirect
from pages.DIC_Page.DIC import dic
from pages.Timer_Page.Timer import timer
from pages.Index_Page.Index import indexPage
from pages.Flashcard_Page.Flashcard import flashcard
from pages.BFD_Page.BF_Machine import bfd
app = Flask(__name__)
app.secret_key = 'B3Dvm1BJF1'

app.register_blueprint(dic,url_prefix='/dic')
app.register_blueprint(timer,url_prefix='/timer')
app.register_blueprint(indexPage,url_prefix='/index')
app.register_blueprint(flashcard,url_prefix='/flashcard')
app.register_blueprint(bfd,url_prefix='/bfd')

@app.route('/')
def index():
	return redirect("/index", code=302)

if __name__ == "__main__":
	app.run(debug=True)

import pexelScraper
import json

from flask import Flask, render_template, request, g, session, redirect
app = Flask(__name__)
app.secret_key = 'B3Dvm1BJF1'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/imgRequest')
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

if __name__ == "__main__":
	app.run(debug=False)

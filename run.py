import pexelScraper
import json

from flask import Flask, render_template, request, g, session, redirect, abort
app = Flask(__name__)
app.secret_key = 'B3Dvm1BJF1'

shortcuts = {
    "cs2521": "https://github.com/zainafzal08/COMP2521-18s1",
    "comp2521": "https://github.com/zainafzal08/COMP2521-18s1",
    "2521": "https://github.com/zainafzal08/COMP2521-18s1",
    "3131": "https://github.com/zainafzal08/cs3131"
}
notes = {
    "comp3131":
}
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<page>')
def direct(page):
    global redirects
    if page in shortcuts:
        return redirect(shortcuts[page])
    abort(404)

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

# notes api
@app.route('/notesapi/<course>/<file>')
def notesRender(course, file):
    abort(404)

@app.route('/notesapi/<course>')
def notesCourseIndex(course):
    abort(404)

@app.route('/notesapi')
def notesIndex():
    abort(404)

if __name__ == "__main__":
	app.run(debug=False)

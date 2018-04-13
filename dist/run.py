import pexelScraper
import json
import os
import base64
import requests
import time
from mdRenderer import render
import datetime

from flask import Flask, render_template, request, g, session, redirect, abort
app = Flask(__name__)
cache = {}
testing = True
app.secret_key = 'B3Dvm1BJF1'

shortcuts = {
    "cs2521": "https://github.com/zainafzal08/COMP2521-18s1",
    "comp2521": "https://github.com/zainafzal08/COMP2521-18s1",
    "2521": "https://github.com/zainafzal08/COMP2521-18s1",
    "3131": "https://github.com/zainafzal08/cs3131"
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

def requestDesc():
    url = "https://api.github.com/repos/zainafzal08/Notes/contents/desc.json"
    res = requests.get(url)
    desc = json.loads(base64.b64decode(res.json()["content"]))
    return desc

def getDesc():
    lu = int(os.environ.get('GITHUB_LAST_UPDATE'))
    if (cache["lastUpdate"] < lu):
        cache["desc"] = requestDesc()
        cache["lastUpdate"] = int(time.time())
    return cache["desc"]

def getNotesRoot():
    desc = getDesc()
    res = list(map(lambda x: {
        "name": x,
        "link": "#/notes/%s"%x,
        "sub":desc["subs"].get(x,"Some markdown notes"),
        "count":desc["counts"].get(x,"N/A")
        }, desc["tree"].keys()))
    return res

def getCourse(course):
    desc = getDesc()
    if course not in desc["tree"]:
        return None
    res = list(map(lambda x: {
            "name": x,
            "link":"#/notes/%s/%s"%(course,x)
        }, desc["tree"][course]))
    return res

def getFile(course, file):
    url = "https://api.github.com/repos/zainafzal08/Notes/contents/%s/%s"%(course,file)
    res = requests.get(url)
    files = res.json()
    mdFile = [f for f in files if f["name"].split(".")[1] == "md"][0]
    res = requests.get(mdFile["download_url"])
    return res.text

def renderMarkdown(raw):
    return render(raw)

def jsonResponse(j):
    response = app.response_class(
        response = json.dumps(j),
        status = 200,
        mimetype = 'application/json'
    )
    if(testing):
        response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/notesUpdate')
def notesUpdate():
    os.environ['GITHUB_LAST_UPDATE'] = str(int(time.time()))
    return redirect("/")

@app.route('/notesapi/<course>/<file>')
def notesRender(course, file):
    desc = getDesc()
    if course not in desc["tree"]:
        abort(404)
    if file not in desc["tree"][course]:
        abort(404)
    return jsonResponse({"rendered":renderMarkdown(getFile(course,file))})

@app.route('/notesapi/<course>')
def notesCourseIndex(course):
    jsonDump = getCourse(course)
    if not jsonDump:
        abort(404)
    return jsonResponse(jsonDump)

@app.route('/notesapi')
def notesIndex():
    return jsonResponse(getNotesRoot())

# logging

@app.route('/logme')
def logme():
    f = open("log.txt","w+")
    leNow = datetime.datetime.now().strftime("%d %b %Y %I:%M %p")
    leArgs = ["%s:%s"%(x,request.args[x]) for x in request.args.keys()]
    leArgs = ",".join(leArgs)
    f.write("%s$%s\n"%(leNow,leArgs))
    f.close()
    return jsonResponse({"msg":"yoinks!"})

@app.route('/log')
def log():
    f = open("log.txt","r")
    daLog = f.read().split("\n")
    daLog = [x.split("$") for x in daLog]
    f.close()
    return render_template("log.html",log=daLog)

if __name__ == "__main__":
    now = int(time.time())
    os.environ['GITHUB_LAST_UPDATE'] = str(now)
    cache["desc"] = requestDesc()
    cache["lastUpdate"] = now
    app.run(debug=False)

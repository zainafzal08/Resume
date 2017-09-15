from flask import Blueprint, request, render_template, abort
import redditImageScraper
import time
import json
import os
from nav import Nav

api = Blueprint('api', __name__)
globalNav = Nav("Zain Afzal","/")

@api.route('/imgRequest')
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

@api.route('/getProjects')
def getProjects():
	with open("projects.txt", "r") as f:
		try:
			j = json.load(f)
		except:
			raise Exception("Malformed projects json")
	return str(j)

@api.route('/getNav')
def getNav():
	global globalNav
	return globalNav.getJson()

def registerPage(title, url):
	global globalNav
	globalNav.addPage(title,url)

def addSubPage(page, title, url):
	global globalNav
	globalNav.addSubPage(page,title,url)
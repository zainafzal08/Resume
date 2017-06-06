from flask import Flask, render_template, request, g, session, redirect
import time
from random import randint

def handleRequest(request):
	# we don't handle any posts
	# just redirect to request page if so
	if request.method != "GET":
		return render_template("timer_request.html", tag=str(time.time()))
	# check if any of the needed args are missing
	if "title" not in request.args:
		return render_template("timer_request.html", tag=str(time.time()))
	if "time_mins" not in request.args:
		return render_template("timer_request.html", tag=str(time.time()))
	if "time_hours" not in request.args:
		return render_template("timer_request.html", tag=str(time.time()))
	# get the settings
	timer_title = request.args["title"]
	changeCol = False
	solidCol = "off"
	if "solidCol" in request.args:
		solidCol = request.args["solidCol"]
	if solidCol == "on":
		imgName = None
		if "changeCol" in request.args:
			if request.args["changeCol"] == "on":
				changeCol = True
	else:
		imgName = getRandomImg(-1);

	if "cheat" in request.args:
		imgName = getRandomImg(request.args["cheat"]);
	# calculate the static numbers needed by client side JS
	timer_time = int(request.args["time_mins"])+60*int(request.args["time_hours"])
	danger = int(request.args["danger"].split(" ")[0])*60
	timer_time_final = timer_time*60 # we like seconds
	# forms the rendering dict
	renderingParams = {
		"changeCol" : changeCol,
		"danger_time" : danger,
		"imgName" : imgName,
		"title" : timer_title,
		"timer_time" : timer_time_final,
		"tag" : str(time.time())
	}
	return render_template("timer.html", **renderingParams)

def getRandomImg(cheat):
	imgs = []
	imgs.append("hipster_1.jpg")
	imgs.append("hipster_2.jpg")
	imgs.append("hipster_3.png")
	imgs.append("hipster_4.png")
	imgs.append("hipster_5.jpg")
	imgs.append("hipster_6.jpg")
	imgs.append("hipster_7.jpg")
	imgs.append("hipster_8.jpg")
	imgs.append("hipster_9.jpg")
	if cheat != -1:
		randNum = int(cheat)-1
	else:
		randNum = randint(0,len(imgs)-1)
	return imgs[randNum]

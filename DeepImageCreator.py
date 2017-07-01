from flask import Flask, render_template, request, g, session, redirect
import time
from random import randint

def handleRequest(request):
	# we don't handle any posts
	# just redirect to request page if so
	if request.method != "GET":
		return render_template("DIC_request.html", tag=str(time.time()))
	# check if any of the needed args are missing
	if "top" not in request.args:
		return render_template("DIC_request.html", tag=str(time.time()))
	if "bot" not in request.args:
		return render_template("DIC_request.html", tag=str(time.time()))
	
	# get the params
	top = request.args["top"]
	bot = request.args["bot"]
	cheat = -1
	if "cheat" in request.args:
		cheat = request.args["cheat"]
		
	img = getRandomImg(cheat)
	return render_template("DIC.html", top=top, bot=bot, img=img)

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

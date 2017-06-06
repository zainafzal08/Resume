# small script to convert a flashcard
# txt into actual randomised flashcards
import sys
import random
from flask import Flask, render_template, request, g, session, redirect
import time

def handleRequest(request):
	if request.method == "GET":
		return render_template("flashcards_request.html", tag=str(time.time()))
	# otherwise it's a post
	# get the raw data
	title = request.form['title']
	inputText = request.form['inputText']
	# process
	flashcards = getFlashcards(inputText)
	# render
	return render_template("flashcards.html", tag=str(time.time()), title=title, flashcards=flashcards)

def getFlashcards(inputText):
	flashcards = []
	count = 1
	question = "ERROR"
	inputTextLines = inputText.split("\n")
	for line in inputTextLines:
		if(count % 3 == 0):
			count = 1
			continue
		elif(count % 2 == 0):
			flashcards.append((question, line.strip()))
		else:
			question = line.strip();
		count+=1

	random.shuffle(flashcards)
	return flashcards




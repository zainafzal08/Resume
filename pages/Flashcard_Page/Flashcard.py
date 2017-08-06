# small script to convert a flashcard
# txt into actual randomised flashcards
import sys
import random
from flask import Flask, render_template, request, g, session, redirect, Blueprint
import time
import re
from ..Common import nav

nav.register("projects","Flashcard","/flashcard")
flashcard = Blueprint('flashcard', __name__, template_folder='templates', static_folder='static')

@flashcard.route('/',methods=["GET","POST"])
def index():
	return handleRequest(request)

class ParseError(Exception):
    pass

def handleRequest(request):
	navBar = nav.getNav().render("projects",'Flashcard', dark=True)
	if request.method == "GET":
		return render_template("flashcards_request.html", navBar=navBar, err=False, tag=str(time.time()))
	# otherwise it's a post
	# get the raw data
	title = request.form['title']
	inputText = request.form['inputText']
	# sanitise
	inputText = re.sub(r'\<', r'&lt;', inputText);
	inputText = re.sub(r'\>', r'&gt;', inputText);
	inputText = re.sub(r'\r', r'', inputText);
	# process
	try:
		flashcards = getFlashcards(inputText)
	except ParseError as errMsg:
		errMsgList = str(errMsg).split(":")
		return render_template("flashcards_request.html", navBar=navBar, err=True, original=inputText, msg=errMsgList, tag=str(time.time()))
	# render
	return render_template("flashcards.html", navBar=navBar, tag=str(time.time()), title=title, flashcards=flashcards, count=len(flashcards))


def multiSplit(text, sep):
	l = len(sep)
	currCount = 0
	result = []
	buffer = []
	for c in text:
		if(c == sep[currCount]):
			currCount+=1
			if(currCount == l):
				end = len(buffer) - l
				result.append("".join(buffer[0:end]))
				buffer = []
				currCount = 0
		else:
			currCount = 0
		buffer.append(c)
	if(len(buffer) > 0):
		result.append("".join(buffer))
	return result
# must return an array of question, answer, string tuples
def getFlashcards(inputText):
	cardSeperator = "\n\n"
	QASeperator = "\n---\n"
	rawCards = inputText.split(cardSeperator)
	flashcards = []
	for i,rawCard in enumerate(rawCards):
		bits = rawCard.split(QASeperator)
		if(len(bits) < 2):
			raise ParseError("Malformed Card: \n"+rawCard)
		question = compile(bits[0])
		answer = compile(bits[1])
		flashcards.append((question, answer, i))
	# shuffle and return
	random.shuffle(flashcards)
	return flashcards

# inserts a table into list of lines
def insertTable(lines, table, index):
	for i,l in enumerate(lines):
		if l == "!table["+str(index)+"]":
			lines[i] = table
			return
	raise Exception("Index not Found")

def compileTable(rawTable):
	final = []
	final.append("<br><table class='table table-striped table-hover'>")
	final.append("  <tbody>")
	for line in rawTable:
		final.append("    <tr>")
		cleanLine = re.sub(r'\s+',r' ', line)
		for data in cleanLine.split(" "):
			final.append("      <td>"+data+"</td>")
		final.append("    </tr>")
	final.append("  </tbody>")
	final.append("</table>")
	return "\n".join(final)

# compiles tables and the such
def compile(text):
	currTable = -1
	result = []
	tables = []
	inTable = False
	# get base positioning and line seperation
	for line in text.split('\n'):
		if(line == "!endtable"):
			inTable = False
			continue
		if(line == "!table"):
			inTable = True
			currTable+=1
			tables.append([])
			result.append(line+"["+str(currTable)+"]")
			continue
		if(inTable):
			tables[currTable].append(line)
		else:
			result.append(line)
	# now compile down tables
	for index, table in enumerate(tables):
		t = compileTable(table)
		insertTable(result, t, index)
	#remember to join with "<br>"
	return "<br>".join(result)
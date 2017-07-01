from flask import Flask, render_template, request, g, session, redirect
import Timer
import time
import BF_Machine
import Flashcard
import DeepImageCreator

app = Flask(__name__)
app.secret_key = 'B3Dvm1BJF1'

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template("index.html", tag=str(time.time()))

@app.route('/timer', methods=['GET', 'POST'])
def timer():
	return Timer.handleRequest(request)

@app.route('/DIC', methods=['GET', 'POST'])
def dic():
	return DeepImageCreator.handleRequest(request);

@app.route('/flashcard', methods=['GET', 'POST'])
def flashcard():
	return Flashcard.handleRequest(request)

@app.route('/BFD', methods=['GET', 'POST'])
def BFD():
	return BF_Machine.handleRequest(request, 80, session)

if __name__ == '__main__':
	app.run(debug=True)
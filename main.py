from flask import Flask, render_template, request, g, session, redirect
import time
import BF_Machine
from random import randint

app = Flask(__name__)
app.secret_key = 'B3Dvm1BJF1'

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template("index.html", tag=str(time.time()))

@app.route('/timer', methods=['GET', 'POST'])
def timer():
	if request.method == "GET":
		if "title" in request.args and "time_mins" in request.args and "time_hours" in request.args:
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

			timer_time = int(request.args["time_mins"])+60*int(request.args["time_hours"])
			danger = int(request.args["danger"].split(" ")[0])*60
			timer_time_final = timer_time*60 # we like seconds
			return render_template("timer.html", changeCol = changeCol, danger_time = danger, imgName = imgName, title = timer_title, timer_time = timer_time_final, tag=str(time.time()))
		else:
			return render_template("timer_request.html", tag=str(time.time()))
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

@app.route('/BFD', methods=['GET', 'POST'])
def BFD():
	if request.method == "GET":
		session['pc'] = -1
		return render_template("BFDIN.html")
	else:
		noPost = False
		if session['pc'] == -1:
			#first time, grab code
			session['code'] = request.form['code']
			try:
				session['code'][0]
			except:
				return redirect("/BFD")
			session['pc'] = 0
			session['scroll'] = 0
			noPost = True
		machine = BF_Machine.Machine(80)
		success = machine.loadCode(session['code'])
		if not success: 
			return redirect("/BFD")
		#get back to old state
		machine.runFor(session['pc'])
		if noPost == False:
			if request.form["post"] == "step+":
				machine.step()
			elif request.form["post"] == "step-":
				reset = session['pc'] - 1
				machine = BF_Machine.Machine(80)
				machine.loadCode(session['code'])
				machine.runFor(reset)
			elif request.form["post"] == "skip":
				machine.skipLoop()
			elif request.form["post"] == "run":
				machine.run()
			elif request.form["post"] == "next":
				machine.nextLoop(True)
			session['pc'] = machine.cycles
			session['scroll'] = request.form['scroll']
		return render_template('BFD.html', code=machine.codeToHTML(), console=machine.consoleToHTML(), memory=machine.memoryToHTML(), scroll=session['scroll'])

if __name__ == '__main__':
	app.run(debug=True)
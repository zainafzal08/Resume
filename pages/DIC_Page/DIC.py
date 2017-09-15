from flask import Blueprint, request, render_template
import time
import json

dic = Blueprint('dic', __name__, template_folder='templates', static_folder='static')

@dic.route('/')
def index():
	if "top" in request.args and "bot" in request.args:
		top = request.args["top"]
		bot = request.args["bot"]
	else:
		top = "CLICK ME"
		bot = "EDIT ME"
	return render_template('DIC.html',top=top,bot=bot,t=str(time.time()))
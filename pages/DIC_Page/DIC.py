from flask import Blueprint, request, render_template
import time
import json

dic = Blueprint('dic', __name__, template_folder='templates', static_folder='static')

@dic.route('/')
def index():
	return render_template('DIC.html', t=str(time.time()))
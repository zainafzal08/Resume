from flask import Blueprint, request, render_template
import time
import json
from flask import abort

indexPage = Blueprint('indexPage', __name__, template_folder='templates', static_folder='static')

@indexPage.route('/')
def index():
	return render_template('index.html',t=str(time.time()))

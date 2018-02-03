from flask import Flask, render_template, request, g, session, redirect
app = Flask(__name__)
app.secret_key = 'B3Dvm1BJF1'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)

from flask import Flask, render_template, request, g, session, redirect
app = Flask(__name__,static_url_path='')
app.secret_key = 'B3Dvm1BJF1'

@app.route('/')
def index():
    return app.send_static_file('dist/index.html')

if __name__ == "__main__":
	app.run(debug=True)

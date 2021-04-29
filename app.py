from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, This is Shing."

@app.route("/index")
def index():
	return render_template('/index.html')
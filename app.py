from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route('/')
def home():
	return "Hello world"

@app.route('/welcome')	
def welcome():
	return render_template("welcome.html")

@app.route('/test/<search_query>')
def search(search_query):
	return search_query

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid credentials. Please try again'
		else:
			return redirect(url_for('home'))


	return render_template('login.html', error=error)

@app.route("/integer/<int:value>")
def int_type(value):
	print value + 1
	return "correct"

@app.route("/float/<float:value>")
def float_type(value):
	print value + 1
	return "correct"

@app.route("/path/<path:value>")
def path_type(value):
	print value
	return "correct"

@app.route('/name/<name>')
def index(name):
	if name.lower() == "michael":
		return "Hello, {}".format(name), 200
	else:
		return "Not found", 404


if __name__ == '__main__':
	app.run()


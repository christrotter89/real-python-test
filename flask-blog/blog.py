#config

DATABASE = 'blog.db'

app.config.from_object(__name__)

@app.route('/')
def login():
	return render_template('login.html')

@app.route('/main')
def main():
	return render_template('main.html')

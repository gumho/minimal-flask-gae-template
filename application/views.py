from myapp import app

@app.route('/')
def index():
	return "Stay thirsty, my friends"
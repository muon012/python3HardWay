from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/hello', methods=['POST', 'GET'])
def index():

	greeting = "Hello World"

	if request.method == 'POST':
		name = request.form['name']
		greet = request.form['greet']
		greeting = f"{greet}, {name}"
		return render_template("index.html", greeting=greeting)
	else:
		return render_template("hello_form.html")


if __name__ == "__main__":
	app.run()

# Type this on your browser after you run this server on your computer:
# http://localhost:5000/hello?name=Toto&greet=%E4%BD%A0%E5%A5%BD

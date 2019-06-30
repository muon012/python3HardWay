from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
	greeting = "Hello World"
	return render_template("index.html", greeting=greeting)


if __name__ == "__main__":
	app.run()


# To run this app just go to the directory "ex50" on Terminal. Type "python3 app.py" then go to the port specified
# on the Terminal log using your web browser. This coed is executing the "index.html" file in the "templates" directory.

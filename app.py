from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<b>Hello World!</b>"

# this is tge goodbye thing
@app.route("/goodbye")
def goodbye():
	return "goodbye"

app.run()
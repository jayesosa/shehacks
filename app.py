import pickle
from flask import Flask, request
app = Flask(__name__)

#This makes an endpoint that the form will go to
@app.route("/form", methods=["POST"])
def form():
	print (request.form)
	values = request.form
	singleRecord = Record(values['location'], values['age'], values['zipcode'],values['gender'], values['ethinicity'], values['height'], values['weight'], values['medication'],values['dosage'],values['dosing'], values['painAmount'], values['pillsUsed'])
	records.append(singleRecord)
	pickle.dump(records,open('records.pickle','wb'))
	return ""

@app.route("/")
def hello():
	html_file = open("structure.html")
	html_response = html_file.read()
	return html_response


# this is tge goodbye thing
@app.route("/goodbye")
def goodbye():
	return "goodbye"

try:
	records = pickle.load(open('records.pickle','rb'))
except:
	records = []

app.run()

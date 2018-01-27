import pickle
from pickleHack import Record
from flask import Flask, request
from bs4 import BeautifulSoup
import urllib2
app = Flask(__name__)


#This makes an endpoint that the form will go to
@app.route("/form", methods=["POST"])
def form():
	print (request.form)
	try:
		values = request.form
		print(values)
		singleRecord = Record(values['age'], values['procedure'], values['zipcode'],values['gender'], values['race'], values['height'], values['weight'], values['medication'],values['dosage'],values['doses'])
		print(singleRecord)
		records.append(singleRecord)
		pickle.dump(records,open('records.pickle','wb'))

		url = urllib2.urlopen("https://en.wikipedia.org/wiki/Egypt").read()

		soup = BeautifulSoup(url)

		for link in soup.find_all('a'):
		     print(link.get('href'))

		return soup
		# html_file = open("graphs.html")
		# html_response = html_file.read()

		# return html_response
	except Exception as e:
		print(e)
		return "oops"
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

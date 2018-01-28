import pickle
from pickleHack import Record
from flask import Flask, request
from bs4 import BeautifulSoup
import urllib
import subprocess
from subprocess import call


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


		class AppURLopener(urllib.FancyURLopener):version = "Mozilla/5.0"
		urllib._urlopener = AppURLopener()
		f = urllib.urlopen("http://datawrapper.dwcdn.net/aL51p/3/")
		myfile = f.read()
		print myfile
		mydata = myfile.split("/n")
		for line in mydata:
			cell = line.split("/t")
			if cell[0] == singleRecord.procedure:
				print line

		# if singleRecord.procedure = 
		#split myfile by /n
		#split each line by /t
		#we have 13 rows
		#check singlerecord.procedure == xxx
		#then return that row 

		#create another file and create button to click here
		return "http://disposemymeds.org/medicine-disposal-locator/"
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

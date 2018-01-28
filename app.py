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
		opioids = "Hydrocodone (Vicodin and Norco) 5 mg tablet\tCodeine (Tylenol #3) 30 mg tablets\tTramadol 50 mg tablets\tOxycodne 5 mg tablets"
		newfile= "\nLaparoscopic Cholecystectomy\t15\t15\t15\t10\nLaparoscopic Appendectomy\t15\t15\t15\t10\nInguinal\/Femoral Hernia Repair (open\/laparoscopic)\t15\t15\t15\t10\nOpen Incisional Hernia Repair\t40\t40\t40\t25\nLaparoscopic Colectomy\t35\t35\t35\t25\nOpen Colectomy\t40\t40\t40\t25\nHysterectomy vaginal \t20\t20\t20\t15\nHyseretomy Laparoscopic & Robotic\t30\t30\t30\t20\nHysterectomy Abdominal \t40\t40\t40\t25\nWide Local Excision \u00b1 Sentinel Lymph Node Biopsy\t30\t30\t30\t20\nSimple Mastectomy \u00b1 Sentinel Lymph Node Biopsy\t30\t30\t30\t20\nLumpectomy \u00b1 Sentinel Lymph Node Biopsy\t15\t15\t15\t10\nBreast Biopsy or Sentinel Lymph Node Biopsy\t15\t15\t15\t10"
		mydata = newfile.split("\n")
		opioidString = opioids.split("\t")
		for line in mydata:
			cell = line.split("\t")
			if cell[0].strip().upper() == singleRecord.procedure.strip().upper():
				for med in opioidString:	
					if med.strip().upper() == singleRecord.medication.strip().upper():
						#print med
						return cell[0] + med

		#create another file and create button to click here
		#return "http://disposemymeds.org/medicine-disposal-locator/"
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

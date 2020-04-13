import requests #For loading files from the internet

#Logging tool
import logging
logging.basicConfig(filename='covid19_reports_JSON_location.log',level=logging.DEBUG)
logging.info('Start program')

#Configuration variables
from setup import *

import csv
import json

covid19Reports_dict = {}
csvFile_path = "rivm_corona_in_nl.csv"

#Load reported covid19 cases from git repository.
covid19Reports_request = requests.get(covid19_reports_load_url(), allow_redirects=True)
#Save the CSV-file locally.
open(csvFile_path, 'wb').write(covid19Reports_request.content)

#Open the file as CSV file.
with open(csvFile_path) as csvFile:
	csvReader = csv.DictReader(csvFile)

	#Load every row into the dictonary
	for rows in csvReader:
		datum = rows['Datum']
		gemeenteCode = rows['Gemeentecode']
		aantal = rows['Aantal']

		if (not datum in covid19Reports_dict):
			covid19Reports_dict[datum] = {}
		covid19Reports_dict[datum][gemeenteCode] = aantal

#Write the data to a JSON-file
with open(covid19_reports_save_location(), 'w') as jsonFile:
	jsonFile.write(json.dumps(covid19Reports_dict)) #use indent=4 for pretty-print.

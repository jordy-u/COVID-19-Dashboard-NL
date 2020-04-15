'use strict';

const fs = require('fs');

//File locations
let file_old = 'input_data/city_names.old.json';
let file_new = 'output_data/city_names.json';

let rawdata = fs.readFileSync(file_old);

let cityNamesDataOld = JSON.parse(rawdata);

//Save all data in this object (dictonary)
var cityNamesData = {};

for (var dataEntryId in cityNamesDataOld) {
	//dataEntryId is a number. dataEntry is the JSON-inner-object assosiated with that ID.
	var dataEntry = cityNamesDataOld[dataEntryId];

    // skip cities without hospitalisation count.
	//These cities are not represented in the map, so it doesn't matter that they're not in the data-file. They are probably part of a larger region.
    if (dataEntry["Gemeentecode"] == -1) continue;
	
	cityNamesData[dataEntry["Gemeentecode"]] = dataEntry["Gemeentenaam"]
}

// Write data to JSON-file 
fs.writeFile(file_new, JSON.stringify(cityNamesData), (err) => { 
      
    // In case of a error throw err. 
    if (err) throw err;
	else console.log("Data written to: " + file_new);
}) 


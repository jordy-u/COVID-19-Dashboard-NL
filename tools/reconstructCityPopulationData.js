//Problem: The CBS (Centraal Bureau voor Statistieken) shares information about the number op people that live in every city. The data in this file has a wrong format and has too much data.
//Solution: This script reads the data from the CBS-JSON-file and writes the relevant data to a new JSON-file, with the correct syntax.

'use strict';

const fs = require('fs');

//File locations
let file_old = 'input_data/population_per_city_old.json';
let file_new = 'output_data/population_per_city.json';

let rawdata = fs.readFileSync(file_old);

//When the file is loaded into a buffer, a weird character is added to the front.
//I bet there is a better way to read the buffer, but it already took me long.
//This line removes the first character.
let rawDataWithoutFirstCharacter = rawdata.toString().substr(1);

let map = JSON.parse(rawDataWithoutFirstCharacter);

//Save all data in this object (dictonary)
var cityPopulationData = {};

/*Create a new JSON-object in the way we want it:
{
	"CITY_ID" : CITY_POPULATION,
	"CITY_ID" : CITY_POPULATION,
	...
}
*/
for (var city in map.value) {
    // skip cities without puplation count.
	//These cities are not represented in the map, so it doesn't matter that they're not in the data-file. They are probably part of a larger region.
    if (map.value[city]["BevolkingAanHetEindeVanDePeriode_15"] == null) continue;
	
	//Remove the "GM" part of a city ID:
	//Example: "GM0048" --> "0048"
	var cityIdString = map.value[city]["RegioS"].substr(2);
	
	//Parse the value to an int to get rid of the prefix zero's:
	//Example: "0048" --> 48
	var cityIdInt = parseInt(cityIdString);
	cityPopulationData[cityIdInt] = map.value[city]['BevolkingAanHetEindeVanDePeriode_15'];
}

// Write data to JSON-file 
fs.writeFile(file_new, JSON.stringify(cityPopulationData), (err) => { 
      
    // In case of a error throw err. 
    if (err) throw err;
	else console.log("Data written to: " + file_new);
}) 


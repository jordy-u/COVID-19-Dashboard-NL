//This script generates polygons for a SVG-file from a geoJson-file.
//This is needed to create a map of the Netherlands for the site.

'use strict';

const fs = require('fs');

//File locations
let file_old = 'input_data/gemeente-2019.geojson';
let file_new = 'output_data/mapNL.svg-part';

let rawdata = fs.readFileSync(file_old);
let map = JSON.parse(rawdata);
//console.log(map.features[0].geometry.coordinates[0][0]);

let maxRegions = -1;
var i = 0;
var region, coordinate;
var svgOutputString = "";

//The values below can be used to calculate the size of the SVG.
//They are not used, because the size doesn't change.
var lowestX = 9999999;
var lowestY = 9999999;
var highestX = 0;
var highestY = 0;

for (region of map.features) {
	//console.log(region.properties.Gemnr + "\n");
	
	//Example of a polygon: <polygon fill="red"  points="564746,1516794 563854,1517000 562425,1516663"/>
	svgOutputString += '<polygon id="' + region.properties.Gemnr + '" fill="green" stroke="black" stroke-width="400" points="';
	
	//All values are very far from offset 0. So all X and Y values are substracted with a constant.
	for (coordinate of region.geometry.coordinates[0][0]) {
		svgOutputString += ' ' + (coordinate[0]-343187) + ',' + (301441-(coordinate[1]-1233554));
	}
	svgOutputString += '"/>\n';
	
	//To calculate actual size. Commented out because the size doesn't change
	//if (lowestX > coordinate[0]) lowestX = coordinate[0];
	//if (lowestY > coordinate[1]) lowestY = coordinate[1];
	//if (highestX < coordinate[0]) highestX = coordinate[0];
	//if (highestY < coordinate[1]) highestY = coordinate[1];
	
	i++;
	if (i == maxRegions) break;
}

//console.log("lowestX: " + lowestX);
//console.log("lowestY: " + lowestY);
//console.log("highestX: " + highestX);
//console.log("highestY: " + highestY);
//
//console.log("verschil X: " + (highestX - lowestX));
//console.log("verschil Y: " + (highestY - lowestY));


// Write data to SVG.part-file 
fs.writeFile(file_new, svgOutputString, (err) => { 
      
    // In case of a error throw err. 
    if (err) throw err;
	else console.log("Data written to: " + file_new);
}) 

//There colors are used for the legend: reported covid-19 cases
var legendColorsCovid19Reports = [
	"#FFFFFF",
	"#FFFFD4",
	"#FEE391",
	"#FEC44F",
	"#FE9929",
	"#D95F0E",
	"#993404"
];

//There colors are used for the legend: reported covid-19 cases
var legendColorsHospitalisation = [
	"#FFFFFF",
	"#FFFFCC",
	"#C7E9B4",
	"#7FCDBB",
	"#41B6C4",
	"#2C7FB8",
	"#253494"
];

var legendColorsCurrentDataset = null;

//To check which color should be used for a city with a specific amount of cases.
//TODO: These values should not be hardcored and change for every dataset and presentation option.
var legendColorRanges = [1, 25, 40, 65, 95, 160, 310];

var legendColorBoxes = [];
var legendValues = [];

$(document).ready(function(){
	//Define legendColorBoxes-array
	for (i = 0; i <= 6; i++) {
		legendColorBoxes[i] = $("#legendColor" + i)[0];
		legendValues[i] = $("#legendValue" + i)[0];
	}
	
	updateLegendColors("covid19Reports");
});

//Change legend colors.
//Options: dataset = covid19Reports, hospitalisation
function updateLegendColors(dataset) {
	if (dataset == "covid19Reports") legendColorsCurrentDataset = legendColorsCovid19Reports;
	else if (dataset == "hospitalisation") legendColorsCurrentDataset = legendColorsHospitalisation;
	//Show an error if the dataset is not implemented
	else {
		$("#errorAlert").html($("#errorAlert").html() + '<div class="alert alert-danger" role="alert"><strong>Error: </strong>Selected dataset does not exist.</div>');
		return;
	}
	
	//Change colors
	for (i = 0; i <= 6; i++) {
		$("rect", legendColorBoxes[i])[0].setAttribute("style", "fill: " + legendColorsCurrentDataset[i])
	}
	//Change legend values
	for (i = 1; i <= 6; i++) {
		legendValues[i].innerHTML = legendColorRanges[i-1] + " - " + legendColorRanges[i];
	}
	
	//Reset the selected city
	$("#legendCityName").html("Selecteer een stad");
	$("#legendCityTotal").html("-");
	$("#legendCityRelative").html("-");
	
}

//Returns a hex-color as a string. Ex: "#41B6C4".
function getLegendColor(numberOfCases) {
	for (i = 0; i < 6; i++) {
		if (numberOfCases < legendColorRanges[i]) return legendColorsCurrentDataset[i];
	}
	return legendColorsCurrentDataset[6];
}

//Update the legend when the user hovers over a city
function updateLegend(cityName, cityPopulation, cityCasesTotal, cityCasesRelative) {
	$("#legendCityName").html(cityName);
	$("#legendCityTotal").html(cityCasesTotal);
	$("#legendCityRelative").html(cityCasesRelative);
}
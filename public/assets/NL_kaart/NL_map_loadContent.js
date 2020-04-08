//Save the reports here.
var covid19Reports = null;
var populationPerCity = null;

//Fill the map with data of today.
function covid19Reports_Process() {
	var amountOfDays = Object.keys(covid19Reports).length;
	
	//Determine last day
	var newestMapDate = new Date("2020-02-27");
	newestMapDate.setDate(newestMapDate.getDate() + amountOfDays - 1);
	
	//Update the map
	updateMap(newestMapDate);
	
	//Set max value of slider
	$("#country-map-slider")[0].setAttribute("max", amountOfDays-1)
	$("#country-map-slider")[0].setAttribute("value", amountOfDays-1)
	
	//Place slider label above the holder (at the end).
	rangeV.style.setProperty("left", "calc(100% + -10px)")
	//Convert the selected date to "dd month"
	const month = newestMapDate.toLocaleString('default', { month: 'long' });
	var dateString = newestMapDate.getDate().toString() + ' ' + month
	rangeV.innerHTML = '<span id="current-date">' + dateString + '</span>';
}

//Update the map with the date in dateString as described in the loaded JSON-file.
//Example: "2020-04-02"
function updateMap(date) {
	var dateString = date.toISOString().substr(0,10)
	var dataSelectedDay = covid19Reports[dateString];
	$( ".st0", $("#gemeentes")[0] ).each(function() {
		reportedCases = (dataSelectedDay[this.id] != null)? dataSelectedDay[this.id] : 0;
		color = reportedCases/571.0*255;
		this.setAttribute("style", "fill: rgb(255," + (255-color) + "," + (255-color) + ")");
	});
}

var request_covid19Reports = {
	data: "",
	url: "/assets/NL_kaart/covid19_reports_every_day.json",
	errorMessage: "Het laden van het aantal covid-19 meldingen is mislukt. Probeer het later nog eens."
};

var request_populationPerCity = {
	data: "",
	url: "/assets/NL_kaart/population_per_city.json",
	errorMessage: "Het laden van aantal inwoners per gemeente is mislukt. Probeer het later nog eens."
};

$(document).ready(function(){
	//Load reported covid-19 cases
	dataLoading_createRequest(request_covid19Reports);
	
	//Load population per city
	dataLoading_createRequest(request_populationPerCity);
});

/*Create a HTTP-request. The requests which are needed are:
* request_covid19Reports:		amount of covid19Reports
* request_populationPerCity: 	City population
*/
function dataLoading_createRequest(request_parameters) {
	console.log("dataLoading_createRequest");
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function () { dataLoading_onreadystatechange(this, request_parameters); };
	xmlhttp.open("GET", request_parameters.url, true);
	xmlhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
	xmlhttp.send();
}

//When the JSON-data is loaded, it is saved in a variable.
//When all data is loaded, covid19Reports_Process() will run.
var dataLoading_numberOfFilesLoaded = 0;
function dataLoading_onreadystatechange(this_request, request_parameters) {
	
	if (this_request.readyState == 4) {
		//Request = OK
		console.log("Request = OK");
		if (this_request.status == 200) {
			request_parameters.data = JSON.parse(this_request.responseText);
			
			// Check if both files are loaded
			dataLoading_numberOfFilesLoaded++;
			if (dataLoading_numberOfFilesLoaded == 2)
				covid19Reports_Process(); 
		}
		//Request is NOT OK
		if (this_request.status != 200) {
			$("#errorAlert").html($("#errorAlert").html() + '<div class="alert alert-danger" role="alert"><strong>Error: </strong>' + request.errorMessage + '</div>');
		}
	}
}

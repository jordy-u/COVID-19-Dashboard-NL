//Save the reports here.
var populationPerCity = null;
var selectedDate = null;
var selectedDataset = null;
var lastSelectedCity = null;

//Datasets
var request_covid19Reports = {
	data: null,
	startDate: "2020-02-27T03:00:00+0000",
	url: "/assets/NL_kaart/covid19_reports_every_day.json",
	errorMessage: "Het laden van het aantal covid-19 meldingen is mislukt. Probeer het later nog eens."
};

var request_populationPerCity = {
	data: null,
	url: "/assets/NL_kaart/population_per_city.json",
	errorMessage: "Het laden van aantal inwoners per gemeente is mislukt. Probeer het later nog eens."
};

var request_hospitalizationPerCity = {
	data: null,
	startDate: "2020-03-31T03:00:00+0000",
	url: "/assets/NL_kaart/covid19_hospitalizations.json",
	errorMessage: "Het laden van aantal ziekenhuisopnamens per gemeente is mislukt. Probeer het later nog eens."
};

var request_cityNames = {
	data: null,
	url: "/assets/NL_kaart/city_names.json",
	errorMessage: "Het laden van de gemeentenamen. Probeer het later nog eens."
};

//Fill the map with data of today.
function covid19Reports_Process(dataSet) {
	
	//TODO: This value should not be hardcoded
	var amountOfDays = 48
	if (dataSet.startDate == "2020-03-31T03:00:00+0000") amountOfDays = 15;
	
	selectedDataset = dataSet;
	
	//Determine last day
	//var newestMapDate = new Date(dataSet.startDate);
	var newestMapDate = new Date("2020-02-27T05:00:00.000Z");
	newestMapDate.setDate(newestMapDate.getDate() + amountOfDays - 1);
	
	//Update the map
	updateMap(newestMapDate);
	
	//Set max value of slider
	$("#country-map-slider")[0].setAttribute("max", amountOfDays-1)
	$("#country-map-slider")[0].setAttribute("value", amountOfDays-1)
	
	//Place slider label above the holder (at the end).
	rangeV.style.setProperty("left", "calc(100% + -10px)")
	
	//Convert the selected date to "dd month"
	var dateString = getDayAndMonth(newestMapDate)
	rangeV.innerHTML = '<span id="current-date">' + dateString + '</span>';
	
	//Change slide to last day
	range.value = range.max
	
	$('path, g', $("#NL_map_svg")).mouseover(function(event) {
		selectCity(this);
	});
}

//When you mouse-over a city, it will be highlighted.
//The city information is shown in the SVG map.
function selectCity(city) {
	//This is when the map is loaden and no city is selected.
	if (city == null) return;
	
	//Don't do anything for regions which don't have data. Those are member of a larger region with data.
	if (request_populationPerCity.data[city.id] == null) return;
	
	date = selectedDate.toISOString().substr(0,10);
	cityId = city.id;
	
	var cityName = request_cityNames.data[city.id];
	var cityPopulation = (request_populationPerCity.data[city.id] != null)? request_populationPerCity.data[city.id] : 1;
	
	var cityCasesTotal = 0;
	if (request_covid19Reports.data[date] != null)
		if (request_covid19Reports.data[date][city.id] != null)
			cityCasesTotal = request_covid19Reports.data[date][city.id];
	
	var cityCasesRelative = (cityPopulation / cityCasesTotal).toFixed(0);

	updateLegend(cityName, cityPopulation, cityCasesTotal, cityCasesRelative);
	
	if (lastSelectedCity != null)
		$(lastSelectedCity).removeClass("selectedCity");
	
	$(city).addClass("selectedCity");
	lastSelectedCity = city;
}

var dataSelectedDay; //debug

//Update the map with the specified date. If no date is specified, the last selected date is used.
function updateMap(date) {
	if (date == undefined) date = selectedDate
	else selectedDate = date;

	var dateString = date.toISOString().substr(0,10)

	/*var*/ dataSelectedDay = selectedDataset.data[dateString];
	$( ".st0", $("#gemeentes")[0] ).each(function() {
		reportedCases = 0;
		if (dataSelectedDay != null) {
			if (dataSelectedDay[this.id] != null)
				reportedCases = dataSelectedDay[this.id];
		}
		if ($("#presentation_normalisation")[0].value == "normalised") {
			cityPopulation = (request_populationPerCity.data[this.id] != null)? request_populationPerCity.data[this.id] : 1;
			reportedCases = reportedCases/cityPopulation * 100000.0
		}

		this.setAttribute("style", "fill: " + getLegendColor(reportedCases));
	});
	
	selectCity(lastSelectedCity)
	
	noDataWarning = $("#date-has-no-data", $("#dataWarning")[0])[0];
	if (dataSelectedDay == null) {
		if (noDataWarning == null)
			$("#dataWarning").html($("#dataWarning").html() + '<div class="alert alert-warning" id="date-has-no-data" role="alert"><strong>Geen data: </strong>Er is nog geen data beschikbaar voor periode 31 maart t/m 8 april.</div>');
	} else {
		if (noDataWarning != null && noDataWarning != null) noDataWarning.remove();
	}
}

$(document).ready(function(){
	//Load reported covid-19 cases
	dataLoading_createRequest(request_covid19Reports);
	
	//Load population per city
	dataLoading_createRequest(request_populationPerCity);
	
	//Load hospitalization numbers 
	dataLoading_createRequest(request_hospitalizationPerCity);
	
	//Load names of every city
	dataLoading_createRequest(request_cityNames);
	
	//When the selected dataset changes:
	$( "#presentation_catagory" ).change(function() {
		if (this.value == "covid19ReportedCases") {
			updateLegendColors("covid19Reports");
			covid19Reports_Process(request_covid19Reports);
		}
		else if (this.value == "hospitalizationCases") {
			updateLegendColors("hospitalisation");
			covid19Reports_Process(request_hospitalizationPerCity);
			
			//Remove the error about not existing data of the other dataset.
			noDataWarning = $("#date-has-no-data", $("#dataWarning")[0])[0];
			if (noDataWarning != null && noDataWarning != null) noDataWarning.remove();
		}
	});
});

/*Create a HTTP-request. The requests which are needed are:
* request_covid19Reports:			Amount of covid19Reports
* request_populationPerCity: 		City population
* request_hospitalizationPerCity	Amount of hospitalisations per city
* request_cityNames					For combining cityId's to cityNames.
*/
function dataLoading_createRequest(request_parameters) {
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
		if (this_request.status == 200) {
			request_parameters.data = JSON.parse(this_request.responseText);
			
			// Check if both files are loaded
			dataLoading_numberOfFilesLoaded++;
			if (dataLoading_numberOfFilesLoaded == 4)
				covid19Reports_Process(request_covid19Reports); 
		}
		//Request is NOT OK
		if (this_request.status != 200) {
			$("#errorAlert").html($("#errorAlert").html() + '<div class="alert alert-danger" role="alert"><strong>Error: </strong>' + request.errorMessage + '</div>');
		}
	}
}


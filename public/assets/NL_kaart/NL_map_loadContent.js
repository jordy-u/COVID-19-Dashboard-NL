//Save the reports here.
var covid19Reports = null;

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
$(document).ready(function(){
	//Load map-information
	{
		var xmlhttp = new XMLHttpRequest();
		var url = "/assets/NL_kaart/covid19_reports_every_day.json";

		xmlhttp.onreadystatechange = function() {
			if (this.readyState == 4) {
				//Request = OK
				if (this.status == 200) {
					covid19Reports = JSON.parse(this.responseText);
					covid19Reports_Process(); 
				}
				//Request is NOT OK
				if (this.status != 200) {
					$("#errorAlert").html('<div class="alert alert-danger" role="alert"><strong>Error: </strong>Het laden van de data is niet gelukt. Probeer het later nog eens.</div>');
				}
			}
		};
		xmlhttp.open("GET", url, true);
		xmlhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
		xmlhttp.send();
	}  
});

<script type="text/javascript" src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.7.1.min.js"></script>
<link rel="stylesheet" href="/assets/NL_kaart/rangeStyle.css">
<script type="text/javascript">

//Save the reports here.
var covid19Reports = null;

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

//Fill the map with data of today.
function covid19Reports_Process() {
	var amountOfDays = Object.keys(covid19Reports).length;
	
	//Determine last day
	var newestMapDate = new Date("2020-02-27");
	newestMapDate.setDate(newestMapDate.getDate() + amountOfDays - 1);
	
	//Set max value of slider
	$("#country-map-slider")[0].setAttribute("max", amountOfDays-1)
	$("#country-map-slider")[0].setAttribute("value", amountOfDays-1)
}

//Update the map with the date in dateString as described in the loaded JSON-file.
//Example: "2020-04-02"
function updateMap(date) {
	var dateString = date.toISOString().substr(0,10)
	var dataSelectedDay = covid19Reports[dateString];
	console.log("test1");
	$( ".st0", $("#gemeentes")[0] ).each(function() {
		color = dataSelectedDay[this.id]/571.0*255;
		this.setAttribute("style", "fill: rgb(255," + (255-color) + "," + (255-color) + ")");
	});
}
</script>

<div id="errorAlert"></div>

<!-- Map of the Netherlands -->
<?php include('assets/NL_kaart/mapNL.svg'); ?>

<!-- slider -->
<div class="range-wrap mt-3 mx-4">
	<div class="range-value" id="rangeV"></div>
	<input id="country-map-slider" type="range" min="0" max="35" value="0" step="1" >
</div>

<!-- Script to use the slider -->
<script>
//https://codepen.io/onyx1812/pen/GRJxmva
const
	range = document.getElementById('country-map-slider'),
	rangeV = document.getElementById('rangeV'),
	setValue = ()=>{
		var mapDate = new Date("2020-02-27");
		var daysLater = parseInt(range.value);
		mapDate.setDate(mapDate.getDate() + daysLater);
		updateMap(mapDate)
		const month = mapDate.toLocaleString('default', { month: 'long' });
		
		var dateString = mapDate.getDate().toString() + ' ' + month
		const
			newValue = Number( (range.value - range.min) * 100 / (range.max - range.min) ),
			newPosition = 10 - (newValue * 0.2);
		rangeV.innerHTML = `<span id="current-date">${dateString}</span>`;
		rangeV.style.left = `calc(${newValue}% + (${newPosition}px))`;
	};
document.addEventListener("DOMContentLoaded", setValue);
range.addEventListener('input', setValue);
</script>

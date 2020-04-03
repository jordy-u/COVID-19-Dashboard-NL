<script type="text/javascript" src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.7.1.min.js"></script>
<script type="text/javascript">
//Include jQuery if it's not defined.
//if(typeof jQuery == 'undefined'){
//	document.write(
//	'<script type="text/javascript" src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.7.1.min.js"></'+'script>'
//	);
//}

//Save the reports here.
var covid19Reports = null;

//With these checks the map-data can be loaded before the rest is loaded.
//When the JSON-file is downloaden AND the document is 'ready', the SVG-map can be configured.
//This script is a bit weird constructed, because all functions/connections are asynchronous.
var covid19Reports_LoadingCompleted = false;
var document_Ready = false;
var covid19Reports_Processing = false;

//Load map-information
{
	var xmlhttp = new XMLHttpRequest();
	var url = "/assets/covid19_reports_every_day.json";

	xmlhttp.onreadystatechange = function() {
		if (this.readyState == 4) {
			if (this.status == 200) {
				covid19Reports = JSON.parse(this.responseText);
				
				//Load covid19Reports into map if the document is ready.
				covid19Reports_LoadingCompleted = true;
				if (document_Ready)
					covid19Reports_Process();
			}
			if (this.status == 400) {
				alert("Error: Can't load covid19-data.");
			}
		}
	};
	xmlhttp.open("GET", url, true);
	xmlhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
	xmlhttp.send();
}

//Document is ready
$(document).ready(function(){
	document_Ready = true;
	//Load covid19Reports into map if the JSON-file is loaded.
	if (covid19Reports_LoadingCompleted)
		covid19Reports_Process();
});

//Fill the map with data of today.
function covid19Reports_Process() {
	if (covid19Reports_Processing) return;
	covid19Reports_Processing = true;
	updateMap("2020-03-30");
}

//Voor DEBUGGING
var dataSelectedDay

//Update the map with the date in dateString as described in the loaded JSON-file.
//Example: "2020-04-02"
function updateMap(dateString) {
	dataSelectedDay = covid19Reports[dateString];
	
	$( "polygon", $("#mapNL")[0] ).each(function() {
		color = dataSelectedDay[this.id]/571.0*255;
		this.setAttribute("fill", "rgb(255," + (255-color) + "," + (255-color) + ")");
	});
}
</script>

<svg class="img-fluid" id="mapNL" style="max-height: 70vh" viewBox="-23000 -10000 270000 315000">
	<?php
		include('assets/mapNL.svg-part');
	?>
	Sorry, your browser does not support inline SVG.
</svg>

<script>
$(document).ready(function(){
    $('[data-toggle="popover"]').popover();   
});
</script>

<!--<img id="meldingenNLMap" class="img-fluid mx-auto d-block" style="max-height: 80vh" src="images/meldingenNL/meldingenNL0.png">-->



<div class="custom-control custom-radio mt-3">
	<p>Selecteer datum</p>
	<input type="range" min="0" max="35" value="0" id="country-map-slider" class="custom-range">
</div>

<script>
//Let the map update when the slider changes value.
var slider = document.getElementById("country-map-slider");
map = $('#meldingenNLMap')[0];
testShape = $('#3')[0];

slider.oninput = function() {
  //map.src = "images/meldingenNL/meldingenNL" + this.value + ".png";
  testShape.setAttribute("fill","rgb(" + this.value*5 + ",0,0)")
}
</script>

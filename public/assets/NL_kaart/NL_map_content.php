<script type="text/javascript" src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.7.1.min.js"></script>
<link rel="stylesheet" href="/assets/NL_kaart/rangeStyle.css">
<script type="text/javascript" src="assets/NL_kaart/NL_map_loadContent.js"></script>

<div id="errorAlert"></div>

<!-- Map of the Netherlands -->
<?php include('mapNL.svg'); ?>

<!-- slider -->
<div class="range-wrap mt-3 mx-4">
	<div class="range-value" id="rangeV"></div>
	<input class="custom-range" id="country-map-slider" type="range" min="0" max="35" value="0" step="1" >
</div>

<!-- Data representation options -->
<form class="form-inline">
	<label for="presentation_catagory" class="mr-sm-2">Gegevens:</label>
	<select id="presentation_catagory" class="custom-select mb-2 mr-sm-2">
		<option value="covid19ReportedCases" selected>Aantal covid-19 meldingen</option>
		<option value="hospitalizationCases">Aantal ziekenhuisopnamens</option>
	</select>
	
	<label for="presentation_normalisation" class="mr-sm-2">Data presentatie:</label>
	<select id="presentation_normalisation" class="custom-select mb-2 mr-sm-2" onChange="updateMap()">
		<option value="normalised" selected>Genormaliseerd</option>
		<option value="total">Totale aantallen</option>
	</select>
</form>
<br>

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
		
		//Don't update the map if the reports are not downloaded yet (when this webpage is loaded).
		if (request_covid19Reports.data)
			updateMap(mapDate)
		
		//Convert the selected date to "dd month"
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

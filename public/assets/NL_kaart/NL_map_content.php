<script type="text/javascript" src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.7.1.min.js"></script>
<link rel="stylesheet" href="/assets/NL_kaart/rangeStyle.css">
<script type="text/javascript" src="/assets/NL_kaart/NL_map_checkValidityOfDatasets.js"></script>
<script type="text/javascript" src="/assets/NL_kaart/NL_map_loadContent.js"></script>
<script type="text/javascript" src="/assets/NL_kaart/NL_map_legend.js"></script>
<script type="text/javascript" src="/assets/dateFunctions.js"></script>

<div id="errorAlert"></div>

<!-- Map of the Netherlands -->
<?php include('mapNL.svg'); ?>

<!-- slider -->
<div class="range-wrap mt-3 mx-4">
	<div class="range-value" id="rangeV"></div>
	<input class="custom-range" id="country-map-slider" type="range" step="1" >
</div>

<div id="dataWarning"></div>

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
<script type="text/javascript" src="/assets/NL_kaart/NL_map_slider.js"></script>

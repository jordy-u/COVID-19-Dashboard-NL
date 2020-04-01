<script type="text/javascript">
//Include jQuery if it's not defined.
if(typeof jQuery == 'undefined'){
	document.write(
	'<script type="text/javascript" src="http://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.7.1.min.js"></'+'script>'
	);
}
</script>

<img id="meldingenNLMap" class="img-fluid mx-auto d-block" style="max-height: 80vh" src="images/meldingenNL/meldingenNL0.png">

<div class="custom-control custom-radio mt-3">
	<p>Selecteer datum</p>
	<input type="range" min="0" max="35" value="0" id="country-map-slider" class="custom-range">
</div>

<script>
//Let the map update when the slider changes value.
var slider = document.getElementById("country-map-slider");
map = $('#meldingenNLMap')[0];

slider.oninput = function() {
  map.src = "images/meldingenNL/meldingenNL" + this.value + ".png";
}
</script>

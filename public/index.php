<?php include_once('assets/config.php'); ?>
<html>
	<?php include_once('assets/head.php'); ?>
<body>

<div class="jumbotron text-center">
  <h1>COVID-19 Dashboard voor Nederland</h1>
  <p>Kijk terug in de tijd en zie hoe het coronavirus zich heeft versprijd in Nedeland.</p> 
</div>

<div class="container">
	<!-- map Netherlands -->
	<div class="row">
		<div class="col-lg-8">
			<?php include('assets/NL_kaart/NL_map_content.php'); ?>
			<br>
			<img src="images/placeholders/placeholder_city_stats.png" class="img-fluid">
		</div>
		<div class="col-lg-4">
			<img src="images/placeholders/placeholder_news.png" class="img-fluid">
		</div>
	</div>
	<!-- Stastistics -->
	<div class="row">
		<div class="col-md">
			<img src="images/placeholders/placeholder_graph_spreading.png" class="img-fluid">
		</div>
		<div class="col-md">
			<img src="images/placeholders/placeholder_graph_hospital_avail.png" class="img-fluid">
		</div>
	</div>
	<div class="row">
		<div class="col-md">
			<img src="images/placeholders/placeholder_city_map.png" class="img-fluid">
		</div>
		<div class="col-md">
			<img src="images/placeholders/placeholder_city_hospital_avail.png" class="img-fluid">
		</div>
	</div>
<p>
Dit is een site in aanbouw. Binnenkort is deze site een dashboard waar statistieken te vinden zijn over het coronavirus.<br><br>

<a href="info">Klik hier voor achtergrondinformatie over deze website.</a><br><br>

</p>
</div>
<?php include_once('assets/body_bottom.php'); ?>
</body>
</html>

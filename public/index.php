<?php include_once('assets/config.php'); ?>
<html>
<head>
<?php include_once('assets/og-data.php'); ?>
<!-- Required meta tags -->
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

<!-- Bootstrap CSS -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

<title>COVID-19 analyse tool</title>
</head>
<body>

<div class="jumbotron text-center">
  <h1>COVID-19 Dashboard voor Nederland</h1>
  <p>Kijk terug in de tijd en zie hoe het coronavirus zich heeft versprijd in Nedeland.</p> 
</div>

<div class="container">
	<!-- map Netherlands -->
	<div class="row">
		<div class="col-lg-8">
			<?php include('NL_map_content.php'); ?>
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
<!-- Optional JavaScript -->
<!-- jQuery first, then Popper.js, then Bootstrap JS -->
<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>
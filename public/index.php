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
		<div class="col">
			<?php include('assets/NL_kaart/NL_map_content.php'); ?>
			<br>
		</div>

	</div>

<p>
<a href="privacyverklaring">Privacyverklaring</a> | <a href="informatiebron">Informatiebron</a><br><br>

</p>
</div>
<?php include_once('assets/body_bottom.php'); ?>
</body>
</html>

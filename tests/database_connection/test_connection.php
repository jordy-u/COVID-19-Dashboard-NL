<?php
/*
This file is for testing the database connection. Steps:
1. Put this in the root-folder of your website documents to test the database connection. So in "/test_connection.php"
2. Fill in the right username, password and database(name = "test") into this file: "assets/database_login_credentials.php"
3. Go to the phpmyadmin page of your testing enviourment, create a database named "test" and import "test_connection_db.sql".
4. Open this file (test_connection.php) in your browser.
5. You should see the following result:

Output:
SQL test
Response:
getal: 1
timestamp: 2020-03-26 17:54:49
string: een

getal: 3
timestamp: 2020-03-26 17:54:50
string: drie

getal: 5
timestamp: 2020-03-26 17:54:50
string: vijf
*/


include_once('assets/config.php');
include_once('assets/connection.php');
?>

<html>
<head>
<title>COVID-19 analyse tool</title>
</head>
<body>
<h1>SQL test</h1>
<p>

<?php
$query = 'SELECT *
FROM `test`
WHERE `getal`=? OR `timestamp`=? OR `string`=?
ORDER BY `timestamp` ASC;';

$response = trySqlQuery($db, $query, [3, "2020-03-26 17:54:49", "vijf"]);

if (!$response->succes) echo 'SQL Error!'; //error
else {
	echo '<b>Response:</b><br>';
	while ($row = $response->data->fetch_assoc()) {
		echo 'getal: ' . $row['getal'] . '<br>timestamp: ' . $row['timestamp'] . '<br>string: ' . $row['string'] . '<br><br>';
	}
}
?>


</p>
</body>
</html>

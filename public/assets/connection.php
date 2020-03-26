<?php
include('assets/database_login_credentials.php');

//Setup database-connection object
$db = new mysqli(SQLSETTING['server'], SQLSETTING['user'], SQLSETTING['pass'], SQLSETTING['db']);
if($db->connect_errno > 0){
    die('Unable to connect to database [' . $db->connect_error . ']');
}

/*return mysqli_result
Parameters:
* db				mysqli-connection object (see variable above)
* query				SQL-query. Example: 'SELECT `columnA` FROM `table` WHERE `columnB`=? AND `columnC`=?'
* parameterArray	Parameters to be filled in instead of the question marks(?). Example: ['foo', 7]

Note that every variable that can be manipulated by a user should be filled in into the parameterArray.
Escape sequences will be applied to those variables to prevent SQL injection.
*/
function trySqlQuery($db, $query, $parameterArray) {
	$returnValues = new \stdClass();
	$returnValues->succes = false;
	$parameterTypes = str_repeat("s", count($parameterArray)); //Create a string with a "s" for every parameter.
	
	
	$stmt = $db->prepare($query);
	if ($stmt == false) { echo "1: Prepare failed: (" . $db->errno . ") " . $db->error; return $returnValues;}
	
	if (count($parameterArray) > 0) {
	$stmt->bind_param($parameterTypes, ...$parameterArray);
	if ($stmt == false) { echo "2: Prepare failed: (" . $db->errno . ") " . $db->error; return $returnValues;}
	}
	
	$stmt->execute();
	if ($stmt == false) { echo "3: Prepare failed: (" . $db->errno . ") " . $db->error; return $returnValues;}
	
	$returnValues->succes = true;
	$returnValues->data = $stmt->get_result();
	return $returnValues;
}
?>

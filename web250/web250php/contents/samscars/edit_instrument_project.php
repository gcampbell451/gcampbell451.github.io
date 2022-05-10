<html>
<head>
<title>Instrument Saved</title>
<link rel = "stylesheet" type = "text/css" href = "styles/default.css" />
</head>

<div class="brand_box">
<?php
// Capture the values posted to this php program from the text fields in the form

$ID = $_REQUEST['ID'] ;
$Brand = $_REQUEST['Brand'] ;
$Model = $_REQUEST['Model'] ;
$Price = $_REQUEST['Asking_Price'] ;

//Build a SQL Query using the values from above

$query = "UPDATE inventory SET 

VIN='$VIN', 
Brand='$Brand', 
Model='$Model', 
ASKING_PRICE='$Price'

WHERE

ID='$ID'"; 

// Print the query to the browser so you can see it
echo ($query. "<br>");

include 'db.php';
/* check connection */
if (mysqli_connect_errno()) {
 echo ("Connection failed: ". $mysqli->error."<br>");
 exit();
}

 echo 'Connected successfully to mySQL. <BR>';

//select a database to work with
$mysqli->select_db("Cars");
 Echo ("Selected the Cars database. <br>");

/* Try to insert the new car into the database */
if ($result = $mysqli->query($query)) {
 echo "<p>You have successfully entered $Brand $Model into the database.</p>";
}
else
{
 echo "Error entering $ID into database: " . mysql_error()."<br>";
}
$mysqli->close();
?>
<p><a href="view_instruments_project.php">View Inventory</a></p>
</div>
</body>
</html>
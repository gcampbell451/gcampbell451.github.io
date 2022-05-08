<html>
<head>
<title>Car Deleted</title>
<link rel = "stylesheet" type = "text/css" href = "styles/default.css" />
</head>
<body>
<div class="brand_box">
<h1 class="center">Sam's Used Cars</h1>
<?php 
include 'db.php';
$vin = $_GET['VIN'];
$query = "DELETE FROM inventory WHERE VIN='$vin'";
echo "$query <br>";
/* Try to query the database */
if ($result = $mysqli->query($query)) {
   echo "The vehicle with VIN $vin has been deleted.";
}
else
{
    echo "Sorry, a vehicle with VIN of $vin cannot be found " . mysql_error()."<br>";
}

$mysqli->close();


 include 'footer.php'
?>
</body>
</div>
</html>

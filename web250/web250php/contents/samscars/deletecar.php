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
$query = "DELETE FROM INVENTORY WHERE VIN='$vin'";
echo "$query <BR>";
/* Try to query the database */
if ($result = $mysqli->query($query)) {
   Echo "The vehicle with VIN $vin has been deleted.";
}
else
{
    echo "Sorry, a vehicle with VIN of $vin cannot be found " . mysql_error()."<br>";
}

$mysqli->close();
   

 echo "<br><br><a href='http://localhost/web250/index.php?p=contents/samscars/samsusedcars.html'>Sam's Used Cars Home</a>";

?>
</body>
</div>
</html>

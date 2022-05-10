<html>
<head>
<title>Axes, Et Cetera | View Instruments</title>
<link rel = "stylesheet" type = "text/css" href = "styles/default.css" />
</head>

<body>

<h1 class="center">Axes, Et Cetera</h1>
<div class="brand_box">
<?php include 'db.php';
$ID = $_GET['ID'];
$query = "SELECT * FROM instruments WHERE ID='$ID'";
/* Try to query the database */
if ($result = $mysqli->query($query)) {
   // Don't do anything if successful.
}
else
{
    echo "Sorry, an instrument with ID of $ID cannot be found " . mysql_error()."<br>";
}

// Loop through all the rows returned by the query, creating a table row for each
while ($result_ar = mysqli_fetch_assoc($result)) {
    $instrument = $result_ar['Instrument'];
	$brand = $result_ar['Brand'];
    $model = $result_ar['Model'];
    $price = $result_ar['Asking_Price'];
}
echo "$instrument $brand $model </p>";
echo "<p>Asking Price: $price </p>";

$mysqli->close();
   
?>
</div>
</body>

</html>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Instrument Entry Form</title>
<link rel = "stylesheet" type = "text/css" href = "styles/default.css" />
</head>
<body>
<h1 class="center">Axes, Et Cetera | Edit Instrument</h1>
<div class="brand_box">
<?php
include 'db.php';
$ID = $_GET['ID'];
$query = "SELECT * FROM instruments WHERE ID='$ID'";
/* Try to query the database */
if ($result = $mysqli->query($query)) {
 // echo "<p>Got the info</p>"; // Don't do anything if successful.
}
else
{
 echo "Sorry, an instrument with ID of $ID cannot be found " .  $mysqli->error."<br>";
}
// Loop through all the rows returned by the query, creating a table row for each
while ($result_ar = mysqli_fetch_assoc($result)) {
 $ID = $result_ar['ID'];
 $instrument = $result_ar['Instrument'];
 $brand = $result_ar['Brand'];
 $model = $result_ar['Model'];
 $price = $result_ar['Asking_Price'];
}
echo "$ID </p>";
//echo "$year $make $model </p>";
//echo "<p>Asking Price: $price </p>";
//echo "<p>Exterior Color: $color </p>";
//echo "<p>Interior Color: $interior </p>";

$mysqli->close();
?>

<form action="edit_instrument_project.php"
method=”post”>
<input name="ID" type="hidden" value= "<?php echo "$ID" ?>" /><br />
<br />
Brand: <input name="Brand" type="text" value= "<?php echo "$brand" ?>" /><br />
<br />
Model: <input name="Model" type="text" value= "<?php echo "$model" ?>" /><br />
<br />
Price: <input name="Asking_Price" type="text" value= "<?php echo "$price" ?>" /><br />
<br />
<input name="Submit1" type="submit" value="submit" /><br />
&nbsp;</form>
</div>
</body>
</html>
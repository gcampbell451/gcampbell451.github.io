<html>
<head>
<title>Instrument Deleted</title>
<link rel = "stylesheet" type = "text/css" href = "styles/default.css" />
</head>
<body>
<div class="brand_box">
<h1 class="center">Axes, Et Cetera | Delete Instrument</h1>
<?php 
include 'db.php';
$ID = $_GET['ID'];
$query = "DELETE FROM instruments WHERE ID='$ID'";
echo "$query <br>";
/* Try to query the database */
if ($result = $mysqli->query($query)) {
   echo "The instrument with ID $ID has been deleted.";
}
else
{
    echo "Sorry, an instruments with ID of $ID cannot be found " . mysql_error()."<br>";
}

$mysqli->close();



?>
<br><br>
<a href="https://www.tarheeltitles.com/web250/web250php/contents/samscars/view_instruments_project.php">View Inventory</a>
</div>
</body>

</html>

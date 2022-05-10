<html>
<head>
    <title>Instrument Saved</title>
    <link rel = "stylesheet" type = "text/css" href = "styles/default.css" />
</head>
<body >
<div class="brand_box">
<?php 
// Capture the values posted to this php program from the text fields

$ID =  trim( $_REQUEST['id']) ;
$Instrument = trim( $_REQUEST['instrument']) ;
$Brand = trim( $_REQUEST['brand']) ;
$Model = trim( $_REQUEST['model']) ;
$Price =  $_REQUEST['asking_price'] ;


//Build a SQL Query using the values from above

$query = "INSERT INTO instruments
  (ID, Instrument, Brand, Model, Asking_Price)
   VALUES (
   '$ID', 
   '$Instrument', 
   '$Brand',
   '$Model',
    $Price
    )";

// Print the query to the browser so you can see it
echo ($query. "<br>");

include 'db.php';

  echo 'Connected successfully to mySQL. <BR>'; 
  
//select a database to work with
$mysqli->select_db("Cars");
   Echo ("Selected the Cars database. <br>");

/* Try to insert the new car into the database */
if ($result = $mysqli->query($query)) {
    echo "<p>You have successfully entered $Brand $Model into the database.</P>";
}
else
{
    echo "Error entering $ID into database: " . $mysqli->error."<br>";
}
$mysqli->close();

?>
<a href="formEnterInstrument_project.htm">Back</a>
</div>
</body>
</html>
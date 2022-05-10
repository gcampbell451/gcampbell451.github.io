<html>
<head>
    <meta charset="utf-8">
    <title>Axes, Et Cetera | Inventory</title>
    <link rel = "stylesheet" type = "text/css" href = "styles/default.css" />
    <style>
  /* The grid is used to format a table instead of a grid control on the list of Notes */
#Grid
{
font-family:"Trebuchet MS", Arial, Helvetica, sans-serif;
width:80%;
border-collapse:collapse;
margin-left: auto;
margin-right: auto;
}
#Grid td, #Grid th 
{
font-size:1em;
border:1px solid #61ADD7;
padding:3px 7px 2px 7px;
}
#Grid th 
{
font-size:1.1em;
text-align:left;
padding-top:5px;
padding-bottom:4px;
background-color:#C2D9FE;
color: lightslategray;

}
#Grid tr.odd td 
{
color:#000000;
background-color: #F2F5A9;
}

#Grid tr.even  
{
color:#000000;
background-color: hsl(326, 14%, 90%);
}
#Grid head 
{
color: hsl(326, 14%, 90%);
background-color: hsl(149, 57%, 10%);
}
.auto-style1 {
	text-align: center;
}
</style>
 
</head> 
<body>
<h1 class="center">Axes, Et Cetera</h1>
<h3 class="center">Current Inventory</h3>
 <div class="auto-style1 brand_box">
 <?php
include 'db.php';
$query = "SELECT * FROM instruments";
/* Try to query the database */
if ($result = $mysqli->query($query)) {
   // Don't do anything if successful.
}
else
{
    echo "Error getting instruments from the database: " . mysql_error()."<br>";
}

// Create the table headers
echo "<table id='Grid' style='width: 80%'>\n";
echo "<tr>";
echo "<th style='width: 50px'>Make</th>";
echo "<th style='width: 50px'>Model</th>";
echo "<th style='width: 50px'>Asking Price</th>";
echo "<th style='width: 50px'>Action</th>";
echo "</tr>\n";

$class ="odd";  // Keep track of whether a row was even or odd, so we can style it later

// Loop through all the rows returned by the query, creating a table row for each
while ($result_ar = mysqli_fetch_assoc($result)) {
    echo "<tr class=\"$class\">";
    echo "<td><a href='view_instrument_project.php?ID=".$result_ar['ID']."'>" . $result_ar['Brand'] . "</a></td>";
    echo "<td>" . $result_ar['Model'] . "</td>";
       echo "<td>" . $result_ar['Asking_Price'] . "</td>";
        echo "<td><a href='form_edit_project.php?ID=".$result_ar['ID']."'>Edit</a>  <a href='delete_instrument_project.php?ID=".$result_ar['ID']."'>Delete</a></td>";
   echo "</tr>\n";
   
   // If the last row was even, make the next one odd and vice-versa
    if ($class=="odd"){
        $class="even";
    }
    else
    {
        $class="odd";
    }
}
echo "</table>";
$mysqli->close();

?>
<br><a href="https://www.tarheeltitles.com/web250/web250php/contents/samscars/formEnterInstrument_project.htm">Add Another Instrument</a>
<br><br><a href="https://www.tarheeltitles.com/web250/web250php/index.php?p=contents/samscars/view_instruments_project.php">Home</a>
</div>	 
 </body>
 
</html>
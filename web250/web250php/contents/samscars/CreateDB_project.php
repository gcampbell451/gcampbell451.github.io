<?php
/**
 * Joy of PHP sample code
 * Demonstrates how to create a database, create a table, and insert records.
 */

$mysqli = new mysqli('localhost', 'root', '' );


   if (!$mysqli) { 
      die('Could not connect'); 
  } 
  echo 'Connected successfully to mySQL. <BR>'; 
  

/* Create table doesn't return a resultset */
if ($mysqli->query("CREATE DATABASE Cars") === TRUE) {
    echo "<p>Database Cars created</P>";
}
else
{
    echo "Error creating Cars database: " . mysqli_connect_error()."<br>";
}
//select a database to work with
$mysqli->select_db("Cars");
   Echo ("Selected the Cars database");

$query = " CREATE TABLE instruments 
(ID varchar(17) PRIMARY KEY, Instrument varchar(20), Brand varchar(30), Model varchar(20), Asking_Price DECIMAL (10,2))";
echo "<p>***********</p>";
echo $query ;
echo "<p>***********</p>";
if ($mysqli->query($query) === TRUE) 
{
    echo "Database table 'instruments' created</P>";
}
else
{
    echo "<p>Error: </p>" . $mysqli->error;
}

$query = "INSERT INTO Cars.instruments 
(ID, Instrument, Brand, Model, Asking_Price) 
VALUES 
('axeman3000', 'guitar', 'Gibson', 'Les Paul', 12500);";


if ($mysqli->query($query) === TRUE) {
    echo "<p>Gibson Les Paul inserted into instruments table. </p>";
}
else
{
    echo "<p>Error inserting Gibson Les Paul: </p>" . $mysqli->error;
    echo "<p>***********</p>";
    echo $query ;
    echo "<p>***********</p>";
}

// Insert a Dodge Durango

$query = "INSERT INTO Cars.instruments
(ID, Instrument, Brand, Model, Asking_Price) 
VALUES 
('bobtheman','bass', 'Fender', 'Bassman', 4500);";


if ($mysqli->query($query) === TRUE) {
    echo "<p>Fender Bassman inserted into inventory table.</p>";
}
else
{
    echo "<p>Error Inserting Fender Bassman: </p>" . $mysqli->error;
    echo "<p>***********</p>";
    echo $query ;
    echo "<p>***********</p>";
}

// Insert 8 other cars
$query = "INSERT INTO Cars.instruments
(ID, Instrument, Brand, Model, Asking_Price) 
VALUES 
('sturules','drum kit', 'Pearl', 'Roadshow', 589);";




/**
('jennieslayer', 'guitar', 'Jackson', 'X Series Rhoads', 899),
('maxrebo', 'bass', 'Rickenbacker', '4000', 10999),
('sprucemcgoose', 'guitar', 'B.C. Rich', 'Warlock', 1250),
('floyd', 'guitar', 'Fender', 'Telecaster', 750),
('habanero99', 'guitar', 'Fender', 'Stratocaster', 650),
('jessiesgirl', 'drum kit', 'Gretsch', 'CTI-J484', 799),
('elvisisalive', 'guitar', 'Gibson', 'Epiphone', 800);";
if ($mysqli->query($query3) === TRUE) {
    echo "<p>8 instruments inserted into instruments table.</p>";
}
else
{
echo mysql_error();
    echo "<p>Error Inserting 8 instruments: </p>" . printf("Errormessage: %s\n", $mysqli->error);
    echo "<p>***********</p>";
    echo $query3;
    echo "<p>***********</p>";
}
*/
$mysqli->close();

?>
<html>
<head>
<title>Creating the 'users' table</title>
<body>
    <h1>Creating the 'users' table in the cars</h1>	
    <?php
    include 'db.php';

    // select a database to work with
    $mysqli-> select_db("samsusedcars");
    Echo ("Selected the Cars database...<br><br>");

    // build a sql query to create the table
    $query = "CREATE TABLE users
    ( id int(4) NOT NULL auto_increment, username varchar(65) NOT NULL, password varchar(65) NOT NULL,
        role varchar(65) NOT NULL, PRIMARY KEY(id))";
    //echo '<p>***************</p>';
    //echo $query;
    //echo '<p>***************</p>';

    if ($mysqli -> query($query) === TRUE)
    {
        echo "<p>Database table 'users' created</p>";
    }
    else
    {
        echo "<p>Error: " . mysqli_error($mysqli) . "</p>";
        echo $query;
    }
    // add a record for Sam
    $query = "INSERT INTO users (username, password, role) VALUES ('checkme', '$uper$ecret', 'Owner');";

    if ($mysqli -> query($query) === TRUE)
    {
        echo "<p>Sam's record was inserted into the users table.</p>";
    }
    else
    {
        echo "<p>Error inserting Sam: </p>" . mysqli_error($mysqli) . "</p";
        echo '<p>***************</p>';
        echo $query;
        echo '<p>***************</p>';
    }

    $mysqli -> close();
    include 'footer.php';


    ?>
</body>	
</head>
</html>


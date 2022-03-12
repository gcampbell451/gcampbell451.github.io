 <?php
$mysqli = new mysqli('mysql.tarheeltitles.com', 'web2502022', 'Database250!', 'samsusedcars' );
/* check connection */
if (mysqli_connect_errno()) {
    printf("Connect failed: %s\n", mysqli_connect_error());
    exit();
}
//select a database to work with
$mysqli->select_db("Cars");
 
?>
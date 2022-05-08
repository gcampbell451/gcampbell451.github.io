<?php
// demo how to process a login form
include 'db.php';

// select a database to work with
$mysqli -> select_db("Cars");
echo("Selected the Cars database...<br><br>");

// get username and password from login form
$myusername=$_POST['myusername'];
$mypassword=$_POST['mypassword'];

// to protect against sql injection
$myusername = stripslashes($myusername);
$mypassword = stripslashes($mypassword);
//$myusername = mysql_real_escape_string($myusername);
//$mypassword = mysql_real_escape_string($mypassword);

$query = "SELECT * FROM Users WHERE username='$myusername' and password = '$mypassword'";
$result = $mysqli -> query($query);

$count = mysqli_num_rows($result);
// if result matched $myusername and $mypassword, the count of table rows should be 1

if($count == 1)
{
    session_start();
    $_SESSION['MyUserName'] = $myusername;
    while ($result_ar = mysqli_fetch_assoc($result))
    {
        $_SESSION['Role'] = $result_ar['Role'];
    }
    header("location:login_success.php");
}
else
{
    echo "Wrong Username or Password";
}
?>
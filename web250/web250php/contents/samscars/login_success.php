<?php
session_start();
// if user is not logged in, redirect them to the login page
if (!isset($_SESSION['MyUserName']))
{
    header("location:../login.html");
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel = "stylesheet" type = "text/css" href = "styles/default.css" />
    <title>Login Success</title>
</head>
<body>
    <div class="brand_box">
    Login Successful
    </div>
</body>
</html>


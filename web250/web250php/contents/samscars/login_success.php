<?php
session_start();
// if user is not logged in, redirect them to the login page
if (!isset($_SESSION['MyUserName']))
{
    header("location:../login.html");
}
header("location:../../index.php");
?>

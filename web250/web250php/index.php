<!DOCTYPE html>
<html lang="en">
<head>
	<meta http-equiv="content-type" content="text/html;charset=UTF-8" />
	<title>Axes, Et Cetera | Table of Contents</title>
	<link rel = "stylesheet" type = "text/css" href = "styles/default.css" />
</head>
<body>
<header>
    <div class="logo">
        <a href="index.php"><img class="transparent" src="images/guitar_logo_small.png" alt="Logo courtesy of nicepng.com"></a>
    </div>
    <h1 class="logo">Axes, Et cetera</h1>
    <p class="tagline center">One man's trash is another man's Trea$ure!</p>
	<div id="headernav">
            <nav>
				<a href = "?p=contents/introduction.php">Introduction</a> |
                <a href = "?p=contents/contract.php">Course Contract</a> |
                <a href = "?p=contents/brand.php">Brand Page</a> |
                <a href = "?p=contents/samscars/samsusedcars.html">Sam's Used Cars</a> |
                <a href="?p=contents/m6_forms.php">M6 Forms</a>
		    </nav>
        </div>
</header>
<!-- dynamic content goes here -->
<h2 class="center">Table of Contents</h2>
<ol>
		<li class="toc_li">
		    <a href = "?p=contents/introduction.php">Introduction</a> 
		</li>
		<li class="toc_li">
		    <a href = "?p=contents/contract.php">Course Contract</a>
		</li>
		<li class="toc_li">
			<a href="?p=contents/brand.php">Brand Page</a>
		</li>
        <li class="toc_li">
			<a href="?p=contents/samscars/samsusedcars.html">Sam's Used Cars</a>
		</li>
        <li class="toc_li">
            <a href="?p=contents/m6_forms.php">One Form, Two Forms, Red Forms, Green Forms, Two Results, One Page</a>
        </li>
	</ol>
<?php
	$sPage = $_GET["p"];
	//echo ("You picked the page: " . $sPage); 
	
	if($sPage == "") {  $sPage = "home.php"; }
	include($sPage);
?>
<footer>
    <nav>			
        <a href="https://github.com/gcampbell451" target="_blank">GitHub</a> |
        <a href="https://gcampbell451.github.io/web250/index.html" target="_blank">GitHub.io</a> |
        <a href="https://gcampbell451.github.io/web250/index.html" target="_blank">web250</a> |
        <a href="https://www.freecodecamp.org/gcampbe2" target="_blank">FreeCodeCamp</a> |
        <a href="https://www.codecademy.com/profiles/gcampbe2" target="_blank">Codecademy</a> |
        <a href="https://jsfiddle.net/user/gcampbe2/fiddles/" target="_blank">JSFiddle</a>	|	
        <a href="https://www.linkedin.com/in/gregory-campbell-27b496162/" target="_blank">LinkedIn</a>			
    </nav>
                
	Designed by Campbell Ink. &copy; 2021<br><br>
    <a href = "https://validator.w3.org/check?uri=" id = "validation_link_html" class="htmlbutton">W3C HTML</a>&nbsp;&nbsp;
    <a href = "https://jigsaw.w3.org/css-validator/check/referer?uri=" id = "validation_link_css" class="cssbutton">W3C CSS</a>
    <script>
        document.getElementById("validation_link_html").setAttribute("href", "https://validator.w3.org/check?uri=" + location.href);
        document.getElementById("validation_link_css").setAttribute("href", "https://jigsaw.w3.org/css-validator/validator?uri=" + location.href);
    </script>
</footer>

</body>
</html>
<main>
<div class="brand_box">
    <h2>One Form, Two Forms, Red Forms, Green Forms, Two Results, One Page</h2>
    <div class="m6_forms">
	<form action="" method="post" >
		<label for="first">First name:</label>
		<input type="text" name="first"><br><br>
		<label for="last">Last name:</label>
		<input type="text" name="last"><br><br>
		<input type="submit" name = "submit1" value="Submit" class="submitbutton"><br><br>
	</form>
				
		<!-- PHP that outputs the form results -->

		<?php 
			$outputString = "Your name is ";
			if (isset($_POST["submit1"])) { 
				$first = $_POST["first"]; 
				$outputString = $outputString . $first . " ";
				$last = $_POST["last"]; 
				$outputString = $outputString . $last;
				echo $outputString; 				 	  
			} 
		?> 

	</div>
	
	<div class="m6_forms">
	<h4 class="center">This form will use the POST method</h4>
	<form action="" method="post" >
		<label for="instrument">What kind of instrument do you wish to buy/sell?</label>
		<input type="text" name="post_instrument"><br><br>
		<label for="price">What is your asking price?</label>
		<input type="text" name="post_price"><br><br>
		<input type="submit" name = "submit2" value="Submit" class="submitbutton"><br><br>
	</form>

		<!-- PHP that outputs the form results -->

		<?php 
			$outputString2 = "You wish to buy/sell a ";
			if (isset($_POST["submit2"])) { 
				$instrument = $_POST["post_instrument"]; 
				$outputString2 = $outputString2 . $instrument . " for $";
				$price = $_POST["post_price"]; 
				$outputString2 = $outputString2 . $price . ".";
				echo $outputString2; 				 	  
			} 
		?>

	</div>
	
	<div class="m6_forms">
	<h4 class="center">This form will use the GET method</h4>
	<form action="" method="get">
		<label for="instrument">What kind of instrument do you wish to buy/sell?</label>
		<input type="text" name="get_instrument"><br><br>
		<label for="price">What is your asking price?</label>
		<input type="text" name="get_price"><br><br>
		<input type="submit" name = "submit3" value="Submit" class="submitbutton">
	</form>

		<!-- PHP that outputs the form results -->

		<?php 
			$outputString3 = "You wish to buy/sell a ";
			if (isset($_GET["submit3"])) { 
				$instrument = $_GET["post_instrument"]; 
				$outputString3 = $outputString3 . $instrument . " for $";
				$price = $_GET["post_price"]; 
				$outputString3 = $outputString3 . $price . ".";
				echo $outputString3; 				 	  
			} 
		?>

	</div>





</div>
</main>
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
			if (isset($_POST["submit1"])) { 
				$first = $_POST["first"]; 
				$last = $_POST["last"]; 
				echo "Your name is ". $first  . " " . $last . ".\n\n"; 
				echo "";				 	  
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
			if (isset($_POST["submit2"])) { 
				$instrument = $_POST["post_instrument"]; 
				$price = $_POST["post_price"]; 
				echo "You want to buy/sell a " . $instrument . " for $" . $price . "."; 				 	  
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
			if (isset($_GET["submit2"])) { 
				$instrument = $_GET["get_instrument"]; 
				$price = $_GET["get_price"]; 
				echo "You want to buy/sell a " . $instrument . " for $" . $price . "."; 				 	  
			} 
		?>

	</div>





</div>
</main>
<main>
	<h2 class="center" id="toc_h2">Gregory Campbell | One Form, Two Forms, Red Forms, Green Forms, Two Results, One Page</h2>
	<?php 
	// define variables and set to empty values
	$first = $last = "";
	?>
<div class="brand_box">
    
    <div class="m6_forms">
	<form action="" method="post" >
		<label for="first" >First name:</label>
		<input type="text" name="first" class="label_entry" value="<?php echo $first;?>"><br><br>
		<label for="last">Last name:</label>
		<input type="text" name="last" class="label_entry"  value="<?php echo $last;?>"><br><br>
		<input type="submit" name = "submit1" value="Submit" class="submitbutton"><br><br>
	</form>
				
		<!-- PHP that outputs the form results -->
		
		<?php 
			$outputString = "Your name is ";
			if (isset($_POST["submit1"])) { 
				$first = $_POST["first"]; 
				$outputString = $outputString . $first . " ";
				$last = $_POST["last"]; 
				$outputString = $outputString . $last . ".";
				echo $outputString; 				 	  
			} 
		?>

	</div>
	
	<div class="m6_forms">
	<h4 class="center">This form will use the POST method</h4>
	<form action="" method="post" >
		<label for="instrument">What kind of instrument do you wish to buy/sell?</label>
		<input type="text" name="post_instrument" class="label_entry"><br><br>
		<label for="price">What is your asking price?</label>
		<input type="text" name="post_price" class="label_entry"><br><br>
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
	<form action="contents/m6_forms_processing.php" method="get">
		<label for="instrument">What kind of instrument do you wish to buy/sell?</label>
		<input type="text" name="get_instrument" class="label_entry"><br><br>
		<label for="price">What is your asking price?</label>
		<input type="text" name="get_price" class="label_entry"><br><br>
		<input type="submit" name = "submit3" value="Submit" class="submitbutton">
	</form>

		<!-- PHP that outputs the form results -->

		<?php 
			function output_get() {
				include 'm6_forms_processing.php';
				echo $outputString3; 	
			}				 	   
		?>

	</div>





</div>
</main>
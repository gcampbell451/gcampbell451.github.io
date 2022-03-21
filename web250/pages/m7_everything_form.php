<main>
    <h2 class="center" id="toc_h2">Gregory Campbell | Everything Form</h2>
	<?php 
	// define variables and set to empty values
    $username = $password = $transaction = $guitar = $bass = $piano = $other = $quantity = $color = $date =  $datetime = 
    $email = $file = $bdaymonth = $phone = $appt = $homepage = $week = $happy = $google_search = "";
	?>

    
<div class="brand_box">
    <!-- PHP that outputs the form results -->
		
    <?php 
            

            
			$outputString = "Your username is ";
			if (isset($_POST["submit1"])) { 
                // assign values to variables 
                $google_search = $_POST["google_search"];             
				$username = $_POST["username"];
				$password = $_POST["password"]; 
                $transaction = $_POST["transaction"];
                // account for empty checkboxes
                if (!empty($_POST["guitar"])){
                    $guitar = $_POST["guitar"];
                }
                if (!empty($_POST["bass"])){
                    $bass = $_POST["bass"];
                }
                if (!empty($_POST["piano"])){
                    $piano = $_POST["piano"];
                }
                if (!empty($_POST["other"])){
                    $other = $_POST["other"];
                }              
                $quantity = $_POST["quantity"];
                $color = $_POST["color"];
                $date = $_POST["date"];
                $datetime = $_POST["datetime"];
                $email = $_POST["email"];
                $file = $_POST["file"];
                $bdaymonth = $_POST["bdaymonth"];
                $phone = $_POST["phone"];
                $appt = $_POST["appt"];
                $homepage = $_POST["homepage"];
                $week = $_POST["week"];
                $happy = $_POST["happy"];
                

        
                // output results
                echo ("<h2>Form Results</h2>");
                echo ("<p>Your Google search string: $google_search</p>");
				echo ("<p>Username: $username</p>");
                echo ("<p>Password: $password</p>");
                echo ("<p>Transaction type: $transaction</p>");	
                echo ("<p>Instrument(s): $guitar $bass $piano $other</p>");
                echo ("<p>Quantity: $quantity</p>");
                echo ("<p>Color: $color</p>");
                echo ("<p>Date of desired appointment: $date</p>");
                echo ("<p>Time of desired appointment: $datetime</p>");
                echo ("<p>Your email: $email</p>");
                echo ("<p>Your file to upload: $file</p>");
                echo ("<p>Your birthday: $bdaymonth</p>");
                echo ("<p>Your phone number: $phone</p>");
                echo ("<p>Your appointment time: $appt</p>");
                echo ("<h3>Vendors</h3>");
                echo ("<p>Your web page: $homepage</p>");
                echo ("<p>Your preferred week for the trade exhibition: $week</p>");
                echo ("<p>Your happiness level: $happy</p>");
                echo ("<h3>Thanks for your time!</h3>");

			} 
		?>
    <div class="m6_forms">
	<form action="" method="post" >
        <!-- search input type -->
        <label for="google_search">Search Google:</label>
        <input type="search" id="google_search" name="google_search" class="label_entry" value="<?php echo $google_search;?>"><br><hr>

        <!-- button input type -->
        <p>Click below to see if you have won today's prize giveaway!</p>
        <input type="button" onclick="alert('Welcome to Axes, Et Cetera! Sorry, better luck next time!')" value="Click For a Chance to Win!" class="cssbutton"><br><br><hr>

        <!-- text input type -->
        <p>Log in:</p>
		<label for="username" >Username:</label>
		<input type="text" name="username" class="label_entry" required><br><br>

        <!-- password input type -->
		<label for="password">Password:</label>
		<input type="password" name="password" class="label_entry" required><br><br><hr>

        <!-- radio input type -->
        <p>Do you wish to buy or sell an instrument?</p>
        <input type="radio" id="buy" name="transaction" value="Buy">
        <label for="buy">Buy</label><br>
        <input type="radio" id="sell" name="transaction" value="Sell">
        <label for="sell">Sell</label><br><br><hr>

        <!-- checkbox input type -->
        <p>What kind of instrument?</p>
        <input type="checkbox" id="guitar" name="guitar" value="Guitar" <?php if(isset($_POST['guitar'])) echo "checked='checked'"; ?>>
        <label for="guitar">Guitar</label><br>
        <input type="checkbox" id="bass" name="bass" value="Bass" <?php if(isset($_POST['bass'])) echo "checked='checked'"; ?>>
        <label for="bass">Bass</label><br>
        <input type="checkbox" id="piano" name="piano" value="Piano" <?php if(isset($_POST['piano'])) echo "checked='checked'"; ?>>
        <label for="piano">Piano</label><br>
        <input type="checkbox" id="other" name="other" value="Other" <?php if(isset($_POST['other'])) echo "checked='checked'"; ?>>
        <label for="other">Other</label><br><br><hr>

        <!-- number input type -->
        <p>How many instruments?</p>
        <label for="quantity">Quantity (between 1 and 10):</label>
        <input type="number" id="quantity" name="quantity" min="1" max="10" class="label_entry" value="<?php echo $quantity;?>" required><br><br><hr>

        <!-- color input type -->
        <label for="color">What color, approximately, is the instrument?</label>
        <input type="color" id="color" name="color" class="label_entry" value="<?php echo $color;?>" ><br><br><hr>

        <!-- date input type -->
        <label for="date">Select a date to come by and speak to a member of our team:</label>
        <input type="date" id="date" name="date" class="label_entry" value="<?php echo $date;?>" required><br><br>

        <!-- datetime input type -->
        <label for="datetime">What time is best for you to come by?</label><br>
        <input type="datetime-local" id="datetime" name="datetime" class="label_entry" value="<?php echo $datetime;?>" required><br><br>

        <!-- email input type -->
        <label for="email">Enter your preferred email to receive confirmation of your appointment:</label><br>
        <input type="email" id="email" name="email" class="label_entry" value="<?php echo $email;?>" required><br><br><hr>

        <!-- file input type -->
        <p>If you are returning or exchanging an instrument, please upload your receipt below to facilitate processing.</p>
        <label for="file">Select a file to upload:</label><br>
        <input type="file" id="file" name="file" class="label_entry"><br><br><hr>

        <!-- hidden input type -->
        <input type="hidden" id="custId" name="custId" value="1234">

        <!-- month input type -->
        <p>Tell us what month your birthday is in for a gift!</p>
        <label for="bdaymonth">Birthday (month and year):</label><br>
        <input type="month" id="bdaymonth" name="bdaymonth" class="label_entry" value="<?php echo $bdaymonth;?>" required><br><br><hr>

        <!-- tel input type -->
        <label for="phone">If you want a member of our team to call you, enter your telephone number in XXX-XXX-XXXX format:</label>
        <input type="tel" id="phone" name="phone" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" class="label_entry" value="<?php echo $password;?>"><br><br>

        <!-- time input type -->
        <label for="appt">What time would be best to reach you?</label>
        <input type="time" id="appt" name="appt" class="label_entry" value="<?php echo $appt;?>" ><br><br><hr>

        <!-- url input type -->
        <p>Vendors, please give us your web address so we can link ours to yours!</p>
        <label for="homepage">Add your homepage:</label>
        <input type="url" id="homepage" name="homepage" class="label_entry" value="<?php echo $homepage;?>" required><br>

        <!-- week input type -->
        <p>We're considering hosting a trade exhibition. What would be your preferred week to set up a station?</p>
        <label for="week">Select a week:</label>
        <input type="week" id="week" name="week" class="label_entry" value="<?php echo $week;?>"><br><br><hr>

        <!-- range input type -->
        <label for="happy">How much have you enjoyed your experience on our site, on a scale of 1-10?</label>
        <input type="range" id="happy" name="happy" min="0" max="10"><br><br>

        <!-- submit, reset, image input type -->
		<input type="submit" name="submit1" value="Submit" class="submitbutton"><br><br>
        <input type="reset" name="reset" class="resetbutton"><br><br>

        
	</form>
				
		

	</div>
</div>
</main>
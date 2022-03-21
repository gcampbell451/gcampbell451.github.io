<main>
    <h2 class="center" id="toc_h2">Gregory Campbell | Demonstrate Math, Dates, & Strings</h2>		
    <?php 
       // echo(), strtoupper(), date(), sunrise(), sunset(), gmdate(), mktime() = 5 date fxns
       echo strtoupper("<h4>welcome to axes, et cetera!</h4>");
       echo date("l") . ", " . date("F d") . ", " . date("Y");
       echo("<br>Charlotte, NC<br>Sunrise: " . date_sunrise(time(),SUNFUNCS_RET_STRING,35.23,-80.84,90.833,-5)); 
       echo("<br>Sunset: " . date_sunset(time(),SUNFUNCS_RET_STRING,35.23,-80.84,90.833,-5));
       echo("<br>Did you know? December 19, 1974 was on a ".gmdate("l", mktime(0,0,0,12,19,1974)) . ".");
    ?>

    <div class="brand_box">
    <?php
       // chop(), printf()
       $special = "1986 B.C. Rich Warlock!!!!!";
       $chopped_special = rtrim($special, "!");
       $price = 1395;
       printf("Today's Special: %s for just $%.2f!", $chopped_special, $price);
        

    ?>
    <img class="center" src="images/warlock.png" alt="B.C. Rich Warlock">
    <?php
        // number_format() = 5 string fxns, rand(), round(), pi(), ceil(), floor() = 5 math fxns
        $cost = $price * 1.075;
        echo("After tax, this beauty can be yours for $" . number_format($cost,2) . "!");
        echo("<br><br>Weekly special: Every day this week, the " . rand(5,10) .
             "th visitor to our store will be entered in a drawing for a chance at a free pack of guitar strings!");
        echo("<br><br>Monthly special: Our Pi Day(". round(pi(),2) . ") special was so popular, we're extending it through the
               end of the month: with the purchase of a guitar or bass at full price, you can add a soft gig bag for $" .
               ceil(pi()) * 5 . " or a hard case for $" . floor(pi()) * 10 . "!");
    ?>


    
    </div>
</main>
<h2 class="center" id="toc_h2">Gregory Campbell | Dynamize a Site with Text Records</h2>
<div class="brand_box">
<h4 class="center">The Axes, Et Cetera Staff</h4>
<?php
    // open and read the file
 
    $infile = fopen("aec_staff.txt", "r");

    // open if there, read as long as values are there
    if($infile) {
        while(!feof($infile)) {
            // put contents into string, use explode() to put contents into array
            $file_contents = fgets($infile);
            $array = explode("||", $file_contents);

            // display contents of array
            echo "<div class='dynamize_table'>" . 
                    "<table>".
                        "<tr>". 
                            "<td>" . "<img src='images/" . $array[0] . "'>" .
                                    "<figure>"."<figcaption>"."Image courtesy of <a href='https://www.freeimages.com/'>FreeImages.com</a>"."</figcaption>"."</figure>".
                            "</td>". 
                            "<td>". "$array[1]". 
                            "</td>" .       
                    "</table>" . 
                 "</div>";
        }
        // close the file
        fclose($infile);
    } else {
        echo "Error! Unable to open file.";
    }

?>
<h4 class="center">Thanks for taking the time to read about our staff! We're here to help you with all of your vintage instrument needs!</h4>
</div>
function chap41() {				// Modifies chap21 to use a while loop
	var matchFound = false;		// Initializes matchFound variable
	var query = prompt("Enter an exotic car brand", "Enter here");		// Prompts user to enter a car brand and stores the input in a variable.
	query = query.toLowerCase();				// Forces user input to all lower case
	var cars = ["ferrari", "lamborghini", "porsche", "maclaren", "pagani"];
	var i=0;
	/*
		The following loop cycles through the array until it finds a match or reaches the end of the array.
	*/
	while (i<=cars.length) {
		if(query===cars[i]) {
			matchFound = true;
			alert("It's on the list!");
			break;
		}
		i++;
	}
	if(matchFound===false) {
		alert("Tis not on the list.");
	}
}

function chap42() {		// Modifies chap21 to use a do...while loop
	var matchFound = false;
	var query = prompt("Enter an exotic car brand", "Enter here");
	query = query.toLowerCase();
	var cars = ["ferrari", "lamborghini", "porsche", "maclaren", "pagani"];
	var i=0;						
	do {
		if(query===cars[i]) {
			matchFound = true;
			alert("It's on the list!");
			break;
		}
		i++;
	} while (i<=cars.length);
	if(matchFound===false) {
		alert("Tis not on the list.");
	} 
}

function chap46() {    // Simple function to display an alert when a button is clicked
	alert("You clicked it!");
}

function chap47() {	   // Simple function to display an alert when the mouse hovers over a button
	alert("Are you looking at me?");
}

function chap48() {
	this.style.backgroundColor='white';
}

function chap49() {						// This function personalizes the h3 greeting for the page
	var first = document.getElementById("first_name").value;
	var last  = document.getElementById("last_name").value;
			
	// Write out welcome using user input
	document.getElementById("greeting").innerHTML = "Hello, " + first + " " +  last + "!";		
}

function chap50() {						
	document.getElementById("answer").value = "That's a nice name!";
}

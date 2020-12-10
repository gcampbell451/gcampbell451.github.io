function changeGreeting() {						// This function personalizes the h3 greeting for the page
	var first = document.getElementById("first_name").value;
	var mid   = document.getElementById("middle_initial").value;		// Get user's name
	var last  = document.getElementById("last_name").value;
			
	// Write out welcome using user input
	if (mid !== "") {
		document.getElementById("greeting").innerHTML = "Welcome to Campbell Ink, " + first + " " + mid + ". " + last + "!";
	} else {
		document.getElementById("greeting").innerHTML = "Welcome to Campbell Ink, " + first + " " + last + "!";		
	}	
	// Create loop which prints themed message
	var msg = "";
	var i;
	for (i = 1; i < 126; i++) {
		msg += i + ".&nbsp;Solving your problems!" + "<br>";
			
	// Write output to page	
	var writeToPage = document.getElementById("loop");
	writeToPage.innerHTML = msg;
	}		
}

function changeGreeting2() {					// This function personalizes the h3 greeting for the page
	var first = document.getElementById("first_name").value;
	var mid   = document.getElementById("middle_initial").value;	// Get user's name
	var last  = document.getElementById("last_name").value;
			
	// Write out welcome using user input
	if (mid !== "") {
		document.getElementById("greeting").innerHTML = "Welcome to Campbell Ink, " + first + " " + mid + ". " + last + "!";
	} else {
		document.getElementById("greeting").innerHTML = "Welcome to Campbell Ink, " + first + " " + last + "!";		
	}
			
	// Prompt user for a number
	var howHigh = prompt("How high do you want to count, " + first + "?");
	var thisHigh = parseInt(howHigh);
		
	// Create loop which prints different message based on whether user's input was even or odd.
	var msg = "";
	var i;
	for (i = 1; i <= thisHigh; i++) {
		if (i % 2 == 0) {
			msg += i + ".&nbsp;Solving your problems! - The number is even." + "<br>";
		} else {
			msg += i + ".&nbsp;Solving your problems! - The number is odd." + "<br>";
		}
	// Write output to page
	var writeToPage = document.getElementById("loop");
	writeToPage.innerHTML = msg;
	}
}

function fizzbuzz1() {					// This function creates a loop with a decision tree
	var first = document.getElementById("first_name").value;
	var mid   = document.getElementById("middle_initial").value;	// Get user's name
	var last  = document.getElementById("last_name").value;
			
	// Write out welcome using user input
	if (mid !== "") {
		document.getElementById("greeting").innerHTML = "Welcome to Campbell Ink, " + first + " " + mid + ". " + last + "!";
	} else {
		document.getElementById("greeting").innerHTML = "Welcome to Campbell Ink, " + first + " " + last + "!";		
	}
	
	// Create loop
	var msg = "";
	var i;
	for (i = 1; i <= 140; i++) {
		if (i % 3 == 0 && i % 5 != 0) {
			msg += i + ".&nbsp;Solve" + "<br>";
		} else if (i % 3 != 0 && i % 5 == 0) {
			msg += i + ".&nbsp;Problems!" + "<br>";
		} else if (i % 3 == 0 && i % 5 == 0) {
			msg += i + ".&nbsp;Solve Problems!" + "<br>";
		} else {
			msg += i + ".&nbsp;Ink!" + "<br>";
		}
	// Write output to page
	var writeToPage = document.getElementById("loop");
	writeToPage.innerHTML = msg;
	}
}

function fizzbuzz2() {
	var first = document.getElementById("first_name").value;
	var mid   = document.getElementById("middle_initial").value;	// Get user's name
	var last  = document.getElementById("last_name").value;
	
	// Write out welcome using user input
	if (mid !== "") {
		document.getElementById("greeting").innerHTML = "Welcome to Campbell Ink, " + first + " " + mid + ". " + last + "!";
	} else {
		document.getElementById("greeting").innerHTML = "Welcome to Campbell Ink, " + first + " " + last + "!";		
	}
	
	// Assign numbers for variables
	var firstDivisor = 3;
	var secondDivisor = 5;
	
	// Create function to test for remainder
	function checkDiv(num1, num2) {
		if (num1 % num2 === 0) {
			return true;
		} else {
			return false;
		}
	}

	// Create loop
	var msg = "";
	var i = 0;
	for (i = 1; i <=140; i++) {
		if (checkDiv(i, firstDivisor) && !checkDiv(i, secondDivisor)) {
			msg += i + ".&nbsp;Solve" + "<br>";
		} else if (!checkDiv(i, firstDivisor) && checkDiv(i, secondDivisor)) {
			msg += i + ".&nbsp;Problems!" + "<br>";
		} else if (checkDiv(i, firstDivisor) && checkDiv(i, secondDivisor)) {
			msg += i + ".&nbsp;Solve Problems!" + "<br>";
		} else {
			msg += i + ".&nbsp;Ink!" + "<br>";
		}
	// Write output to page
	var writeToPage = document.getElementById("loop");
	writeToPage.innerHTML = msg;		
	}
	
}

function fizzbuzz3() {
	var first = document.getElementById("first_name").value;
	var mid   = document.getElementById("middle_initial").value;	// Get user's name
	var last  = document.getElementById("last_name").value;
	
	// Write out welcome using user input
	if (mid !== "") {
		document.getElementById("greeting").innerHTML = "Welcome to Campbell Ink, " + first + " " + mid + ". " + last + "!";
	} else {
		document.getElementById("greeting").innerHTML = "Welcome to Campbell Ink, " + first + " " + last + "!";		
	}
	
	// Assign numbers for variables
	var firstDivisor = 3;
	var secondDivisor = 5;
	var thirdDivisor = 7;

	// Create function to test for remainder
	function checkDiv(num1, num2) {
		if (num1 % num2 === 0) {
			return true;
		} else {
			return false;
		}
	}	
	// Create loop
	var msg = "";
	var i;
	for (i = 1; i <= 140; i++) {
		if (checkDiv(i, firstDivisor) && !checkDiv(i, secondDivisor) && !checkDiv(i, thirdDivisor)) {			// 3 only
			msg += i + ".&nbsp;Solve" + "<br>";
		} else if (!checkDiv(i, firstDivisor) && checkDiv(i, secondDivisor) && !checkDiv(i, thirdDivisor)) { 	// 5 only
			msg += i + ".&nbsp;Problems!" + "<br>";
		} else if (!checkDiv(i, firstDivisor) && !checkDiv(i, secondDivisor) && checkDiv(i, thirdDivisor)) {	// 7 only
			msg += i + ".&nbsp;Quickly!" + "<br>";
		} else if (checkDiv(i, firstDivisor) && checkDiv(i, secondDivisor) && !checkDiv(i, thirdDivisor)) {		// 3-5 only
			msg += i + ".&nbsp;Solve Problems!" + "<br>";
		} else if (checkDiv(i, firstDivisor) && !checkDiv(i, secondDivisor) && checkDiv(i, thirdDivisor)) {		// 3-7 only
			msg += i + ".&nbsp;Solve Quickly!" + "<br>";
		} else if (!checkDiv(i, firstDivisor) && checkDiv(i, secondDivisor) && checkDiv(i, thirdDivisor)) {		// 5-7 only
			msg += i + ".&nbsp;Problems Quickly!" + "<br>";
		} else if (checkDiv(i, firstDivisor) && checkDiv(i, secondDivisor) && checkDiv(i, thirdDivisor)) {		// 3-5-7
			msg += i + ".&nbsp;Solve Problems Quickly!" + "<br>";
		} else {
			msg += i + ".&nbsp;Ink!" + "<br>";
		}
	// Write output to page
	var writeToPage = document.getElementById("loop");
	writeToPage.innerHTML = msg;
	}
}

function fizzbuzz4() {
	var first = document.getElementById("first_name").value;
	var mid   = document.getElementById("middle_initial").value;	// Get user's name
	var last  = document.getElementById("last_name").value;
	var howHigh = document.getElementById("count").value;
	var thisHigh = parseInt(howHigh);
	var number1 = document.getElementById("number1").value;
	var number2 = document.getElementById("number2").value;
	var number3 = document.getElementById("number3").value;
	var firstDivisor = parseInt(number1);
	var secondDivisor = parseInt(number2);
	var thirdDivisor = parseInt(number3);
	var word1 = document.getElementById("word1").value;
	var word2 = document.getElementById("word2").value;
	var word3 = document.getElementById("word3").value;
	var word4 = document.getElementById("word4").value;

	// Write out welcome using user input
	if (mid !== "") {
		document.getElementById("greeting").innerHTML = "Welcome to Campbell Ink, " + first + " " + mid + ". " + last + "!";
	} else {
		document.getElementById("greeting").innerHTML = "Welcome to Campbell Ink, " + first + " " + last + "!";		
	}

	// Create function to test for remainder
	function checkDiv(num1, num2) {
		if (num1 % num2 === 0) {
			return true;
		} else {
			return false;
		}
	}	
	// Create loop
	var msg = "";
	var i;
	for (i = 1; i <= thisHigh; i++) {
		if (checkDiv(i, firstDivisor) && !checkDiv(i, secondDivisor) && !checkDiv(i, thirdDivisor)) {			// 3 only
			msg += i + ". " + word1 + "<br>";
		} else if (!checkDiv(i, firstDivisor) && checkDiv(i, secondDivisor) && !checkDiv(i, thirdDivisor)) { 	// 5 only
			msg += i + ". " + word2 + "<br>";
		} else if (!checkDiv(i, firstDivisor) && !checkDiv(i, secondDivisor) && checkDiv(i, thirdDivisor)) {	// 7 only
			msg += i + ". " + word3 + "<br>";
		} else if (checkDiv(i, firstDivisor) && checkDiv(i, secondDivisor) && !checkDiv(i, thirdDivisor)) {		// 3-5 only
			msg += i + ". " + word1 + " " + word2 + "<br>";
		} else if (checkDiv(i, firstDivisor) && !checkDiv(i, secondDivisor) && checkDiv(i, thirdDivisor)) {		// 3-7 only
			msg += i + ". " + word1 + " " + word3 + "<br>";
		} else if (!checkDiv(i, firstDivisor) && checkDiv(i, secondDivisor) && checkDiv(i, thirdDivisor)) {		// 5-7 only
			msg += i + ". " + word2 + " " + word3 + "<br>";
		} else if (checkDiv(i, firstDivisor) && checkDiv(i, secondDivisor) && checkDiv(i, thirdDivisor)) {		// 3-5-7
			msg += i + ". " + word1 + " " + word2 + " " + word3 + "<br>";
		} else {
			msg += i + ". " + word4 + "<br>";
		}
	// Write output to page
	var writeToPage = document.getElementById("loop");
	writeToPage.innerHTML = msg;
	}
}
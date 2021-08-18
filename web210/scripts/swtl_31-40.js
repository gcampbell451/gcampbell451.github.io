function chap31() { // Gets system time
	var dateTime = new Date();
	alert(dateTime);
}

function chap31a() { // Gets day of week
	var days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
	var today = new Date();
	var date = today.getDay();
	var todaysName = days[date];
	alert("The day of the week is " + todaysName + ".");
}

function chap32() { // Gets month of year
	var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
	var today = new Date();
	var date = today.getMonth();
	var todaysMonth = months[date];
	alert("The month of the year is " + todaysMonth + ".");
}

function chap32a() { // Gets day of month
	var today = new Date();
	var date = today.getDate();;
	alert("The day of the month is " + date + ".");
}

function chap32b() { // Gets current year
	var today = new Date();
	var todaysYear = today.getFullYear();
	alert("The current year is " + todaysYear + ".");
}

function chap32c() { // Gets current hour of day
	var today = new Date();
	var hour = today.getHours();
	alert("The current hour is " + hour + ".");
}

function chap32d() { // Gets current minute of hour
	var today = new Date();
	var min = today.getMinutes();
	alert("The current minute is " + min + ".");
}

function chap32e() { // Gets current second of minute
	var today = new Date();
	var sec = today.getSeconds();
	alert("The current second was " + sec + ".");
}

function chap32f() { // Gets current millisecond
	var today = new Date();
	var ms = today.getMilliseconds();
	alert("The current millisecond was just " + ms + ".");
}

function chap32g() { // Gets milliseconds since 1/1/70
	var today = new Date();
	var bigNum = today.getTime();
	alert("The number of milliseconds since January 1, 1970 is " + bigNum + ".");
}

function chap33() {
	var today = new Date();							// Create a date object for today.
	var endOfYear = new Date("December 31, 2020");  // Note the naming convention on the date. This must be followed exactly.
	var msToday = today.getTime();					// Get ms since 1/1/1970 for today.
	var msEndOfYear = endOfYear.getTime();			// Get ms since 1/1/1970 for the end of this year.
	var msDiff = msEndOfYear - msToday;				// Calculate the difference.
	var days = msDiff / (1000 * 60 * 60 * 24);		// Converts ms into days.
	days = Math.floor(days);						// This rounds the above calculation down to an integer.
	alert("This year will end in " + days + " days. 2021 can't come fast enough!");
}

function chap34() { // Gets current year then changes the year
	var today = new Date();
	today.setFullYear(2021);
	todaysYear = today.getFullYear();
	alert("The current year is " + todaysYear + ".");
}

function chap36() {
	var userNum1 = "Enter a number";
	var defaultAnswer1 = "Enter number here";
	var userNum2 = "Enter another number";
	var defaultAnswer2 = "Enter number here";
	var num1 = parseInt(prompt(userNum1, defaultAnswer1));
	var num2 = parseInt(prompt(userNum2, defaultAnswer2));
	function sum(num1, num2) {
		var sum = num1 + num2;	
		alert("The sum of " + num1 + " and " + num2 + " is " + sum + ".");
	}
	sum(num1, num2);
}

function chap37() {
	var userNum1 = "Enter a number";
	var defaultAnswer1 = "Enter number here";
	var userNum2 = "Enter another number";
	var defaultAnswer2 = "Enter number here";
	var num1 = parseInt(prompt(userNum1, defaultAnswer1));
	var num2 = parseInt(prompt(userNum2, defaultAnswer2));
	function sum(num1, num2) {
		return num1 + num2;			// Use return keyword to return the sum
	}
	var total = sum(num1, num2);	// Capture the returned value of the sum function
	alert("The sum of " + num1 + " and " + num2 + " is " + total + ".");
}

function chap38() {
	var global = "Global Scope";
	function chap38a() {
		var local = "Local Scope";
	}
	alert(local);
}

function chap38b() {
	var global = "Global Scope";
	function chap38a() {
		var local = "Local Scope";
	}
	alert(global);
}

function chap39() {
	var userNum = "Choose a number between 1 and 4.";
	var defaultAnswer = "Enter number here";
	var num = parseInt(prompt(userNum, defaultAnswer));
	switch(num) {
	case 1:
	  alert("You chose the number one.");
	  break;
	case 2:
	  alert("You chose the number two.");
	  break;
	case 3:
	  alert("You chose the number three.");
	  break;
	case 4:
	  alert("You chose the number four.");
	  break;
	}
}

function chap40() {
	var userNum = "Choose a number between 1 and 4.";
	var defaultAnswer = "Enter number here";
	var num = parseInt(prompt(userNum, defaultAnswer));
	switch(num) {
	case 1:
	  alert("You chose the number one.");
	case 2:
	  alert("You chose the number two.");
	case 3:
	  alert("You chose the number three.");
	case 4:
	  alert("You chose the number four.");
	}
}

function chap40a() {
	var userNum = "Choose a number between 1 and 4.";
	var defaultAnswer = "Enter number here";
	var num = parseInt(prompt(userNum, defaultAnswer));
	switch(num) {
	case 1:
	  alert("You chose the number one.");
	  break;
	case 2:
	  alert("You chose the number two.");
	  break;
	case 3:
	  alert("You chose the number three.");
	  break;
	case 4:
	  alert("You chose the number four.");
	  break;
	default:
	  alert("Invalid entry. Try again. This time, actually select a number between 1 and 4.");
	}
}
function chap21() {
	var matchFound = false;
	var query = prompt("Enter an exotic car brand", "Enter here");
	query = query.toLowerCase();
	var cars = ["ferrari", "lamborghini", "porsche", "maclaren", "pagani"];
	for(var i=0; i<=4; i++) {
		if(query===cars[i]) {
			matchFound = true;
			alert("It's on the list!");
			break;
		} 
	}
	if(matchFound===false) {
		alert("Tis not on the list.");
	}
}

function chap22() {
	var matchFound = false;
	var query = prompt("Enter an exotic car brand", "Enter here");
	query = query.toLowerCase();
	var cars = ["ferrari", "lamborghini", "porsche", "maclaren", "pagani"];
	var firstChar = query.slice(0, 1);
	var restOfChars = query.slice(1);
	firstChar = firstChar.toUpperCase();
	restOfChars = restOfChars.toLowerCase();
	var firstCap = firstChar + restOfChars;
	for(var i=0; i<=4; i++) {
		if(query===cars[i]) {
			matchFound = true;
			alert(firstCap + " is on the list!");
			break;
		} 
	}
	if(matchFound===false) {
		alert(firstCap + " is not on the list.");
	}
}

function chap23() {
	var text = "the quick brown fox jumped over the lazy dog.";
	alert(text.indexOf("the"));
} 

function chap23a() {
	var text = "the quick brown fox jumped over the lazy dog.";
	alert(text.lastIndexOf("the"));
} 

function chap23b() {
	var text = "the quick brown fox jumped over the lazy dog.";
	var firstChar = text.indexOf("the");
	text = text.slice(0, firstChar) + "The" + text.slice(firstChar + 3);
	alert(text);
}

function chap24() {
	var text = "the quick brown fox jumped over the lazy dog.";
	alert(text.charAt(0));
}

function chap24a() {
	var text = "the quick brown fox jumped over the lazy dog.";
	alert(text.charAt(14));
}

function chap24b() {
	var text = "the quick brown fox jumped over the lazy dog.";
	alert(text.charAt(30));
}

function chap25() {
	var text = "the quick brown fox jumped over the lazy dog.";
	alert(text.replace("the", "THE"));
}

function chap25a() {
	var text = "the quick brown fox jumped over the lazy dog.";
	alert(text.replace(/the/g, "THE"));
}

function chap26() {
	alert(Math.round(.49));	
}

function chap26a() {
	alert(Math.ceil(.49));
}

function chap26b() {
	alert(Math.floor(.99));
}

function chap27() {
		var decimal = Math.random();
		var closer = (decimal * 10) + 1;
		var randomInt = Math.floor(closer);
		alert(randomInt);
}

function chap28() {
	var string = "Enter a number with a decimal part:";
	var defaultAnswer = "Enter number here";
	var query = parseInt(prompt(string, defaultAnswer));
	alert("The parseInt() function returns " + query);
	alert("Add 1 to the parsed number: " + query + " + 1 = " + (query + 1));
}

function chap28a() {
	var string = "Enter the same number you entered above:";
	var defaultAnswer = "Enter number here";
	var query = parseFloat(prompt(string, defaultAnswer));
	alert("The parseFloat() function returns " + query);
	alert("Add 1 to the parsed number: " + query + " + 1 = " + (query + 1));
}

function chap29() {
	var string = "Enter a number with a decimal part:";
	var defaultAnswer = "Enter number here";
	var query = Number(prompt(string, defaultAnswer));
	alert("The Number() function returns " + query);
	alert("Add 1 to the parsed number: " + query + " + 1 = " + (query + 1));
}

function chap29a() {
	var string = "Enter a number with a decimal part:";
	var defaultAnswer = "Enter number here";
	var query = Number(prompt(string, defaultAnswer));
	var numAsString = query.toString();
	alert("The toString() function returns " + numAsString);
	alert("Add 1 to the number: " + numAsString + " + 1 = " + (numAsString + 1));
}

function chap30() {
	var num = 5.45678;
	alert(num.toFixed());
}

function chap30a() {
	var num = 5.45678;
	alert(num.toFixed(2));
}

function chap30b() {
	var num = 5.45678;
	alert(num.toFixed(3));
}

function chap30c() {
	var num = 5.45678;
	alert(num.toFixed(4));
}
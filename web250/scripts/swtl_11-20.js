function chap11() {
	var string1 = "Enter a string.";
	var defaultAnswer1 = "Enter string here."
	var string2 = "Enter a second string.";
	var defaultAnswer2 = "Enter string here."
	var question1 = prompt(string1, defaultAnswer1);
	var question1a = prompt(string2, defaultAnswer2);
	if (question1 === question1a) {
		alert("The strings you entered are identical.");
	} 
}

function chap11a() {
	var string1 = "Enter a string.";
	var defaultAnswer1 = "Enter string here."
	var string2 = "Enter a second string.";
	var defaultAnswer2 = "Enter string here."
	var question1 = prompt(string1, defaultAnswer1);
	var question1a = prompt(string2, defaultAnswer2);
	if (question1 !== question1a) {
		alert("The strings you entered are not identical.");
	} 
}

function chap12() {
	var string1 = "Enter a string.";
	var defaultAnswer1 = "Enter string here."
	var string2 = "Enter a second string.";
	var defaultAnswer2 = "Enter string here."
	var question1 = prompt(string1, defaultAnswer1);
	var question1a = prompt(string2, defaultAnswer2);
	if (question1 === question1a) {
		alert("The strings you entered are identical.");
	} else {
		alert("The strings you entered are not identical.");
	}
}

function chap13() {
	var num1 = "Enter a number.";
	var defaultNum1 = "Enter number here."
	var num2 = "Enter a second number.";
	var defaultNum2 = "Enter number here."
	var question1 = prompt(num1, defaultNum1);
	var question1a = prompt(num2, defaultNum2);
	if (question1 < question1a && question1 < 10) {
		alert("The first number you entered is less than 10 and is smaller than the second.");
	} else if (question1 == question1a && question1 < 10) {
		alert("The numbers you entered are identical and both are less than 10.");
	} else if (question1 == question1a && question1 > 10) {
		alert("The numbers you entered are identical and both are greater than 10.");
	} else if (question1 == question1a && question1 == 10) {
		alert("The numbers you entered are identical and each is 10.");
	} else {
		alert("The first number you entered is greater than 10 and is larger than the second.");
	}
}

function chap14() {
	var num1 = prompt("Enter a number.");
	var num2 = prompt("Enter another number.");
	var num3 = prompt("Enter a third number.");
	
	if (num1 % 2 == 0){
		if (num2 % 2 == 0) {
			if (num3 % 2 == 0) {
				alert("All the numbers you entered were even. That's odd!");
			}
		}
	} else {
		alert("Nothing remarkable here.");
	}	
}

function chap15() {
	var query = "Enter an index number from 0-6";
	var defaultAnswer = "Enter a number from 0-6";
	var question = prompt(query, defaultAnswer);
	var userInput = parseInt(question);
	var array1 = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"];
	alert("The value stored in that index is " + array1[userInput] + ".");
}

function chap16(){
	var array1 = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"];
	alert("The length of array1 is " + array1.length + ".");
}

function chap16a(){
	var array1 = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"];
	array1.pop();
	alert("The new length of array1 is " + array1.length + ".");
}

function chap16b(){
	var array1 = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"];
	var goByeBye = array1.pop();
	array1.push(goByeBye);
	alert("The new length of array1 is " + array1.length + " and we returned " + goByeBye + " to the end of the array" + ".");
}

function chap17() {
	var cars = ["Ferrari", "Lamborghini", "Porsche", "MacLaren", "Pagani"];
	var goByeBye = cars.shift();
	alert(cars[0] + " , " + cars[1] + " , " + cars[2] + " , " + cars[3]);
}

function chap17a() {
	var cars = ["Ferrari", "Lamborghini", "Porsche", "MacLaren", "Pagani"];
	cars.unshift("Aston Martin", "Lotus");
	alert(cars[0] + " , " + cars[1] + " , " + cars[2] + " , " + cars[3] + " , " + cars[4] + " , " + cars[5]);
}

function chap17b() {
	var cars = ["Ferrari", "Lamborghini", "Porsche", "MacLaren", "Pagani"];
	cars.splice(1, 1, "Aston Martin", "Lotus");
	alert(cars[0] + " , " + cars[1] + " , " + cars[2] + " , " + cars[3] + " , " + cars[4]);
}

function chap17c() {
	var cars = ["Ferrari", "Lamborghini", "Porsche", "MacLaren", "Pagani"];
	var newCars = cars.slice(0, 2);
	alert(newCars[0] + ", " + newCars[1]);
}

function chap18() {
	var cars = ["Ferrari", "Lamborghini", "Porsche", "MacLaren", "Pagani"];
	var query = prompt("Enter an exotic car brand", "Enter here");
	for(var i=0; i<=4; i++) {
		if(query===cars[i]) {
			alert("It's on the list!");
		} 
	}
}

function chap19() {
	var matchFound = false;
	var cars = ["Ferrari", "Lamborghini", "Porsche", "MacLaren", "Pagani"];
	var query = prompt("Enter an exotic car brand", "Enter here");
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

function chap20()  {
	   var fNames = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"];
	   var lNames = ["Earth", "Wind", "Fire", "Water"];
	   var bandNames = [];
	   for(var i=0; i < fNames.length; i++) {
	     for(var j=0; j < lNames.length; j++) {
		   bandNames.push(fNames[i] + lNames[j]);
		 }
	   }
		alert(bandNames[0] + ", " + bandNames[1] + ", " + bandNames[2] + ", " + bandNames[3] + ", " + bandNames[4] + ", " + bandNames[5] + ", " + 
			bandNames[6] + ", " + bandNames[7] + ", " + bandNames[8] + ", " + bandNames[9] + ", " + bandNames[10] + ", " + bandNames[11] + ", " + 
			bandNames[12] + ", " + bandNames[13] + ", " + bandNames[14] + ", " + bandNames[15] + ", " + bandNames[16] + ", " + bandNames[17] + ", " + 
			bandNames[18] + ", " + bandNames[19] + ", " + bandNames[20] + ", " + bandNames[21] + ", " + bandNames[22] + ", " + bandNames[23] + ", " + 
			bandNames[24] + ", " + bandNames[25] + ", " + bandNames[26] + ", " + bandNames[27]);
}
function chap81() {
	var testPop = window.open("", "", "width=100,height=100");
	if (testPop === null) {
		alert("Please disable your popup blocker.");
	}
	testPop.close();
}

function chap82() {
	if (document.getElementById("last_name").value.length === 0) {
		alert("Please enter your last name.");
		return false;
	}
}

function chap83(selection) {
	var target = document.getElementById(selection);
	if (target.selectedIndex === 0) {
		alert("Please select a color");
		return false;
	}
}

function chap84() {
	var target = document.getElementsByName("r84");
	for (var i = 0; i < target.length; i++) {
		if (target[i].checked) {
			return true;
		}
	}
	alert("Please select a color.");
	return false;
}

function chap85() {
	var valueEntered = document.getElementById("zip").value;
	var numChars = valueEntered.length;
	if (numChars < 5 || numChars > 5) {
		alert("Please enter a 5-digit code.");
		return false;
	}
	for (var i = 0; i <=4; i++) {
		var thisChar = parseInt(valueEntered[i]);
			if(isNaN(thisChar)) {
				alert("Please enter numbers only.");
				return false;
			}
	}
}

function chap86() {
	var addrIsLegal = true;
	var userEmail = document.getElementById("email").value;
	if (userEmail.indexOf(" ") !== -1) {
		addrIsLegal = false;
	}
	if (userEmail.indexOf("@") < 1 || userEmail.indexOf("@") > userEmail.length - 5) {
		addrIsLegal = false;
	}
	if (userEmail.indexOf(".") - userEmail.indexOf("@") < 2 || userEmail.indexOf(".") > userEmail.length - 3) {
		addrIsLegal = false;
	}
	if (addrIsLegal === false) {
		alert("That is not a valid Email address.");
		return false;
	}
}

function chap87() {
	try {
		aler("This is an intentional mistake!");
	}
	catch(error) {
		alert(error);
	}	
}

function chap88() {
	try {
		var word = document.getElementById("bigWord").value;
		if (word.length < 8) {
			throw "Please enter a longer word.";
		}
	}
	catch(err) {
		alert(err);		
	}
}

var button1 = document.getElementById("ch89");
button1.onclick = chap89;

function chap89() {
	try {
		aler("This is an intentional mistake!");
	}
	catch(error) {
		alert(error);
	}
}
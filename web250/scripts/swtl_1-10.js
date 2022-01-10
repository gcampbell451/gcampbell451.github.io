function chap1() {
	alert("No problem too small, no solution too big!");
}

function chap2() {
	var name = "Gregory";
	alert(name);
}

function chap2b() {
	var name = "Gregory";
	name = "Steve";
	alert(name);
}

function chap3() {
	var num = 1974;
	alert(num + 46);
}

function chap3a() {
	var num = 1974;
	alert(num + num);
}

function chap5() {
	var num = 1900;
	alert(num + 74);
}

function chap5b() {
	var num = 1900;
	alert(num + num);
}

function chap6() {
	var num = 1;
	var newNum = num++;
	alert(newNum);
}

function chap6b() {
	var num = 1;
	var newNum = ++num;
	alert(newNum);
}

function chap7() {
	var num = (2 + 2) * 4;
	alert(num);
}

function chap7b() {
	var num = 2 + (2 * 4);
	alert(num);
}

function chap8() {
	var message = "Hi, ";
	var exclam = "!";
	alert(message + "(Your name here)" + exclam);
}

function chap9() {
	var question1 = prompt("Do you like dogs?", "Yes!");
}

function chap9b() {
	var query = "Do you like cats?";
	var defaultAnswer = "But of course!";
	var question2 = prompt(query, defaultAnswer);
}

function chap10() {
	var query = prompt("Is the sky blue?", "yes");
	if(query === "yes") {
		alert("Correct!");
	} else {
		alert("Incorrect");
	}
}
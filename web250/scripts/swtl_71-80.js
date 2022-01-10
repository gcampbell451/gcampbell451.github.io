function chap71() {
	var newObject = {
		name: "setFullYear()",
		example: "x.setFullYear(2021)",
		result: "Year of x is 2021",
		write: function() {
			var writeToPage = document.getElementById("write71");
			writeToPage.innerHTML = "The name of the first method in the table is " + newObject.name + ".";
		}
	};
	newObject.write();
}

function chap72() {
	function Method(name, example, result) {
		this.name = name;
		this.example = example;
		this.result = result;
	}
	var method1 = new Method("setFullYear()", "x.setFullYear(2021)", "Year of x is 2021");
	var method2 = new Method("setMonth()", "x.setMonth(0)", "Month of x is January");
	var method3 = new Method("setDate()", "x.setDate(1)", "Day of the month is 1");
	var method4 = new Method("setHours()", "x.setHours(0)", "Midnight");
	var method5 = new Method("setMinutes()", "x.setMinutes(1)", "One minute past the hour");
	var method6 = new Method("setSeconds()", "x.setSeconds(1)", "One second past the minute");
	var method7 = new Method("setMilliseconds()", "x.setMilliseconds(1)", "One ms past the second");
	
	var writeToPage = document.getElementById("write72");
	writeToPage.innerHTML = "The last method in the list is " + method7.name + ".";
}

function chap73() {
	function Method(name, example, result) {
		this.name = name;
		this.example = example;
		this.result = result;
		this.write = function() {
						alert("The name of the first method in the list is " + this.name);
					 };
	}
	var method1 = new Method("setFullYear()", "x.setFullYear(2021)", "Year of x is 2021");
	var method2 = new Method("setMonth()", "x.setMonth(0)", "Month of x is January");
	var method3 = new Method("setDate()", "x.setDate(1)", "Day of the month is 1");
	var method4 = new Method("setHours()", "x.setHours(0)", "Midnight");
	var method5 = new Method("setMinutes()", "x.setMinutes(1)", "One minute past the hour");
	var method6 = new Method("setSeconds()", "x.setSeconds(1)", "One second past the minute");
	var method7 = new Method("setMilliseconds()", "x.setMilliseconds(1)", "One ms past the second");
	var writeToPage = document.getElementById("write73");
	writeToPage.innerHTML = method1.write();
	
}

function chap74() {
	function Method(name, example, result) {
		this.name = name;
		this.example = example;
		this.result = result;
	}
	Method.prototype.write = function() {
								alert("The name of the first method in the list is " + this.name);
							 };
							 
	var method1 = new Method("setFullYear()", "x.setFullYear(2021)", "Year of x is 2021");
	var method2 = new Method("setMonth()", "x.setMonth(0)", "Month of x is January");
	var method3 = new Method("setDate()", "x.setDate(1)", "Day of the month is 1");
	var method4 = new Method("setHours()", "x.setHours(0)", "Midnight");
	var method5 = new Method("setMinutes()", "x.setMinutes(1)", "One minute past the hour");
	var method6 = new Method("setSeconds()", "x.setSeconds(1)", "One second past the minute");
	var method7 = new Method("setMilliseconds()", "x.setMilliseconds(1)", "One ms past the second");

	var writeToPage = document.getElementById("write74");
	writeToPage.innerHTML = method1.write();
}

function chap74a() {
	function Method(name, example, result) {
		this.name = name;
		this.example = example;
		this.result = result;
	}
	Method.prototype.exists = true;
							 
	var method1 = new Method("setFullYear()", "x.setFullYear(2021)", "Year of x is 2021");
	var method2 = new Method("setMonth()", "x.setMonth(0)", "Month of x is January");
	var method3 = new Method("setDate()", "x.setDate(1)", "Day of the month is 1");
	var method4 = new Method("setHours()", "x.setHours(0)", "Midnight");
	var method5 = new Method("setMinutes()", "x.setMinutes(1)", "One minute past the hour");
	var method6 = new Method("setSeconds()", "x.setSeconds(1)", "One second past the minute");
	var method7 = new Method("setMilliseconds()", "x.setMilliseconds(1)", "One ms past the second");
	var writeToPage = document.getElementById("write74");
	writeToPage.innerHTML = "The property 'exists' has a value of " + method1.exists + ".";

}

function chap75() {
	var newObject = {
		name: "setFullYear()",
		example: "x.setFullYear()",
		result: "Year of x is 2021"
	}
	var propList = [];
	for (var i in newObject){
		propList.push(i);
	}
	var writeToPage = document.getElementById("write75");
	writeToPage.innerHTML = "The properties of newObject are " + propList[0] + ", " + propList[1] + ", and " + propList[2] + ".";
}

function chap75a() {
	function Method(name, example, result) {
		this.name = name;
		this.example = example;
		this.result = result;
	}
	var newObject = new Method("setFullYear()", "x.setFullYear(2021)", "Year of x is 2021");
	Method.prototype.exists = true;
	var propList = [];
	for (var i in newObject){
		propList.push(i);
	}
	var writeToPage = document.getElementById("write75a");
	writeToPage.innerHTML = "The properties of newObject are " + propList[0] + ", " + propList[1] + ", " + propList[2] + ", and " + propList[3] + ".";
}

function chap75b() {
	function Method(name, example, result) {
		this.name = name;
		this.example = example;
		this.result = result;
	}
	var newObject = new Method("setFullYear()", "x.setFullYear(2021)", "Year of x is 2021");
	Method.prototype.exists = true;
	var propList = [];
	for (var i in newObject) {
		if (newObject.hasOwnProperty(i)) {
			propList.push(i);
		}
	}
	var writeToPage = document.getElementById("write75b");
	writeToPage.innerHTML = "The properties of newObject are " + propList[0] + ", " + propList[1] + ", and " + propList[2] + ".";
}

function chap76() {
	var theURL = window.location.href;
	var writeToPage = document.getElementById("write76");
	writeToPage.innerHTML = "The current URL is " + theURL + ".";
}

function chap76a() {
	var theHost = window.location.hostname;
	var writeToPage = document.getElementById("write76a");
	writeToPage.innerHTML = "The domain name is " + theHost + ".";
}

function chap76b() {
	var thePath = window.location.pathname;
	var writeToPage = document.getElementById("write76b");
	writeToPage.innerHTML = "The path is " + thePath + ".";
}

function chap76c() {
	var theHash = window.location.hash;
	var writeToPage = document.getElementById("write76c");
	writeToPage.innerHTML = "The hash is " + theHash + ".";
}

function chap76d() {
	window.location.href="https://www.cpcc.edu/"; 
}

function chap76e() {
	var currentSite = window.location.hostname;
	var destination = "http://" + currentSite + "/introduction.html";
	window.location.href = destination;
}

function chap77()  {
	window.location.assign("http://www.cpcc.edu");
}

function chap77a()  {
	window.location.replace("http://www.wikipedia.com");
}

function chap77b()  {
	window.location.reload();
}

function chap78()  {
	history.back();
}

function chap78a()  {
	history.forward();
}

function chap78b()  {
	history.go(-2);
}

function chap79()  {
	var popup = window.open();
	var content = "<h1>My Cute Cats!</h1><img src='images/cats.jpg' width='600'>";
	popup.document.write(content);
}

function chap80()  {
	var popup = window.open("","newPopup","width=800,height=600,left=50,top=50");
	var content = "<h1>My Cute Cats!</h1><img src='images/cats.jpg' width='500'>";
	popup.document.write(content);
}
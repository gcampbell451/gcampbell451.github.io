function chap61() {
	var a = document.getElementById("Ch61");
	var pCounter = 0;
	for (var i = 0; i < a.childNodes.length; i++) {
		if (a.childNodes[i].nodeType === 1) {
			pCounter++;
		}
		if (pCounter === 2) {
				var imgs = a.childNodes[i];
				imgs.style.border = "5px solid #99BADD";
				break;
		}
	}
}

function chap62() {
	var a = document.getElementById("Ch62");
	var imgs = a.firstChild;
	imgs.style.border = "5px solid #99BADD";
}

function chap62a() {
	var a = document.getElementById("Ch62");
	var imgs = a.lastChild;
	imgs.style.border = "5px solid #99BADD";
}

function chap63() {
	var target = document.getElementById("ch63table");
	var nName = target.nodeName;
	var writeToPage = document.getElementById("write63");
	writeToPage.innerHTML = "The nodeName of the table is " + nName +".";
}

function chap63a() {
	var target = document.getElementById("ch63table");
	var nName = target.nodeValue;
	var writeToPage = document.getElementById("write63a");
	writeToPage.innerHTML = "The nodeValue of the table is " + nName +".";
}

function chap64() {
	var parentNode = document.getElementById("Ch64");
	var numImgs = parentNode.childNodes.length;
	var writeToPage = document.getElementById("write64");
	writeToPage.innerHTML = "There are  " + numImgs +" pictures of cute kitties in Chapter 64.";	
}

function chap65() {
	var target = document.getElementById("Chap65");
	target.setAttribute("src", "images/cats2.jpg");
}

function chap65a() {
	var target = document.getElementById("Chap65");
	target.setAttribute("src", "images/cats.jpg");
}

function chap66() {
	var numAttributes = document.getElementById("Ch66").attributes.length;
	var writeToPage = document.getElementById("write66");
	writeToPage.innerHTML = "The image has " + numAttributes + " attributes.";
}

function chap66a() {
	var attributeVals = document.getElementById("Ch66").attributes;
	var writeToPage = document.getElementById("write66a");
	writeToPage.innerHTML = "The image's attributes, in order, are: " + attributeVals[0].nodeName + ", " +  attributeVals[1].nodeName + ", "
		+  attributeVals[2].nodeName + ", " +  attributeVals[3].nodeName + ", " +  attributeVals[4].nodeName + ", and " +  attributeVals[5].nodeName + ".";
}

function chap66b() {
	var attributeVals = document.getElementById("Ch66").attributes;
	var writeToPage = document.getElementById("write66b");
	writeToPage.innerHTML = "Those attribute values, in order, are: " + attributeVals[0].nodeValue + ", " +  attributeVals[1].nodeValue + ", "
		+  attributeVals[2].nodeValue + ", " +  attributeVals[3].nodeValue + ", " +  attributeVals[4].nodeValue + ", and " +  attributeVals[5].nodeValue + ".";
}

function chap68() {
	var parentDiv = document.getElementById("Ch68");
	var newPara = document.createElement("p");
	var newText = document.createTextNode("But I happen to be right!");
	newPara.appendChild(newText);
	parentDiv.appendChild(newPara);
}

function chap68a() {
	var parentDiv = document.getElementById("Ch68");
	var newImg = document.createElement("img");
	newImg.setAttribute("src", "images/cats2.jpg");
	newImg.setAttribute("width", "600");
	newImg.setAttribute("class", "center");
	para1 = parentDiv.firstChild;
	parentDiv.insertBefore(newImg, para1);
}

function chap69() {
	var newObject = {
		name: "setFullYear()",
		example: "x.setFullYear()",
		result: "Year of x is 2021"
	};
	var writeToPage = document.getElementById("write69");
	writeToPage.innerHTML = "The name of the first method in the table is " + newObject.name + ".";
}

function chap70() {
	var newObject = {
		name: "setFullYear()",
		example: "x.setFullYear()",
		result: "Year of x is 2021"
	};
	var propertyExists = "name" in newObject;
	var writeToPage = document.getElementById("write70");
	if (propertyExists == true)
		writeToPage.innerHTML = "The property 'name' does in fact exist in newObject.";
}
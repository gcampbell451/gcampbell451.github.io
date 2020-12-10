function chap51() {
	document.getElementById("chap51").innerHTML = "I, Gregory C. Campbell, agree to abide by the terms in my Fall 2020 WEB115 Web Markup and Scripting class with my instructor, D.I. von Briesen. I understand that all work I do on my school and personal websites will be publicly available to the world. I will not put information there that is inappropriate for schoolwork, or that I wish to keep private. I also understand that it is my work that counts for attendance, not logins or showing up for class. As such failure to turn in assignments may show as an absence. Signed, Gregory C. Campbell, 10 August 2020.";
}

function chap52() {
	document.getElementById("chap52").className = "hidden";
}

function chap53(eId, newPic) {
	document.getElementById(eId).src = newPic;
}

function chap54(eId, newPic) {
	var a = document.getElementById(eId);
	a.src = newPic;
}

function chap55() {
	document.getElementById("chap55").style.border = "2px solid #99BADD";
}

function chap56() {
	var h3 = document.getElementsByTagName("h3");
	for (var i = 0; i < h3.length; i++) {
		h3[i].style.fontSize = "3em";
	}
}

function chap57() {
	var a = document.getElementById("Ch57");
	var imgs = a.getElementsByTagName("img");
	imgs[1].style.border = "5px solid #99BADD";
}

function chap60() {
	var a = document.getElementById("Ch60");
	var imgs = a.childNodes[8];
	imgs.style.border = "5px solid #99BADD";	
}
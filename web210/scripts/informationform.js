function infoForm() {
	// collect user input into variables
	var fname = document.getElementById("first_name").value;
	var mname = document.getElementById("middle_initial").value;
	var lname = document.getElementById("last_name").value;
	var userImg = document.getElementById("pic").value;
	var cap = document.getElementById("figcaption").value;
	var perBack = document.getElementById("personal").value;
	var proBack = document.getElementById("professional").value;
	var acaBack = document.getElementById("academic").value;
	var cpuBack = document.getElementById("platform").value;
	var course1 = document.getElementById("course1").value;
	var course2 = document.getElementById("course2").value;
	var course3 = document.getElementById("course3").value;
	var course1why = document.getElementById("course1why").value;
	var course2why = document.getElementById("course2why").value;
	var course3why = document.getElementById("course3why").value;
	var remember = document.getElementById("remember").value;
	var share = document.getElementById("share").value;
	
	// display user information
	if (mname !== "") {
		document.getElementById("userName").innerHTML = "Name: " + fname + " " + mname + ". " + lname;
	} else {
		document.getElementById("userName").innerHTML = "Name: " + fname + " " + lname;		
	}
	

	// display user picture
	var imgNodeToAdd = document.createElement("img");
	imgNodeToAdd.setAttribute("src", userImg);
	imgNodeToAdd.setAttribute("width", "600");
	var parentP = document.getElementById("userPic");
	parentP.appendChild(imgNodeToAdd);
	document.getElementById("userCap").innerHTML = cap;
	
	document.getElementById("userPersonal").innerHTML = "Personal Background: " + perBack;
	document.getElementById("userProfessional").innerHTML = "Professional Background: " + proBack;
	document.getElementById("userAcademic").innerHTML = "Academic Background: " + acaBack;
	document.getElementById("userPlatform").innerHTML = "Primary Computer Platform: " + cpuBack;
	document.getElementById("courses").innerHTML = "Your courses and why you're taking them: <br>" + "<ul><li>" + course1 + "&mdash;" + course1why + "</li><br><li>" + course2 + "&mdash;" + course2why + "</li><br><li>" + course3 + "&mdash;" + course3why + "</li></ul>";		
	document.getElementById("userRemember").innerHTML = "Something to Remember Me By: " + remember;
	document.getElementById("userShare").innerHTML = "I'd Also Like to Share: " + share;

}

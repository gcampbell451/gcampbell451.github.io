function createForm() {
    var intro = "Introduction"
    var fName = document.getElementById("fName").value;
    var lName = document.getElementById("lName").value;
    var personalBackground = document.getElementById("personalBackground").value;
    var professionalBackground = document.getElementById("professionalBackground").value;
    var academicBackground = document.getElementById("academicBackground").value;
    var backgroundInSubject = document.getElementById("backgroundInSubject").value;
    var primaryPlatform = document.getElementById("primaryPlatform").value;
    var courses = document.getElementById("courses").value;
    var interesting = document.getElementById("interesting").value;

    document.getElementById("intro").innerHTML = intro
    document.getElementById("nameOut").innerHTML = "Name: " + fName + " " + lName;
    document.getElementById("personalBackgroundOut").innerHTML = "Personal Background: " + personalBackground;
    document.getElementById("professionalBackgroundOut").innerHTML = "Professional Background: " + professionalBackground
    document.getElementById("academicBackgroundOut").innerHTML = "Academic Background: " + academicBackground
    document.getElementById("backgroundInSubjectOut").innerHTML = "Background in This Subject: " + backgroundInSubject;
    document.getElementById("primaryPlatformOut").innerHTML = "Primary Computer Platform: " + primaryPlatform
    document.getElementById("coursesOut").innerHTML = "Courses I'm Taking & Why: " + courses;
    document.getElementById("interestingOut").innerHTML = "Funny/Interesting Item About Yourself: " + interesting;
}
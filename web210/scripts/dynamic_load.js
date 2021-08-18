if (document.addEventListener) {
  document.addEventListener("DOMContentLoaded", function(){load_home(null, 'pages/home.html');}, false);
}

function load_home (e, file) {
    (e || window.event).preventDefault(); // prevents anchor doing its thing
    var con = document.getElementById('page-loader'), // assigns page-loader to con   
    xhr = new XMLHttpRequest(); // assigns a new HTTP request to xhr
    xhr.onreadystatechange = function (e) { 
      if (xhr.readyState == 4 /*&& xhr.status == 200*/) {
        con.innerHTML = xhr.responseText;
      }
    }
  
    xhr.open("GET", file);
    xhr.setRequestHeader('Content-type', 'text/html');
    xhr.send();
  }
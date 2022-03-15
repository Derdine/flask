var livebutton = document.getElementById("livebutton");
var readybutton = document.getElementById("readybutton");
var breakbutton = document.getElementById("breakbutton");
var logmebutton = document.getElementById("logmebutton");
var meterbutton = document.getElementById("meterbutton");

var meter = 0

var http_request = function(url,element){
    var http = new XMLHttpRequest();
    http.open("GET", url, true);
    http.send();
    http.onreadystatechange = function() {
        console.log(http.responseText)
        if (this.status == 200) {
            document.getElementById(element).innerHTML = "OK";
        }
        else {
            document.getElementById(element).innerHTML = "Error " + this.status;
        }
    };
}


livebutton.onclick = function(){
    http_request("http://127.0.0.1:5000/health","liveres")
}

readybutton.onclick = function(){
    http_request("http://127.0.0.1:5000/readiness","readyres")
}

breakbutton.onclick = function(){
    if(document.getElementById("breakres").innerHTML.includes("DOWN")) {
    document.getElementById("breakres").innerHTML = "Server UP"
}
    else {
    document.getElementById("breakres").innerHTML = "Server DOWN"
    }
}

logmebutton.onclick = function(){
    document.getElementById("logmeres").innerHTML = "Check Console"
}

meterbutton.onclick = function(){
    meter = meter + 1
    document.getElementById("meterres").innerHTML = meter
}
var toggled = false;
var blocked = false;
var prevClock = "00:10:00";
var running = false;
var timeLeft = 0;
var interval = null;
var locked = false;
var changed = true;
var focusToggled = false;
var focusAnimating = false;

document.onkeypress = function (e) {
    e = e || window.event;
    var charCode = e.keyCode || e.which;
    // 13 is the enter button lol
    if(charCode == 13){
    	cleanTitle();
    	document.getElementById("title-text").blur();
    	document.getElementById("clock-time").blur();
    // this is 'F'
    }else if(charCode == 102){
    	focusScreen();
    }else{
    	titleChange();
    }
};

function focusScreen(){
	if(focusAnimating)
		return
	if(focusToggled){
		focusToggled = false;
		focusAnimating = true;
		var navbar = document.getElementById('nav-bar');
		var link = document.getElementById('left');
		var info = document.getElementById('right');
		var background = document.getElementById('background-div');
		var clkBackground = document.getElementById('clock-back');
		Velocity(navbar, { opacity: 1}, { duration: 1000 });
		Velocity(link, { opacity: 1}, { duration: 1000 });
		Velocity(info, { opacity: 1}, { duration: 1000 });
		Velocity(background, { blur: 0}, { duration: 1000 });
		Velocity(clkBackground, { opacity: 0.2}, { duration: 1000 });
		setTimeout(function(){ focusAnimating = false }, 1200);
	}else{
		focusToggled = true;
		focusAnimating = true;
		var navbar = document.getElementById('nav-bar');
		var link = document.getElementById('left');
		var info = document.getElementById('right');
		var background = document.getElementById('background-div');
		var clkBackground = document.getElementById('clock-back');
		Velocity(navbar, { opacity: 0}, { duration: 1000 });
		Velocity(link, { opacity: 0}, { duration: 1000 });
		Velocity(info, { opacity: 0}, { duration: 1000 });
		Velocity(background, { blur: 3}, { duration: 1000 });
		Velocity(clkBackground, { opacity: 0.4}, { duration: 1000 });
		setTimeout(function(){ focusAnimating = false }, 1200);
	}
}

function toggle(){
	if(blocked)
		return;
	toggled = !toggled;
	var element = document.getElementById("url_link");
	var url = getURL();
	animationTime = 500;
	if(toggled){
		blocked = true;
		element.value = url;
		Velocity(element, { width: 200}, { duration: 500 });
		setTimeout(function(){ blocked = false }, 500);
	}else{
		blocked = true;
		Velocity(element, { width: 0}, { duration: 500 });
		setTimeout(function(){ blocked = false }, 500);
	}
}

function closeLink(){
	if(toggled){
		toggle();
	}
}

function titleFocus(){
	closeLink();
	pauseClock();
}

function cleanTitle(){
	var title = document.getElementById("title-text").innerHTML;
	title = title.replace(/\<[^\<\>]*\>/g," ");
	document.getElementById("title-text").innerHTML = title;
}
function titleChange(){
	updateClockPosition();
}
function getURL(){
	var base = window.location.href;
	base = base.split("?")[0];
	var url = base+"?";
	url += "title="+document.getElementById("title-text").innerHTML;
	url += "&time="+document.getElementById("clock-time").innerHTML;
	url = encodeURI(url);
	return url;	
}

function setDefaults(){
	getBackgroundImage();
	var base = window.location.href;
	var args = [];
	if (base.includes("?")){
		base = base.split("?")[1];
		if(base.includes("&"))
			args = base.split("&");
		else
			args.push(base)
	}
	var title = null;
	var time = null;
	for (var i = 0; i < args.length; i++) {
		if(args[i].split("=")[0] == "title")
			title = decodeURI(args[i].split("=")[1]);
		if(args[i].split("=")[0] == "time")
			time = decodeURI(args[i].split("=")[1]);
	}
	if(title != null)
		document.getElementById("title-text").innerHTML = title;
	else
		document.getElementById("title-text").innerHTML = "Timer App";
	if(time != null)
		document.getElementById("clock-time").innerHTML = time;
	else
		document.getElementById("clock-time").innerHTML = "00:10:00";

	updateClockPosition();
	originalTitleHeight = document.getElementById("title-text").offsetHeight;
	prevTitle = document.getElementById("title-text").innerHTML;
}
function updateClockPosition(event) {
	orientError();
    orientClock()
    orientTitle();
    orientUI();
};

function orientError(){
	var err = document.getElementById("error-container");
    err.style.left = (Math.floor(document.documentElement.clientWidth/2)-Math.floor(err.offsetWidth/2))+"px";
}
function orientUI(){
	var title = document.getElementById("title-text");
	var titleLeft = parseInt(title.style.left.match(/\d+/));
	var titleTop = parseInt(title.style.top.match(/\d+/));
	var ul = document.getElementById("title-underline");
	var ulLeft = parseInt(ul.style.left.match(/\d+/));
	var ulTop = parseInt(ul.style.top.match(/\d+/));
	var btnTop = ulTop+ul.offsetHeight+40;
	btnTop+="px"
    var start = document.getElementById("startBtn");
    start.style.top = btnTop;
    start.style.left = (ulLeft - (start.offsetWidth/2))+"px";
    var pause = document.getElementById("pauseBtn");
    pause.style.top = btnTop;
    pause.style.left = (ulLeft + ul.offsetWidth - (pause.offsetWidth/2))+"px";
    var reset = document.getElementById("resetBtn");
    reset.style.top = btnTop;
    reset.style.left = (ulLeft + (ul.offsetWidth/2) - (reset.offsetWidth/2))+"px";
}
function orientClock(){
    var back = document.getElementById("clock-svg");
    back.style.left = (Math.floor(document.documentElement.clientWidth/2)-150)+"px";
    var backTop = (Math.floor(document.documentElement.clientHeight/2)-150+50);
    back.style.top = backTop+"px";
    var time = document.getElementById("clock-time");
    time.style.left = (Math.floor(document.documentElement.clientWidth/2)-Math.floor(time.offsetWidth/2))+"px";
    time.style.top = (backTop+150-Math.floor(time.offsetHeight/2))+"px";
}
function orientTitle(){
    var title = document.getElementById("title-text");
    title.style.top = (document.documentElement.clientHeight/10)+ "px";
    title.style.left = (Math.floor(document.documentElement.clientWidth/2)-Math.floor(title.offsetWidth/2))+"px";
    var underline = document.getElementById("title-underline");
    underline.style.top = (parseInt(title.style.top.match(/\d+/))+title.offsetHeight/2 + 5)+"px";
    underline.style.width = title.offsetWidth+"px";
    underline.style.left = (Math.floor(document.documentElement.clientWidth/2)-Math.floor(underline.offsetWidth/2))+"px";
}
window.onresize = updateClockPosition;


function clockTimeBlur(){
	// clear any errors
	removeError();
	// check if nothing changed
	var elem = document.getElementById("clock-time");
	if(elem.innerHTML == prevClock)
		return;
	changed = true;
	// validate that it's correct here
	// if time is not valid, raise error and default to 10:00:00
	// this should enforce that whenever start is clicked the time
	// is valid. 
	var re = /\d+\:\d+\:\d+/g;
	var res = elem.innerHTML.match(re);
	if(elem.innerHTML.length == 0 || res == null){
		elem.innerHTML = prevClock;
		raiseError("Sorry! I can only really understand times in the format HH:MM:SS");
	}else{
		prevClock = elem.innerHTML;
	}
	// update the position in case the string changed
	updateClockPosition(null);
}

function clockTimeFocus(){
	// clear any errors
	removeError();
	// this should just pause the clock
	// if it's not already paused/stopped
	pauseClock();
}

function startClock(){
	if(running)
		return;
	if(!changed){
		if(!locked){
			running = true;
			interval = setInterval(progressClock, 1000);
		}
		return;
	}
	// clear any errors
	removeError();
	// get the time left
	var time = document.getElementById('clock-time').innerHTML.split(':');
	var hours = parseInt(time[0]);
	var minutes = parseInt(time[1]);
	var seconds = parseInt(time[2]);
	timeLeft = 60*60*hours + 60*minutes + seconds;
	// activate the interrupt
	running = true;
	changed = false;
	locked = false;
	original = timeLeft;
	interval = setInterval(progressClock, 1000);
}

function resetClock(){
	// stop the clock
	stopClock();
	// clear any errors
	removeError();
	// reset globals
	running = false;
	changed = true;
	locked = false;
	timeLeft = original+1;
	// update how the clock looks
	progressClock();
}

function progressClock(){
	if(timeLeft == 0){
		stopClock();
	}
	else{
		timeLeft-=1;
		updateArcView((360 - ((timeLeft/original) * 360)), "rgba(17,190,242,0.7)");
		var hours = Math.floor(timeLeft/3600);
		if(hours < 10)
			hours = "0"+hours;
		var minutes = Math.floor((timeLeft - hours*3600)/60);
		if(minutes < 10)
			minutes = "0"+minutes;
		var seconds = timeLeft - minutes*60;
		if(seconds < 10)
			seconds = "0"+seconds;
		document.getElementById('clock-time').innerHTML = hours+":"+minutes+":"+seconds;
	}
}

function pauseClock(){
	if(running){
		running = false;
		clearInterval(interval);
		interval = null;
		prevClock = document.getElementById('clock-time').innerHTML;
	}
}

function stopClock(){
	if (running){
		running = false;
		clearInterval(interval);
		interval = null;
		locked = true;
		prevClock = document.getElementById('clock-time').innerHTML;
	}
}

function raiseError(msg){
	// remove any previous errors
	removeError();
	// add the message
	var elem = document.getElementById("error-container");
	elem.innerHTML = msg;
	// update it's position
	updateClockPosition(null);
	// animate
	Velocity(elem, { top: "80%"}, { duration: 200 });
}

function removeError(){
	var elem = document.getElementById("error-container");
	Velocity(elem, "stop");
	// removes any error message that might be up
	elem.style.top = "100%";
}
function toRadians (angle) {
  return angle * (Math.PI / 180);
}

function updateArcView(angle, col){
	// reset. 
	setArcOne(0,col)
	setArcTwo(90,col)
	setArcThree(180,col)
	setArcFour(270,col)
	if(angle <= 90){
		setArcOne(angle,col);
	}else if(angle > 90 && angle <= 180){
		setArcOne(90,col);
		setArcTwo(angle,col);
	}else if(angle > 180 && angle <= 270){
		setArcOne(90,col);
		setArcTwo(180,col);
		setArcThree(angle,col)
	}else{
		setArcOne(90,col);
		setArcTwo(180,col);
		setArcThree(270,col);
		setArcFour(angle,col);
	}
}

function setArcOne(angle, col){
	var arc1 = document.getElementById("arc1");
	arc1.setAttribute("stroke", col);
	x = 147*Math.sin(toRadians(angle));
	y = 147 - 147*Math.cos(toRadians(angle));
	var newVal = "m150 3 a144 144 0 0 1" +x.toString() +" " + y.toString();
	arc1.setAttribute("d", newVal);
}
function setArcTwo(angle, col){
	var arc2 = document.getElementById("arc2");
	arc2.setAttribute("stroke", col);
	angle = angle - 90;
	x = (147 - 147*Math.cos(toRadians(angle)))*-1;
	y = 147*Math.sin(toRadians(angle));
	var newVal = "m297 150 a144 144 0 0 1 " +x.toString() +" " + y.toString();
	arc2.setAttribute("d", newVal);
}
function setArcThree(angle, col){
	var arc3 = document.getElementById("arc3");
	arc3.setAttribute("stroke", col);
	angle = angle - 180;
	x = 147*Math.sin(toRadians(angle))*-1;
	y = (147-147*Math.cos(toRadians(angle)))*-1;
	var newVal = "m150 297 a144 144 0 0 1 " +x.toString() +" " + y.toString();
	arc3.setAttribute("d", newVal);
}
function setArcFour(angle,col){
	var arc4 = document.getElementById("arc4");
	arc4.setAttribute("stroke", col);
	angle = angle - 270;
	x = 147 - 147*Math.cos(toRadians(angle));
	y = 147*Math.sin(toRadians(angle))*-1;
	var newVal = "m3 150 a144 144 0 0 1 " +x.toString() +" " + y.toString();
	arc4.setAttribute("d", newVal);
}


function getBackgroundImage(){
	var width = document.documentElement.clientWidth;
	var height = document.documentElement.clientHeight;
	var base = window.location.href.split("?")[0];
	var url = base+"imgRequest?w="+width+"&h="+height;
	try{
		httpGetAsync(url,setBackgroundImg);
	}catch(err){
		console.log("Sorry! There was a error getting a background image from the server");
		console.log("Using default backup image...")
		var imgElem = document.getElementById("background-div");
		var imgCreditElem = document.getElementById("img-credit");
		imgCreditElem.href = "https://wallpapersafari.com/free-mountain-wallpaper-backgrounds/";
		imgElem.style.backgroundImage = "url(http://cdn.wallpapersafari.com/17/34/42nLhc.jpg)";
	}
}


function setBackgroundImg(response){
	var imgElem = document.getElementById("background-div");
	var imgCreditElem = document.getElementById("img-credit");
	var img = JSON.parse(response);
	imgCreditElem.href = img.credit;
	imgElem.style.backgroundImage = "url("+img.src+")";
}

/* 
 * This function was taken from stackoverflow
 * via user Joan
 * https://stackoverflow.com/questions/247483/http-get-request-in-javascript
 */
function httpGetAsync(theUrl, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}

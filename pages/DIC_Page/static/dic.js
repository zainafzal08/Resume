var toggled = false;
var blocked = false;
let focusToggled = false;
let focusAnimating = false;

document.onkeypress = handleKeyDown;

function handleKeyDown(e=window.event){
	const charCode = e.keyCode || e.which;
	const bot = document.getElementById("top");
	const top = document.getElementById("bottom");

	// this is 'F'
	if(charCode == 102 && top !== document.activeElement && bot !== document.activeElement){
		focusScreen();
	}
}


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
		Velocity(navbar, { opacity: 1}, { duration: 1000 });
		Velocity(link, { opacity: 1}, { duration: 1000 });
		Velocity(info, { opacity: 1}, { duration: 1000 });
		Velocity(background, { blur: 0}, { duration: 1000 });
		setTimeout(function(){ focusAnimating = false }, 1200);
	}else{
		focusToggled = true;
		focusAnimating = true;
		var navbar = document.getElementById('nav-bar');
		var link = document.getElementById('left');
		var info = document.getElementById('right');
		var background = document.getElementById('background-div');
		Velocity(navbar, { opacity: 0}, { duration: 1000 });
		Velocity(link, { opacity: 0}, { duration: 1000 });
		Velocity(info, { opacity: 0}, { duration: 1000 });
		Velocity(background, { blur: 3}, { duration: 1000 });
		setTimeout(function(){ focusAnimating = false }, 1200);
	}
}

function toggle(){
	if(blocked)
		return
	toggled = !toggled;
	var element = document.getElementById("url_link");
	var url = "";
	var top = document.getElementById("top").value;
	var bot = document.getElementById("bottom").value;
	base = window.location.href;
	base = base.split("?")[0];
	url = base+"?top="+top+"&bot="+bot;
	url = encodeURI(url);
	animationTime = 500;
	if(toggled){
		blocked = true
		element.value = url;
		Velocity(element, { width: 200}, { duration: 500 });
		setTimeout(function(){ blocked = false }, 500);
	}else{
		blocked = true
		Velocity(element, { width: 0}, { duration: 500 });
		setTimeout(function(){ blocked = false }, 500);
	}
}

function closeLink(){
	if(toggled){
		toggle();
	}
}

function getBackgroundImage(){
	var width = document.documentElement.clientWidth;
	var height = document.documentElement.clientHeight;
	var base = window.location.href.split("?")[0];
	var url = base+"imgRequest?w="+width+"&h="+height;
	if(window.location.href.split("?").length == 2 && window.location.href.split("?")[1] == "plain"){
		plainImg();
		return
	}

	try{
		httpGetAsync(url,setBackgroundImg);
	}catch(err){
		fallBackImg();
	}
}

function fallBackImg(){
	console.log("Sorry! There was a error getting a background image from the server");
	console.log("Using default backup image...")
	var imgElem = document.getElementById("background-div");
	var imgCreditElem = document.getElementById("img-credit");
	imgCreditElem.href = "https://wallpapersafari.com/free-mountain-wallpaper-backgrounds/";
	imgElem.style.backgroundImage = "url(http://cdn.wallpapersafari.com/17/34/42nLhc.jpg)";
}

function plainImg(){
	console.log("Getting a plain image because getting a random one is too WILD for you apparently");
	var imgElem = document.getElementById("background-div");
	var imgCreditElem = document.getElementById("img-credit");
	imgCreditElem.href = "https://www.instagram.com/juliamstarr/";
	imgElem.style.backgroundImage = "url(/static/test.jpg)";
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

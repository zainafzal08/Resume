var toggled = false;
var blocked = false;

function toggle(){
	if(blocked)
		return
	toggled = !toggled;
	var element = document.getElementById("url_link");
	var url = "";
	var top = document.getElementById("top").innerHTML;
	var bot = document.getElementById("bottom").innerHTML;
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

function textBlur(elem){
	var title = document.getElementById(elem).innerHTML;
	title = title.replace(/\<[^\<\>]*\>/g," ");
	document.getElementById(elem).innerHTML = title;
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
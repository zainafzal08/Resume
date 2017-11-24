function calcPx(num){
	return num + "px";
}

function initaliseView(prjNum){
	getBackgroundImage();
	calibrateView(prjNum);
}
function calibrateView(prjNum){
	var welcome = document.getElementById('welcome-block');
	var about = document.getElementById('about-block');
	var project = document.getElementById('project-block');
	var aboutSep = document.getElementById('about-block-seperator');
	var projectSep = document.getElementById('project-block-seperator');
	var footer = document.getElementById('footer-block');
	var footerSep = document.getElementById('footer-block-seperator');
	welcome.style.width = calcPx(document.documentElement.clientWidth);
	welcome.style.height = calcPx(document.documentElement.clientHeight);
	about.style.width = calcPx(document.documentElement.clientWidth);
	about.style.height = calcPx(document.documentElement.clientHeight/2);
	aboutSep.style.width = calcPx(document.documentElement.clientWidth);
	projectSep.style.width = calcPx(document.documentElement.clientWidth);
	footerSep.style.width = calcPx(document.documentElement.clientWidth);
	project.style.width = calcPx(document.documentElement.clientWidth);
	alignProjectCards(project, prjNum);
	footer.style.width = calcPx(document.documentElement.clientWidth);
	footer.style.height = calcPx(document.documentElement.clientHeight/10);
}

function alignProjectCards(project, n){
	var i = 0;
	for(i=1;i<=n;i++){
		var base = "project-card-"+i;
		var top = document.getElementById(base+"-container");
		var card = document.getElementById(base)
		var val = Math.floor(top.offsetWidth/2-card.offsetWidth/2);
		if(val < 0)
			val = 0;
		card.style.marginLeft = calcPx(val);
	}

}

function updateNav(){
	var welcome = document.getElementById('welcome-block').getBoundingClientRect().top;
	var about = document.getElementById('about-block').getBoundingClientRect().top;
	var projects = document.getElementById('project-block').getBoundingClientRect().top;
	if(0 < about){
		triggerLightNav()
		focusNav("Home");
	}else if(0 < projects){
		triggerDarkNav();
		focusNav("About");
	}else{
		triggerDarkNav();
		focusNav("Projects");
	}
}

function focusNav(elem){
	document.getElementById("Home").className = "";
	document.getElementById("About").className = "";
	document.getElementById("Projects").className = "";
	document.getElementById(elem).className = "active";
}
function triggerDarkNav(){
	document.getElementById("nav-bar").className = "nav-bar-dark"
}
function triggerLightNav(){
	document.getElementById("nav-bar").className = "nav-bar"
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
		document.getElementById("background-div").className = "background";
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
	imgElem.className = "background";
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
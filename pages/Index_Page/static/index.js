function calcPx(num){
	return num + "px";
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
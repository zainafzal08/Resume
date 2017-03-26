var colors = {};
colors['tab-1'] = "e51c23";
colors['tab-2'] = "862197";
colors['tab-3'] = "2196f3";

var margins = {};
margins['tab-1'] = 1;
margins['tab-2'] = 2;
margins['tab-3'] = 3;
var tabPulled = "none";
var tabPulledReturn = 0;

var lock = 0;
function textFocus(id, color){
	// Get the color value
	try{
		color = colors[color];
	}catch(err){
		throw "Unknown color specified";
	}
	// Color all the text elements
	elements = document.getElementById(id).querySelectorAll("h1, h2, h3, h4, h5, h6");
	var currColor = color;
	for(e in elements){
		if (typeof(elements[e].innerText) != "undefined"){
			elements[e].style.color = "#"+color;
		}
	}
}	

function textUnFocus(id) {
	// Color all the text elements
	elements = document.getElementById(id).querySelectorAll("h1, h2, h3, h4, h5, h6");
	for(e in elements){
		if (typeof(elements[e].innerText) != "undefined"){
			elements[e].style.color = '';
		}
	}
}

function pushTab(c){
	var d = margins[c].toString() + '%';
	$(document.getElementsByClassName(c)[0]).velocity({marginLeft: d},{duration: '900'});
}

function pullTab(c){
	if(tabPulled == c){
		pushTab(c);
		tabPulled = "none";
		return;
	}
	if(tabPulled != "none"){
		pushTab(tabPulled);
	}
	tabPulled = c;
	// Actual pulling code
	var pushVal = (document.getElementsByClassName(c)[0].offsetWidth / $(document).width() * 100)-1;
	var pushLen = (margins[c]+pushVal).toString()+"%";
	$(document.getElementsByClassName(c)[0]).velocity({marginLeft: pushLen},{duration: '700'});
}
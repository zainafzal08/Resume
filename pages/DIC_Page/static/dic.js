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
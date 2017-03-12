function openNav(){
	$(document.getElementById('ul1')).velocity({width: '100%', marginLeft: '0%'},{duration: '900'});
	$(document.getElementById('ul3')).velocity({width: '100%'},{duration: '900'});
	$(document.getElementById('title')).velocity({opacity: '0'},{duration: '900'});
	$(document.getElementById('navL')).velocity({marginRight: '50%',opacity: '1'},{duration: '900'});
	$(document.getElementById('navR')).velocity({marginLeft: '50%',opacity: '1'},{duration: '900'});
	$(document.getElementById('head')).velocity({paddingTop: '5vh'},{duration: '900'});
	$(document.getElementById('data')).velocity({opacity: '1'},{duration: '900'});
	document.getElementById('ul2').onclick = function(){closeNav()};

}

function closeNav(){
	$(document.getElementById('ul1')).velocity({width: '0%', marginLeft: '100%'},{duration: '900'});
	$(document.getElementById('ul3')).velocity({width: '0%'},{duration: '900'});
	$(document.getElementById('title')).velocity({opacity: '1'},{duration: '900'});
	$(document.getElementById('navL')).velocity({marginRight: '0%',opacity: '0'},{duration: '900'});
	$(document.getElementById('navR')).velocity({marginLeft: '0%',opacity: '0'},{duration: '900'});
	$(document.getElementById('head')).velocity({paddingTop: '25vh'},{duration: '900'});
	$(document.getElementById('data')).velocity({opacity: '0'},{duration: '900'});
	document.getElementById('ul2').onclick = function(){openNav()};
}
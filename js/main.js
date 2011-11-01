$(document).ready(function(){
	
	$(".more").click(function(){
		$(this).parent().children(".description").slideToggle();
		if($(this).children().children().attr("src")=="images/more.png"){
			$(this).children().children().attr("src","images/close.png")
		}else{
			$(this).children().children().attr("src","images/more.png")
		}
		
		
		
	});
});

Cufon.replace('.need', { fontFamily: 'Futura' });
Cufon.replace('a.button', { fontFamily: 'Futura', textShadow: '#0d133b 1px 1px 1px' });
Cufon.replace('a.group', { fontFamily: 'Futura', textShadow: '#0d133b 1px 1px 1px' });
Cufon.replace('.introtitle', { fontFamily: 'Futura', textShadow: '#ffffff 1px 1px 1px' });
Cufon.replace('.menu', { fontFamily: 'Futura', textShadow: '#ffffff 1px 1px 1px' });
Cufon.replace('a.mail', { fontFamily: 'Futura', textShadow: '#ffffff 1px 1px 1px' });
Cufon.replace('h2', { fontFamily: 'Futura', textShadow: '#ffffff 1px 1px 1px' });

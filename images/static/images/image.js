image = document.getElementById('painting');
rotateLeft = document.getElementById('rotateleft');
rotateRight = document.getElementById('rotateright');
num_likes = document.getElementById('num_likes');
imid = document.getElementById('imid');
angle = 0;

rotateLeft.addEventListener('click', function(){
	angle -= 90;
	image.setAttribute('style','transform:rotate('+angle+'deg)');
})

rotateRight.addEventListener('click', function(){
	angle += 90;
	image.setAttribute('style','transform:rotate('+angle+'deg)');
})


document.addEventListener("DOMContentLoaded", function(event) { 
	$("#likebtn").click(function(){
				$.get('/putlike/'+imid.innerHTML,
					function(data,status){
						console.log(data);
						if(data.success)
							num_likes.innerHTML = "   "+(parseInt(num_likes.innerHTML)+1);
						else
							alert("You have already liked this painting");
					}
				);
			}
		);

});



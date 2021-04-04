
    var colors = ["black","orange","yellow","green","blue","indigo","violet","brown","white","red","grey","pink"];

    // Get the input field
    var inputVal = document.getElementById("inp");

    // Execute a function when the user releases a key on the keyboard
    inputVal.addEventListener("keyup", function(event) {
    // Number 13 is the "Enter" key on the keyboard
    if (event.keyCode === 13) {
        // Cancel the default action, if needed
        event.preventDefault();
        // Trigger the button element with a click
        document.getElementById("butto").click();
    }
    });

    function start(){
        for(var x = 0; x<300; x+=10){
            for(var y = 0; y<500; y+=10){
                drawIt(x, y);
            }
        }
    }

    document.addEventListener('DOMContentLoaded', function() {
        var link = document.getElementById('butto');
        // onClick's logic below:
        link.addEventListener('click', function() {
            start();
        });
    });



    function saveImage() {
				var ua = window.navigator.userAgent;

				if (ua.indexOf("Chrome") > 0) {
					var canvas = document.getElementById("main");
                    var name = document.getElementById("inp");
					// save image as png
					var link = document.createElement('a');
    				link.download = name.value+".png";
    				link.href = canvas.toDataURL("image/png").replace("image/png", "image/octet-stream");;
    				link.click();
				}
				else {
					alert("Please use Chrome");
				}
			}

    document.addEventListener('DOMContentLoaded', function() {
        var doen = document.getElementById('doen');
        // onClick's logic below:
        doen.addEventListener('click', function() {
            saveImage();
        });
    });
    function rando(salt_x, salt_y){
        var randy = 0;
        var inp = document.getElementById("inp");
        var seed = inp.value;
        for(var x = 0; x < seed.length; x++){
            if(x == 0){
                randy += seed.charCodeAt(x)*salt_y;
            }
             
            else{
                randy = randy * (seed.charCodeAt(x)+salt_x);
            } 
        
        }
        return (randy*(salt_x*salt_y))%26;
    };

    function drawIt(x, y){

    var c = document.getElementById("main");
    var con = c.getContext("2d");

    con.beginPath();
    con.rect(x, y, 10, 10);  
    con.fillStyle = colors[(rando((x+1), (y+1))%12)];
    con.fill();
    };



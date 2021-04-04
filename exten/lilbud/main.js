    var age = 0;
    var canvas = document.getElementById('main');
    var context = canvas.getContext('2d');
    var egg = new Image();
    egg.src = 'egg/egg40.png';
    var baby = new Image();
    baby.src = 'baby/baby40.png';

    egg.onload = function() {
        context.drawImage(egg, 55, 110);
    };
    
    

    function hatch(stage){
        if(age==0){
            egg.src = 'egg/egg42.png';
        }
        if(age==1){
            egg.src = 'egg/egg43.png';
        }
        if(age==2){
            egg.src = 'egg/egg44.png';
        }
        if(age==3){
            egg.src = 'egg/egg45.png';
        }
        if(age==4){

            context.clearRect(0,0,150,150);
            
            context.drawImage(baby, 45,90);            

            var i = 40;  

            var heart = setInterval(function spawn(){
                
                i++;
                var sauce = 'baby/heart'+i+'.png'
                baby.src = sauce;
                
                baby.onload = function(){
                    context.clearRect(0,0,150,150);
                    context.drawImage(baby, 45,90);
                }
                if(i==45){
                    clearInterval(heart);
                    uiChange(1);
                    baby.src = 'baby/baby40.png'
                }
            }, 250);
        }
        age++;
    }

    document.addEventListener('DOMContentLoaded', function() {
        var link = document.getElementById('hatch');
        // onClick's logic below:
        link.addEventListener('click', function() {
            hatch(age);
        });
    });

    document.addEventListener("click", function() {
        var link = document.getElementById('left');
        // onClick's logic below:
        link.addEventListener('click', function() {
            move(0);
        });
    });

    document.addEventListener("click", function() {
        var link = document.getElementById('right');
        // onClick's logic below:
        link.addEventListener('click', function() {
            move(1);
        });
    });

    function uiChange(prog){
        if(prog==1){
            var cont = document.getElementById("cont");
            cont.innerHTML = "<input type=\"button\" id=\"left\" value=\"<\"></input> <input type=\"button\" id=\"right\" value=\">\"></input>";
        }
        if(prog==2){
            var cont = document.getElementById("cont");
            cont.innerHTML = "";
        }
    }

    function move(dir){
        //move left
        if(dir==0){
            var i = 0;
            var left = setInterval(function left(){
                
                i+= 4;
                var sauce = 'baby/left40.png'
                baby.src = sauce;
                
                baby.onload = function(){
                    context.clearRect(0,0,150,150);
                    context.drawImage(baby, 45-i,90);
                }
                if(i==(25*4)){
                    clearInterval(left);
                }
            }, 250);
        }

        //move right
        if(dir==1){
            var i = 0;
            var right = setInterval(function right(){
                
                i+= 4;
                var sauce = 'baby/right40.png'
                baby.src = sauce;
                
                baby.onload = function(){
                    context.clearRect(0,0,150,150);
                    context.drawImage(baby, 45+i,90);
                }
                if(i==(25*4)){
                    clearInterval(right);
                }
            }, 250);
        }
    }
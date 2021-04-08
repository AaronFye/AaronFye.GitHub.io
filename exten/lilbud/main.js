    var age = 0;
    var canvas = document.getElementById('main');
    var context = canvas.getContext('2d');
    var pos = 45;
    var last = 0;
    var eaten = true;
    var carPos = -100;

    var egg = new Image();
    egg.src = 'egg/egg40.png';
    var baby = new Image();
    baby.src = 'baby/baby40.png';
    var carrot = new Image();
    carrot.src = 'etc/food40.png';

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
            
            context.drawImage(baby, pos,90);            

            var i = pos-5;;  

            var heart = setInterval(function spawn(){
                
                i++;
                var sauce = 'baby/heart'+i+'.png'
                baby.src = sauce;
                
                baby.onload = function(){
                    context.clearRect(0,0,150,150);
                    context.drawImage(baby, pos,90);
                }
                if(i==pos){
                    clearInterval(heart);
                    uiChange(1);
                    baby.src = 'baby/baby40.png'
                    go();
                }
            }, 250);
        }
        age++;
    }

    
    function move(dir){

        //move left
        if(dir==0){
            if(pos<110 && last != 2){
            var sauce = 'baby/right40.png';
            baby.src = sauce;
                
            baby.onload = function(){
                context.clearRect(pos+12, 125, 40, 35);
                context.drawImage(baby, pos+4,90);
                pos +=4;
                last = 1;
            }
            }
            else{
                var sauce = 'baby/baby40.png';
                baby.src = sauce;
                    
                baby.onload = function(){
                    context.clearRect(pos+10, 125, 35, 30);
                    context.drawImage(baby, pos,90);
                    last = 0;
                }
            }
        }
        else{
            if(pos>4 && last != 1){
                var sauce = 'baby/left40.png';
                baby.src = sauce;
                    
                baby.onload = function(){
                    context.clearRect(pos+10, 125, 35, 30);
                    context.drawImage(baby, pos-4,90);
                    pos -=4;
                    last = 2;
                }
            }
            else{
                var sauce = 'baby/baby40.png';
                baby.src = sauce;
                    
                baby.onload = function(){
                    context.clearRect(pos+10, 125, 35, 30);
                    context.drawImage(baby, pos,90);
                    last = 0;
                }
            }
        }
                
    }

    function go(){
    var moove = setInterval(function mover(){
        
        var rando = Math.floor(Math.random()*1000000)%2;
        move(rando);
        if(carPos==pos){
            age++;
            carPos= -100;
            context.clearRect(0,0,150,150);
            eaten = true;
        }

    }, 1000);
    }
    


    document.addEventListener('DOMContentLoaded', function() {
        var link = document.getElementById('hatch');
        // onClick's logic below:
        link.addEventListener('click', function() {
            hatch(age);
        });
    });

    function uiChange(prog){
        if(prog==1){
            var cont = document.getElementById("hatch");
            cont.style = "display: none;";
            var trol = document.getElementById("feed");
            trol.style = "display: inline;";
        }
    }

    function crop(x){
        if(eaten == true){
            eaten = false;
            var rando = (Math.floor(Math.random()*1000000)%2);
            if(rando==0){
                carPos = pos +24;
                if(carPos > 150){
                    carPos = pos - 24;
                }
            }
            else{
                carPos = pos - 24;
                if(carPos < 0){
                    carPos = pos + 24;
                }
            }
            context.drawImage(carrot, carPos , 125);
        }

    }

    document.addEventListener('DOMContentLoaded', function() {
        var link = document.getElementById('feed');
        // onClick's logic below:
        link.addEventListener('click', function() {
            var rando = (Math.floor(Math.random()*1000000)%15+3);
            crop(rando);
        });
    });

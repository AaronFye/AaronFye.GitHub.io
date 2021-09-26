    var age = 0;
    var canvas = document.getElementById('main');
    var context = canvas.getContext('2d');
    var pos = 45; // -30 for mid
    var lPos = 0;
    var last = 0;
    var eaten = true;
    var carPos = -100; //-10 for mid

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
            hrt();
        }
        age++;
    }

    function hrt(){
        context.clearRect(0,0,150,150);
            
            context.drawImage(baby, pos,90);            

            var i = 40;  

            var heart = setInterval(function spawn(){
                
                i++;
                var sauce = 'baby/heart'+i+'.png'
                baby.src = sauce;
                
                baby.onload = function(){
                    context.clearRect(0,0,150,150);
                    context.drawImage(baby, pos,90);
                }
                if(i==45){
                    clearInterval(heart);
                    context.clearRect(0,0,150,150);
                    uiChange(1);
                    baby.src = 'baby/baby40.png'
                    go(age);
                    
                }
            }, 250);
    }
    
    function move(dir){

        //move left
        if(dir==0){
            if(pos<110 && last != 2){
                if(age<10){
                    var sauce = 'baby/right40.png';
                    baby.src = sauce;
                        
                    baby.onload = function(){
                        context.clearRect(pos+12, 125, 40, 35);
                        context.drawImage(baby, pos+4,90);
                        lPos = pos;
                        pos +=4;
                        last = 1;
                    }
                }
                else{
                    var sauce = 'kid/right.png';
                    baby.src = sauce;
                        
                    baby.onload = function(){
                        context.clearRect(pos+12, 125, 40, 35);
                        context.drawImage(baby, pos+4,90);
                        lPos = pos;
                        pos +=4;
                        last = 1;
                    }
                }

            }
            else{
                if(age<11){
                    var sauce = 'baby/baby40.png';
                    baby.src = sauce;
                        
                    baby.onload = function(){
                        context.clearRect(pos+10, 125, 35, 30);
                        context.drawImage(baby, pos,90);
                        lPos = pos;
                        last = 0;
                    }
                    }
                else{
                    alert(age);
                }
            }
        }
        else{
            if(pos>4 && last != 1){
                if(age<11){
                    var sauce = 'baby/left40.png';
                    baby.src = sauce;
                        
                    baby.onload = function(){
                        context.clearRect(pos+10, 125, 35, 30);
                        context.drawImage(baby, pos-4,90);
                        lPos = pos;
                        pos -=4;
                        last = 2;
                    }
                }
                else{
                    alert(age);
                }
            }
            else{
                if(age<11){
                    var sauce = 'baby/baby40.png';
                    baby.src = sauce;
                        
                    baby.onload = function(){
                        context.clearRect(pos+10, 125, 35, 30);
                        context.drawImage(baby, pos,90);
                        lPos = pos;
                        last = 0;
                    }
                }
                else{
                    alert(age);
                }
            }
        }
                
    }

    function go(x){
    if(x<=5){
    var moove = setInterval(function mover(){
        var rando = Math.floor(Math.random()*1000000)%2;
        move(rando);
        if(carPos==(pos+34)){
            //alert("-2 la: " + (lPos+30) + " car " + carPos );
            if((lPos+30) < carPos){
            hrt();
            age++;
            //alert("- car " + carPos + " pos:" + pos + " tr" + (pos+30));
            carPos= -100;
            context.clearRect(0,0,150,150);
            eaten = true;
            document.getElementById("feed").style = "color:black";
            document.getElementById("count").src = "etc/count" + (age-5) + ".png";
            }

        }
        if((carPos+24)==(pos+30)){
            //alert("+2 la: " + (lPos+30) + " car " + carPos );
            if((lPos+30) > carPos){
            hrt();
            age++;
            //alert("+ car " + carPos + " pos:" + pos + " tr" + (pos+30));
            carPos= -100;
            context.clearRect(0,0,150,150);
            eaten = true;
            document.getElementById("feed").style = "color:black";
            document.getElementById("count").src = "etc/count" + (age-5) + ".png";
            }
        }
    }, 1000);
    }
    else{
        
    }
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
        
            
        
            var cart = document.getElementById("count");
            cart.style = "display: inline;";

            
            if(age == 10){
                document.getElementById("feed").style = "display: none;";
            }
            else{
                var trol = document.getElementById("feed");
                trol.style = "display: inline;";
            }

        }
    }

    function crop(x){
        if(eaten == true){
            var tpos = pos + 30; 
            eaten = false;
            var rando = (Math.floor(Math.random()*1000000)%2);
            if(rando==0){
                carPos = tpos +36;
                if(carPos > 130){
                    carPos = tpos - 44;
                }
            }
            else{
                carPos = tpos - 44;
                if(carPos < 10){
                    carPos = tpos + 36;
                }
            }
         //   alert("pos " + pos + " tpos " + tpos + " car " +carPos);
            context.drawImage(carrot, carPos, 125);
            document.getElementById("feed").style = "color:red";
          //  carPos +=12;
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

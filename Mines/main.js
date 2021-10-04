var lost = 0;
var trol = Math.floor(Math.random() *1000000);
var troll = trol%2;
var Egg = 0;

var bgm = new Audio("Minecraft.mp3");
var lbgm = new Audio("despasquido.wav");
var splat = new Audio("splat attack.mp3");
var mine = new Audio("dirt.mp3");
var bmg = new Audio("bomb.mp3");
var des = new Audio("despacito.mp3");
var hiss = new Audio("boom.mp3");

var field = 
[[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
];

/*function fill(){
    var ammo = (document.getElementById("ammo")).value;
    field = [[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]];
    Roll(ammo);

}*/

function rev(pos){
    var x = document.getElementById(pos);
    
    var pos = pos+"";
    var sub_x = pos.substring(0, 2);
    var sub_y = pos.substring(2, 4);
    
    sub_x--;
    sub_y--;

    if(!lost){
    if(field[sub_x][sub_y]==0){
        mine.play();
        bgm.play();        
        x.style = "background-color: white";
        var bmb = howMany(sub_x, sub_y);
        danger(bmb, x);
    }
    else{
        if(Egg){
            bmg.play();
            x.style = "background-image: url('bomb1.png'); background-size: 25px;";
        }
        else{
            hiss.play();
            x.style = "background-image: url('face.png'); background-size: 20px;";
        }
        Lose();
        bgm.pause();
    }
    }

}

function Lose(){
    if(Egg){
        if(troll==1){
            lbgm.play();
        }
        else{
            splat.play();
        }
    }
    else{
        des.play();
    }

    lost = 1;
    for(var l=0; l<16; l++){
        for(var k=0; k<16; k++){
            var loc = "";
            if(l<9){
                loc = "0";
                loc+=(l+1);
            }
            else{
                loc+=(l+1);
            }
            if(k<9){
                loc+="0";
                loc+=(k+1);
            }
            else{
                //alert("bruh");
                loc+=(k+1);
            }
            //alert(loc);
            var bom = document.getElementById(loc);
            if(field[l][k]){
                if(Egg){
                    bom.style = "background-image: url('bomb1.png'); background-size: 25px;";
                }
                else{
                    bom.style = "background-image: url('face.png'); background-size: 20px;";
                }
            }
        }
    }

    if(Egg){
        var bk = document.getElementById("bod");
        bk.style = "background-color: purple;";

        var bk = document.getElementById("left");
        bk.style = "float: right;  margin-left: 0%; margin-right: 15%;  visibility: visible;";
        var bk = document.getElementById("right");
        bk.style = "float: left; margin-left: 15%; margin-right: 0%; visibility: visible;";
    }
    else{
        var bk = document.getElementById("left");
        bk.src = "creeper.png";
        bk.style = "float: right;  margin-left: 0%; margin-right: 15%;  visibility: visible;";
        var bk = document.getElementById("right");
        bk.src = "creeper.png";
        bk.style = "float: left; margin-left: 15%; margin-right: 0%; visibility: visible;";
    }

}

function howMany(pos_x, pos_y){

    var num = 0;

    if(pos_x == 0 && pos_y == 0){
        if(field[pos_x+1][pos_y]){
            num++;
        }
        if(field[pos_x+1][pos_y+1]){
            num++;
        }
        if(field[pos_x][pos_y+1]){
            num++;
        }
        return num;
    }

    if(pos_x == 15 && pos_y == 0){
        if(field[pos_x-1][pos_y]){
            num++;
        }
        if(field[pos_x-1][pos_y+1]){
            num++;
        }
        if(field[pos_x][pos_y+1]){
            num++;
        }
        return num;
    }

    if(pos_x == 15 && pos_y == 15){
        if(field[pos_x-1][pos_y]){
            num++;
        }
        if(field[pos_x-1][pos_y-1]){
            num++;
        }
        if(field[pos_x][pos_y-1]){
            num++;
        }
        return num;
    }

    if(pos_x == 0 && pos_y == 15){
        if(field[pos_x][pos_y-1]){
            num++;
        }
        if(field[pos_x+1][pos_y-1]){
            num++;
        }
        if(field[pos_x+1][pos_y]){
            num++;
        }
        return num;
    }

    if( pos_x == 15 && 0<pos_y<15){
        if(field[pos_x-1][pos_y-1]){
            num++;
        }
        if(field[pos_x-1][pos_y]){
            num++;
        }
        if(field[pos_x-1][pos_y+1]){
            num++;
        }
        if(field[pos_x][pos_y-1]){
            num++;
        }
        if(field[pos_x][pos_y+1]){
            num++;
        }
        return num;
    }

    if( pos_x == 0 && 0<pos_y<15){
        
        if(field[pos_x][pos_y-1]){
            num++;
        }
        if(field[pos_x+1][pos_y-1]){
            num++;
        }
        if(field[pos_x+1][pos_y]){
            num++;
        }
        if(field[pos_x+1][pos_y+1]){
            num++;
        }
        if(field[pos_x][pos_y+1]){
            num++;
        }
        return num;
    }

    if(field[pos_x-1][pos_y-1]){
        num++;
    }
    if(field[pos_x-1][pos_y]){
        num++;
    }
    if(field[pos_x-1][pos_y+1]){
        num++;
    }
    if(field[pos_x][pos_y-1]){
        num++;
    }
    if(field[pos_x+1][pos_y-1]){
        num++;
    }
    if(field[pos_x+1][pos_y+1]){
        num++;
    }
    if(field[pos_x+1][pos_y]){
        num++;
    }
    if(field[pos_x][pos_y+1]){
        num++;
    }

    return num;
}

function Roll(numb){

    for(var i = 0; i<numb;){
        
        r_x = Math.floor(Math.random()*876543)%16;
        r_y = Math.floor(Math.random()*543210)%16;

        if(field[r_x][r_y] == 0){
            field[r_x][r_y] = 1;
            i++;
        }
    }
    

}

function easter(){
    Egg = 1;
}

function danger(number, doc){
    switch(number){
        case 0:
            doc.style = "background-image: url('0.png'); background-size: 25px;"
            break;
        case 1:
            doc.style = "background-image: url('1.png'); background-size: 25px;"
            break;
        case 2:
            doc.style = "background-image: url('2.png'); background-size: 25px;"
            break;
        case 3:
            doc.style = "background-image: url('3.png'); background-size: 25px;"
            break;
        case 4:
            doc.style = "background-image: url('4.png'); background-size: 25px;"
            break;
        case 5:
            doc.style = "background-image: url('5.png'); background-size: 25px;"
            break;
        case 6:
            doc.style = "background-image: url('6.png'); background-size: 25px;"
            break;
        case 7:
            doc.style = "background-image: url('7.png'); background-size: 25px;"
            break;
        case 8:
            doc.style = "background-image: url('8.png'); background-size: 25px;"
            break;        
    }
}

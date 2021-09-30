
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
]

function rev(pos){
    var x = document.getElementById(pos);
    
    var pos = pos+"";
    var sub_x = pos.substring(0, 2);
    var sub_y = pos.substring(2, 4);
    
    sub_x--;
    sub_y--;

    if(field[sub_x][sub_y]==0){        
        x.style = "background-color: white";
        var bmb = howMany(sub_x, sub_y);
        danger(bmb, x);
    }
    else{
        x.style = "background-image: url('bomb.png'); background-size: 25px;"
    }

}

function howMany(pos_x, pos_y){

    var num = 0;

    //for(var i = 0; i<8;i++){
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

function Roll(){

    for(var i = 0; i<32;){
        
        r_x = Math.floor(Math.random()*876543)%16;
        r_y = Math.floor(Math.random()*543210)%16;

        if(field[r_x][r_y] == 0){
            field[r_x][r_y] = 1;
            i++;
        }
    }
    

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

var result = 0;
var vs = document.getElementById("vs");
let board = new Array(9);
var turn = 0;
var won = false;
board = ['0','1','2','3','4','5','6','7','8'];
token = [['🟧','🟣'],['🐱','🐶'],['❌','⭕'],['🌝','🌞'],['❄','🔥'],['💩','🚽']];


result = Math.floor(Math.random()*100000)%6;

function Roll(){
    var lastResult = result;
    result = Math.random();
    result = result*100;
    result = result % 6;
    result = Math.trunc(result);
    vs.textContent = token[result][0] + " vs " + token[result][1];
    }

vs.textContent = token[result][0] + " vs " + token[result][1];

function win(){
    if(board[0]==board[1] && board[0]==board[2]){
        alert(token[result][turn%2] + " WINS!!!!");
        won = true;
    }
    if(board[3]==board[4] && board[4]==board[5]){
        alert(token[result][turn%2] + " WINS!!!!");
        won = true;
    }   

    if(board[6]==board[7] && board[8]==board[7]){
        alert(token[result][turn%2] + " WINS!!!!");
        won = true;
    }
    if(board[0]==board[3] && board[0]==board[6]){
        alert(token[result][turn%2] + " WINS!!!!");
        won = true;
    }

    if(board[1]==board[4] && board[1]==board[7]){
        alert(token[result][turn%2] + " WINS!!!!");
        won = true;
    }

    if(board[2]==board[5] && board[2]==board[8]){
        alert(token[result][turn%2] + " WINS!!!!");
        won = true;
    }

    if(board[0]==board[4] && board[0]==board[8]){
        alert(token[result][turn%2] + " WINS!!!!");
        won = true;
    }

    if(board[6]==board[4] && board[6]==board[2]){
        alert(token[result][turn%2] + " WINS!!!!");
        won = true;
    }

    if(turn == 9 && !won){
        alert("It is a tie!");
        won = true;
    }

    if(won){
        location.reload(true);
    }

}

function Tick(position) {
    if(!won){
        
    if(turn%2==0 && board[position]!='X' && board[position]!='O'){
    board[position] = 'X';
    var x = document.getElementById(position);
    x.textContent = token[result][0];
    win();
    turn++;
    if(turn==9){
        win();
    }
    }


    else if(turn%2==1 && board[position]!='X' && board[position]!='O'){
    board[position] = 'O';
    var x = document.getElementById(position);
    x.textContent = token[result][1];
    win();
    turn++;
    if(turn==9){
        win();
    }


    }  }
    }

    







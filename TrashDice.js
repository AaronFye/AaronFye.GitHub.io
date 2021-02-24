window.gun = new Gun({
    localStorage: false,
    secret: room,
    portal: "https://siasky.net",
    debug: false,
    })


var result = 0;
var vs = document.getElementById("vs");
let board = new Array(9);
var turn = 0;
var room = "null";
var won = false;
board = ['0','1','2','3','4','5','6','7','8'];
token = [['🟧','🟣'],['🐱','🐶'],['❌','⭕'],['🌝','🌞'],['❄','🔥'],['💩','🚽']];

var game = document.getElementById("game");

var code = document.getElementById("code");

var rc = document.getElementById("rc");

var again = document.getElementById("again");

gun.get('TTT').put({ board:board, won:won, turn:turn, token:token, result:result, game:game, code:code, rc:rc, again:again, vs:vs, room:room,});

again.style.display = 'none'; 
game.style.display = 'none'; 



result = Math.floor(Math.random()*100000)%6;

function Roll(){
    gun.get('TTT').on(data => { 
    result = Math.floor(Math.random()*100000)%6;
    vs.textContent = token[result][0] + " vs " + token[result][1];
    })
}

vs.textContent = token[result][0] + " vs " + token[result][1];

function win(){
    gun.get('TTT').on(data => { 
        if(board[0]==board[1] && board[0]==board[2]){
            alert(token[result][turn%2] + " WINS!!!!");
            won = true;
            gun.get('TTT').put({ board:board, won:won, turn:turn, token:token, result:result, game:game, code:code, rc:rc, again:again, vs:vs, room:room,});
        }
        if(board[3]==board[4] && board[4]==board[5]){
            alert(token[result][turn%2] + " WINS!!!!");
            won = true;
            gun.get('TTT').put({ board:board, won:won, turn:turn, token:token, result:result, game:game, code:code, rc:rc, again:again, vs:vs, room:room,});
        }   

        if(board[6]==board[7] && board[8]==board[7]){
            alert(token[result][turn%2] + " WINS!!!!");
            won = true;
            gun.get('TTT').put({ board:board, won:won, turn:turn, token:token, result:result, game:game, code:code, rc:rc, again:again, vs:vs, room:room,});
        }
        if(board[0]==board[3] && board[0]==board[6]){
            alert(token[result][turn%2] + " WINS!!!!");
            won = true;
            gun.get('TTT').put({ board:board, won:won, turn:turn, token:token, result:result, game:game, code:code, rc:rc, again:again, vs:vs, room:room,});
        }

        if(board[1]==board[4] && board[1]==board[7]){
            alert(token[result][turn%2] + " WINS!!!!");
            won = true;
            gun.get('TTT').put({ board:board, won:won, turn:turn, token:token, result:result, game:game, code:code, rc:rc, again:again, vs:vs, room:room,});
        }

        if(board[2]==board[5] && board[2]==board[8]){
            alert(token[result][turn%2] + " WINS!!!!");
            won = true;
            gun.get('TTT').put({ board:board, won:won, turn:turn, token:token, result:result, game:game, code:code, rc:rc, again:again, vs:vs, room:room,});
        }

        if(board[0]==board[4] && board[0]==board[8]){
            alert(token[result][turn%2] + " WINS!!!!");
            won = true;
            gun.get('TTT').put({ board:board, won:won, turn:turn, token:token, result:result, game:game, code:code, rc:rc, again:again, vs:vs, room:room,});
        }

        if(board[6]==board[4] && board[6]==board[2]){
            alert(token[result][turn%2] + " WINS!!!!");
            won = true;
            gun.get('TTT').put({ board:board, won:won, turn:turn, token:token, result:result, game:game, code:code, rc:rc, again:again, vs:vs, room:room,});
        }

        if(turn == 9 && !won){
            alert("It is a tie!");
            won = true;
            gun.get('TTT').put({ board:board, won:won, turn:turn, token:token, result:result, game:game, code:code, rc:rc, again:again, vs:vs, room:room,});
        }

        if(won){

            again.style.display = "block";
            gun.get('TTT').put({ board:board, won:won, turn:turn, token:token, result:result, game:game, code:code, rc:rc, again:again, vs:vs, room:room,});
        }
     })
}

function Tick(position) {
    if(!won){
        
        gun.get('TTT').on(data => { 
            if(turn%2==0 && board[position]!='X' && board[position]!='O'){
                board[position] = 'X';
                gun.get('TTT').put({ board:board, won:won, turn:turn, token:token, result:result, game:game, code:code, rc:rc, again:again, vs:vs, room:room,});

                var x = document.getElementById(position);
                x.textContent = token[result][0];
                win();
                turn++;
                gun.get('TTT').put({ board:board, won:won, turn:turn, token:token, result:result, game:game, code:code, rc:rc, again:again, vs:vs, room:room,});
                if(turn==9){
                    win();
                }
            }

            else if(turn%2==1 && board[position]!='X' && board[position]!='O'){
                board[position] = 'O';
                gun.get('TTT').put({ board:board, won:won, turn:turn, token:token, result:result, game:game, code:code, rc:rc, again:again, vs:vs, room:room,});
                var x = document.getElementById(position);
                x.textContent = token[result][1];
                win();
                turn++;
                gun.get('TTT').put({ board:board, won:won, turn:turn, token:token, result:result, game:game, code:code, rc:rc, again:again, vs:vs, room:room,});
                if(turn==9){
                    win();
                }
            }  

        })
    }
}

function Switch(){
    room = rc.value;
    code.style.display = 'none';  
    game.style.display = "block";
    }



gun.get('TTT').on(data => { 
    data = {state: board}
})




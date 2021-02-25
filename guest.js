window.gun = new Gun({
    localStorage: false,
    secret: "AaronGuest",
    portal: "https://siasky.net",
    debug: false,
})

gun.get('guest').on(data => { 
    //data = {: board}
})



var book = document.getElementById("list");

function load(name){
    var pre = book.innerHTML;
    book.innerHTML= pre + "<br>" + name; 
    
}

function sign(){
    var index = 0;
    var list = [""];
    item = "";
    var name = document.getElementById("sign");
    list[index] = name.value;
    index++;

    gun.get('guest').put({ list:list, index:index});
    
  ///  for(var f = 0; f<index;f++){
        load(name.value);
}

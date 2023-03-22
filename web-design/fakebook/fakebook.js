function hello(){
    let username = document.getElementById("userName");
    let password = document.getElementById("userPassword");
    alert(username.value + " " + password.value) ;
}

function hello2() {
    let login_info = document.getElementsByClassName("prompt");
    let username = login_info[0].value;
    let password = login_info[1].value;
    alert(username + " " + password);
}

/* JS EventHandlers */

let login = document.getElementById("loginButton");


login.onclick = hello2;

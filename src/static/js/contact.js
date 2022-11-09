function campos(){
    name = document.getElementById('name');
    email = document.getElementById('email');
    message = document.getElementById('message');

    if (name == " " || email == " " || message == " ") {
        document.getElementById('send').disabled = true;
    }
}
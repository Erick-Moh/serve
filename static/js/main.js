function showChatList() {
    document.getElementById('side--1').classList.remove("d-side");
    document.getElementById('side--2').classList.add("d-side");
}

function hideChatList() {
    document.getElementById('side--1').classList.add("d-side");
    document.getElementById('side--2').classList.remove("d-side");
}

function onKeyDown() {
    document.addEventListener('keydown', function (key) {
        if (key.which === 13) {
            sendMessage();
        }
    });
}

function sendMessage() {
    var message = `
        <div class="message my_message">
            <div>${document.getElementById('txtMessage').value}<br><span>8:15</span></div>
        </div>`;
    document.getElementById('messages').innerHTML += message;
    document.getElementById('txtMessage').value = '';
    document.getElementById('txtMessage').focus();

    // scroll effect
    document.getElementById('messages').scrollTo(0, document.getElementById('messages').clientHeight);
}

// Dropdown Menu
var dropbtns = Array.from(document.getElementsByClassName('dropbtn'))
// console.log(Array.from(dropbtns))
dropbtns.forEach(btn => {
    btn.addEventListener('click', function (e) {
        openDropdown(e.target.dataset.id)
    })
});
// DropDown 1
function openDropdown(id) {
    document.getElementById(id).classList.toggle("drop-show");
}

document.addEventListener("click", function (e) {
    // console.log(e)
    if (!e.target.matches('.dropbtn')) {
        var dropdownContents = Array.from(document.getElementsByClassName("dropdown-content"));
        dropdownContents.forEach(content => {
            content.classList.remove('drop-show');
        })
    }
})



// Model for show list
// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

console.log(document.getElementsByClassName("close"));
// When the user clicks the button, open the modal
btn.onclick = function () {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}


// Model for create group
var modal2 = document.getElementById("myModal2");

// Get the button that opens the modal
var btn2 = document.getElementById("myBtn2");

// Get the <span> element that closes the modal
var span2 = document.getElementsByClassName("close")[1];

// When the user clicks the button, open the modal
btn2.onclick = function () {
    modal2.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span2.onclick = function () {
    modal2.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal2) {
        modal2.style.display = "none";
    }
}


// Model for create group
var modal3 = document.getElementById("myModal3");

// Get the button that opens the modal
var btn3 = document.getElementById("myBtn3");

// Get the <span> element that closes the modal
var span3 = document.getElementsByClassName("close")[2];

// When the user clicks the button, open the modal
btn3.onclick = function () {
    modal3.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span3.onclick = function () {
    modal3.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal3) {
        modal3.style.display = "none";
    }
}


// Send Image File
function chooseImage() {
    document.getElementById('imageFile').click();
}

function sendImage(event) {
    var file = event.files[0];

    if (!file.type.match("image.*")) {
        alert("Please select image only.")
    }
    else {
        alert("Image send...")
    }
}

// Send Icon and Audio | Send Message
function changeSendIcon(control) {
    if (control.value !== '') {
        document.getElementById('send').removeAttribute('style');
        document.getElementById('audio').setAttribute('style', 'display:none');
    }
    else {
        document.getElementById('audio').removeAttribute('style');
        document.getElementById('send').setAttribute('style', 'display:none');
    }
}
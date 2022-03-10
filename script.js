// let searchBtn = document.querySelector('#search-btn');
// let searchBar = document.querySelector('.search-bar-container');
let formBtn = document.querySelector('#login-btn');
let loginForm = document.querySelector('.login-form-container');
let formClose = document.querySelector('#form-close');


window.onscroll = () =>{
    // searchBtn.classList.remove('fa-times');
    searchBar.classList.remove('active');
    loginForm.classList.remove('active');

}

// searchBtn.addEventListener('click', () =>{
//     searchBtn.classList.toggle('fa-times');
//     searchBar.classList.toggle('active');
// });



formBtn.addEventListener('click', () =>{
    loginForm.classList.add('active');
});


formClose.addEventListener('click', () =>{
    loginForm.classList.remove('active');
});

// var modal = document.getElementById("myModal");

// // Get the button that opens the modal
// var btn = document.getElementById("myBtn");

// // Get the <span> element that closes the modal
// var span = document.getElementsByClassName("close")[0];

// // When the user clicks the button, open the modal 
// btn.onclick = function() {
//   modal.style.display = "block";
// }

// // When the user clicks on <span> (x), close the modal
// span.onclick = function() {
//   modal.style.display = "none";
// }

// // When the user clicks anywhere outside of the modal, close it
// window.onclick = function(event) {
//   if (event.target == modal) {
//     modal.style.display = "none";
//   }
// }

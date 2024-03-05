let searchForm=document.querySelector('.search-form');
document.querySelector('#search-btn').onclick=()=>
{
    searchForm.classList.toggle('active');
    shoppingCart.classList.remove('active');
    loginForm.classList.remove('active');
}

let shoppingCart=document.querySelector('.shopping-cart');
document.querySelector('#cart-btn').onclick=()=>
{
    shoppingCart.classList.toggle('active');
    searchForm.classList.remove('active');
    loginForm.classList.remove('active');
}

let loginForm=document.querySelector('.login-form');
document.querySelector('#login-btn').onclick=()=>
{
    loginForm.classList.toggle('active');
    searchForm.classList.remove('active');
    shoppingCart.classList.remove('active');
}






let loginForm1=document.querySelector('.login-form1');
document.querySelector('#messenger-btn').onclick=()=>
{
    loginForm1.classList.toggle('active');
    searchForm.classList.remove('active');
    shoppingCart.classList.remove('active');

}








window.onscroll=() =>
{
    searchForm.classList.remove('active');
    shoppingCart.classList.remove('active');
    loginForm.classList.remove('active');
}



var attempt = 3; // Variable to count number of attempts.
// Below function Executes on click of login button.
function validate(){
var username = document.getElementById("username").value;
var password = document.getElementById("password").value;
if ( username == "ashok31@gmail.com" && password == "ashok123"){
alert ("Login successfully Completed!..");
window.location = "index.html"; // Redirecting to other page.
return false;
}
else{
attempt --;// Decrementing by one.
alert("Login Failed, You have left "+attempt+" attempt;");
// Disabling fields after 3 attempts.
if( attempt == 0){
document.getElementById("username").disabled = true;
document.getElementById("password").disabled = true;
document.getElementById("submit").disabled = true;
return false;
}
}
}


document.addEventListener("DOMContentLoaded", function () {
    // Get the sign-out button by ID
    var logoutButton = document.getElementById("logout-btn");

    // Add a click event listener to the sign-out button
    logoutButton.addEventListener("click", function () {
        // Display the "Successfully Signed-out" message
        alert("Successfully Signed-out");
        // You can also redirect to a sign-out page or perform other actions here
    });
});



document.addEventListener("DOMContentLoaded", function () {
    // Initialize Swiper for the product slider
    var productSwiper = new Swiper(".product-slider", {
        loop: true,
        spaceBetween: 20,
        autoplay: {
            delay: 7500,
            disableOnInteraction: false,
        },
        breakpoints: {
            0: {
                slidesPerView: 1,
            },
            768: {
                slidesPerView: 2,
            },
            1020: {
                slidesPerView: 3,
            },
        },
        // Add pagination
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
    });

    // Your other JavaScript code here...
});


document.addEventListener("DOMContentLoaded", function () {
    // Initialize Swiper for the product slider
    var productSwiper = new Swiper(".review-slider", {
        loop: true,
        spaceBetween: 20,
        autoplay: {
            delay: 7500,
            disableOnInteraction: false,
        },
        breakpoints: {
            0: {
                slidesPerView: 1,
            },
            768: {
                slidesPerView: 2,
            },
            1020: {
                slidesPerView: 3,
            },
        },
        // Add pagination
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
    });

    // Your other JavaScript code here...
});

function myFunction() {
    var element = document.body;
    element.classList.toggle("dark-mode");
 }






 function validate1(){

    alert ("Your Query successfully sent...");
    window.location = "index.html"; // Redirecting to other page.
    return false;
    }







    var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
}
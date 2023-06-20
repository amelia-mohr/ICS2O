document.addEventListener('DOMContentLoaded', loadPage);

function loadPage(){
    deleteCookie();
};

function deleteCookie(){
    // Deleting payload in cookie to count 0 items in cart
    console.log("emptying cookie");
    document.cookie = "cart= " + JSON.stringify({}) + "; path=/";
    console.log("cookie should be empty");
};

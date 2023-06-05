const btnCart = document.querySelector('#bag');
const cart = document.querySelector('.cart');
const btnClose = document.querySelector('#cart-close');

btnCart.addEventListener('click', () => {
    cart.classList.add('cart-active');
});

btnClose.addEventListener('click', () => {
    cart.classList.remove('cart-active');
});


document.addEventListener('DOMContentLoaded',loadProducts);

function loadProducts(){
    loadContent();
};

function loadContent(){
    //Remove Items From Cart
    let btnRemove = document.querySelectorAll('.remove');
    btnRemove.forEach((btn) => {
        btn.addEventListener('click', removeItem);
    });

    // Product Item Change Event
    const num = document.getElementById("num");
    const add = document.getElementById("add");
    const sub = document.getElementById("sub");
    add.forEach((btn) => {
        btn.addEventListener('click', increaseQty);
    });
    sub.forEach((btn) => {
        btn.addEventListener('click', lowerQty);
    });
};

// Remove Item
function removeItem(){
    this.parentElement.remove();
};

//Lower Quantity
function lowerQty(){
    if (num.innerHTML > 1) {
        num.innerHTML--;
    };
};

//Increase Quantity
function increaseQty(){
    if (num.innerHTML < 9){
        num.innerHTML++;
    };
};
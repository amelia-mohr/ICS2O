const btnCart = document.querySelector('.bag');
const cart = document.querySelector('.cart');
const btnClose = document.querySelector('#cart-close');

btnCart.forEach((btn) => {
    btn.addEventListener('click', showCart);
});

function showCart(){
    cart.classList.add('cart-active');
};

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
    
};

// Remove Item
function removeItem(){
    this.parentElement.remove();
};
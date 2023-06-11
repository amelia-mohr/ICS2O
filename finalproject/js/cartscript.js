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
    //Add to Cart
    // btnAddBag1 = document.querySelectorAll('#add-bag-1.add-btn');
    //btnAddBag1.addEventListener('click', addBag1);
    console.log('bag page loaded');
    console.log(decodeURIComponent(document.cookie));
};

// Remove Item
function removeItem(){
    this.parentElement.remove();
};

//Add Cart

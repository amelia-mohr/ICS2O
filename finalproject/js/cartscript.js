const btnCart = document.querySelector('#bag');
const cart = document.querySelector('.cart');
const btnClose = document.querySelector('#cart-close');

// title to price
var titleToPrice = {};
titleToPrice['Product1'] = 8.00;
titleToPrice['Product2'] = 10.00;
titleToPrice['Product3'] = 12.00;

// title to image
var titleToImage = {};
titleToImage['Product1'] = "puppic1.jpg";
titleToImage['Product2'] = "puppic2.jpg";
titleToImage['Product3'] = "puppic3.jpg";

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            nc = c.substring(1);
        };
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        };
    };
    return null;
}

// delete item & cookie
function removeLogic(title) {
    let c = getCookie("cart");
    if (c == null) {
        // nothing in the cookie 
    } else {
        // load the cookie from a string to dictionary
        let obj = JSON.parse(c);
        let found = false;
        // look through all the items in the bag
        // if find our current item -> delete
        for (const [key] of Object.entries(obj)) {
            if (key == title) {
                delete obj[key];
                found = true;
            };
        };
        if (!found) {
            console.log("NOT FOUND!!!");
        };
        document.cookie = "cart=" + JSON.stringify(obj) + "; path=/";     
    };
    let itemDiv = document.getElementById("item-" + title);
    itemDiv.parentElement.remove();
}

btnCart.addEventListener('click', () => {
    cart.classList.add('cart-active');
    const cartBasket = document.getElementById("cart-content");
    cartBasket.innerHTML = '';
    let c = getCookie("cart");
    if (c == null) {
        // nothing in the cookie, cart is empty
    } else {
        let obj = JSON.parse(c);
        // look through all the items in the bag and add them to the panel
        for (const [key, value] of Object.entries(obj)) {
            let newProductElement = createCartProduct(key,value,titleToPrice,titleToImage);
            let element = document.createElement('div');
            element.innerHTML = newProductElement;
            cartBasket.append(element);
            // delete function
            const btnRemove = document.getElementById('remove-' + key);
            btnRemove.addEventListener('click', () => {
                removeLogic(key);
            });
        };
    };
});

btnClose.addEventListener('click', () => {
    cart.classList.remove('cart-active');
});

// add cart
function createCartProduct(title,qty,titleToPrice,titleToImage){
    // lookup price
    let overallPrice = titleToPrice[title] * parseInt(qty);
    let price = overallPrice.toFixed(2)
    console.log(price);

    // lookup image
    let image = titleToImage[title];

    return `
    <div id="item-${title}" class="cart-box">
      <img src="/images/${image}" class="cart-img">
      <div class="detail-box">
        <h3 id="box-title">${title}</h3>
        <div class="price-box">
          <p>Price:</p>
          <h4>$${price}</h4>
        </div>
        <p>Quantity: <span class="product-quant">${qty}</span></p>
      </div>
      <span id="remove-${title}" class="remove material-symbols-rounded">delete</span>
    </div>
    `;
};

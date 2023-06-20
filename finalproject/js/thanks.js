const btnCart = document.querySelector('#bag');
const cart = document.querySelector('.cart');
const btnClose = document.querySelector('#cart-close');

// title to price
var titleToPrice = {};
titleToPrice['Product1'] = 7.00;
titleToPrice['Product2'] = 6.00;
titleToPrice['Product3'] = 5.00;
titleToPrice['Product4'] = 20.00;

// title to image
var titleToImage = {};
titleToImage['Product1'] = "whale/dark_blue_front.jpeg";
titleToImage['Product2'] = "egg/one_egg.jpeg";
titleToImage['Product3'] = "bubbletea/bubbletea_1.jpeg";
titleToImage['Product4'] = "octopus/octopus_front.jpeg";

// title to product name
var titleToProduct = {};
titleToProduct['Product1'] = "Whale";
titleToProduct['Product2'] = "Sunny Side Up Eggs";
titleToProduct['Product3'] = "Bubble Tea";
titleToProduct['Product4'] = "Octopus";

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
    let name = titleToProduct[title];
    let answer = confirm("Are you sure you want to delete " + name + "?");
    answer;
    if (answer == true){
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
                alert("Unfortunately, there has been an error. Please try again.")
            };
            document.cookie = "cart=" + JSON.stringify(obj) + "; path=/";     
        };
        let itemDiv = document.getElementById("item-" + title);
        itemDiv.parentElement.remove();
        countItems();
        finalTotal();
    };
};

//open cart
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
            // adding product to cart
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
    finalTotal();
});

//close cart
btnClose.addEventListener('click', () => {
    cart.classList.remove('cart-active');
});

// add cart
function createCartProduct(title,qty,titleToPrice,titleToImage){
    // lookup price
    let overallPrice = titleToPrice[title] * parseInt(qty);
    let price = overallPrice.toFixed(2)

    // lookup image
    let image = titleToImage[title];

    // lookup name
    let name = titleToProduct[title];

    return `
    <div id="item-${title}" class="cart-box">
      <img src="/images/${image}" class="cart-img">
      <div class="detail-box">
        <h3 id="box-title">${name}</h3>
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

document.addEventListener('DOMContentLoaded', loadPage);

function loadPage(){
    deleteCookie();
    countItems();
};

function deleteCookie(){
    // Deleting payload in cookie to count 0 items in cart
    console.log("emptying cookie");
    document.cookie = "cart= " + JSON.stringify({}) + "; path=/";
    console.log("cookie should be empty");
};

//count items
function countItems(){
    let count = document.getElementById("items");
    count.innerHTML = 0;
    let c = getCookie("cart");
    if (c == null) {
        // nothing in the cookie, cart is empty
    } else {
        let obj = JSON.parse(c);
        // look through all the items in the bag and add to count
        for (const [key, value] of Object.entries(obj)) {
            count.innerHTML++;
        };
    };
};

// get the final total
function finalTotal(){
    let finalTotal = document.getElementById("final-total");
    finalTotal.innerHTML = 0.00;
    let c = getCookie("cart");
    if (c == null) {
        // nothing in the cookie, cart is empty
    } else {
        let obj = JSON.parse(c);
        // look through all the items in the bag and add to count
        for (const [key, value] of Object.entries(obj)) {
            // getting final total
            let itemPrice = parseFloat(titleToPrice[key] * parseInt(value));
            finalTotal.innerHTML = (parseFloat(finalTotal.innerHTML) + itemPrice).toFixed(2);
        };
    };
};

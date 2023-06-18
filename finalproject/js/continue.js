const sendBtn = document.getElementById('send');
const fName = document.getElementById('fname');
const lName = document.getElementById('lname');

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

sendBtn.addEventListener('click', () => {
    if (fName.value.trim().length == 0 || lName.value.trim().length == 0) {
        console.log("No first name")
        return;
    }
    let c = getCookie("cart");
    if (c == null) {
        // nothing in the cookie, cart is empty
        return;
    } else {
        let obj = JSON.parse(c);

        obj['first'] = fName.value;
        obj['last'] = fName.value;
        
        console.log(obj);
    };
});
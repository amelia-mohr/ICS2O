var largeImg = document.getElementById("largeImg");
var smallImg = document.getElementsByClassName("smallImg");
var layer = document.getElementsByClassName("layer");

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    console.log(decodedCookie);
    let ca = decodedCookie.split(';');
        for(let i = 0; i <ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) == ' ') {
                c = c.substring(1);
            };
            if (c.indexOf(name) == 0) {
                return c.substring(name.length, c.length);
            };
        };
    return null;
}
      
layer[0].onclick = function(){
    largeImg.src = smallImg[0].src;
}
layer[1].onclick = function(){
    largeImg.src = smallImg[1].src;
}
layer[2].onclick = function(){
    largeImg.src = smallImg[2].src;
};
const num = document.getElementById("num");
const add = document.getElementById("add");
const sub = document.getElementById("sub");
const price = document.getElementById("price");
const cost = 7.00;
add.onclick = function(){
    if (num.innerHTML < 9){
        num.innerHTML++;
        const result = cost * num.innerHTML;
        price.innerHTML = result.toFixed(2);
    };
};
sub.onclick = function(){
    if (num.innerHTML > 1) {
        num.innerHTML--;
        const result = cost * num.innerHTML;
        price.innerHTML = result.toFixed(2);
    };
};

var btnAddBag1 = document.getElementById('add-bag-1');
btnAddBag1.addEventListener('click', () => {
    let c = getCookie("cart");
    if (c == null) {
        // nothing in the cookie, just add our item
        document.cookie = "cart=" + JSON.stringify({Product1: num.innerHTML}) + "; path=/";
    } else {
        // load the cookie from a string to dictionary
        let obj = JSON.parse(c);
        let found = false;
        // look through all the items in the bag
        // if find current item -> add to the count
        for (const [key, value] of Object.entries(obj)) {
            if (key == 'Product1') {
                let total = parseInt(value) + parseInt(num.innerHTML);
                if (total > 9) {
                    total = 9;
                };
                obj['Product1'] = total;
                found = true;
            };
        };
        if (!found) {
            obj['Product1'] = num.innerHTML;
        };
        document.cookie = "cart=" + JSON.stringify(obj) + "; path=/";     
    }; 
    alert("Item added to cart!");
});

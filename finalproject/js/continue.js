const sendBtn = document.getElementById('send');
const fName = document.getElementById('fname');
const lName = document.getElementById('lname');

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
        return;
    }
    let c = getCookie("cart");
    if (c == null) {
        // nothing in the cookie, cart is empty
        return;
    } else {
        let obj = JSON.parse(c);
        // replace Pro# with actual name
        for (const [key, value] of Object.entries(obj)) {
            let name = titleToProduct[key];
            obj[name] = obj[key];
            delete obj[key];
        };
        // add user name to cookie
        obj['first'] = fName.value;
        obj['last'] = lName.value;
        
        console.log(obj);

        // Creating a XHR object
        let xhr = new XMLHttpRequest();
        let url = "/python/";
        // open a connection
        xhr.open("POST", url, true);
        // Set the request header i.e. which type of content you are sending
        xhr.setRequestHeader("Content-Type", "application/json");
        // Converting JSON data to string
        var data = JSON.stringify(obj);
        // Sending data with the request
        xhr.send(data);uestHeader("Content-Type", "application/json");
        xhr.send();
        // Deleting payload in cookie to count 0 items in cart
        let c = getCookie("cart");
        if (c == null) {
             // nothing in the cookie 
         } else {
            // load the cookie from a string to dictionary
            let obj = JSON.parse(c);
            let found = false;
            // look through all the items in the bag
            // delete all
            for (const [key] of Object.entries(obj)) {
                delete obj[key];
                found = true;
            };
            if (!found) {
                console.log("NOT FOUND!!!");
                alert("Unfortunately, there has been an error. Please try again.")
            };
            document.cookie = "cart=" + JSON.stringify(obj) + "; path=/";     
        };
    };
});

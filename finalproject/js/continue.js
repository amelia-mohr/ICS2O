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
        obj['last'] = lName.value;
        
        console.log(obj);

        // Creating a XHR object
        let xhr = new XMLHttpRequest();
        let url = "/python";
   
        // open a connection
        xhr.open("POST", url, true);

        // Set the request header i.e. which type of content you are sending
        xhr.setRequestHeader("Content-Type", "application/json");

        // // Create a state change callback
        // xhr.onreadystatechange = function () {
        //     if (xhr.readyState === 4 && xhr.status === 200) {

        //         // Print received data from server
        //         result.innerHTML = this.responseText;

        //     }
        // };

        // Converting JSON data to string
        var data = JSON.stringify(obj);

        // Sending data with the request
        xhr.send(data);uestHeader("Content-Type", "application/json");
        xhr.send();
    };
});
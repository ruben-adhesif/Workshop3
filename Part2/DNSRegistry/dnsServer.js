const express = require('express');
const dnsApp = express();
const dnsPort = 4000;

// Flag to represent the state of the e-commerce server
let isEcommerceServerUp = true;

dnsApp.get('/getServer', (req, res) => {
    if (isEcommerceServerUp) {
        res.json({ "code": 200, "server": "localhost:3002" });
    } else {
        // E-commerce app is down, redirect to Hello World server
        res.json({ "code": 200, "server": "localhost:3001" });
    }
});

dnsApp.get('/toggleEcommerceServer', (req, res) => {
    isEcommerceServerUp = !isEcommerceServerUp; // Toggle the server state
    res.send(`E-commerce server is now ${isEcommerceServerUp ? "up" : "down"}`);
});

dnsApp.listen(dnsPort, () => {
    console.log(`DNS Server listening at http://localhost:${dnsPort}`);
});

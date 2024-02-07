const express = require('express');
const fs = require('fs');
const app = express();
const port = 3002;

app.use(express.json());
app.use(express.static('public'));


// Helper function to read the database
function readDB() {
    return JSON.parse(fs.readFileSync('db.json', 'utf8'));
}

// Helper function to write to the database
function writeDB(data) {
    fs.writeFileSync('db.json', JSON.stringify(data, null, 2), 'utf8');
}

// Products Routes
app.get('/products', (req, res) => {
    const db = readDB();
    res.json(db.products);
});

app.get('/products/:id', (req, res) => {
    const db = readDB();
    const product = db.products.find(p => p.id === parseInt(req.params.id));
    if (!product) return res.status(404).send('Product not found.');
    res.json(product);
});

app.post('/products', (req, res) => {
    const db = readDB();
    const newProduct = { id: db.products.length + 1, ...req.body };
    db.products.push(newProduct);
    writeDB(db);
    res.status(201).json(newProduct);
});

app.put('/products/:id', (req, res) => {
    const db = readDB();
    const productIndex = db.products.findIndex(p => p.id === parseInt(req.params.id));
    if (productIndex === -1) return res.status(404).send('Product not found.');

    db.products[productIndex] = { ...db.products[productIndex], ...req.body };
    writeDB(db);
    res.json(db.products[productIndex]);
});

app.delete('/products/:id', (req, res) => {
    const db = readDB();
    const productIndex = db.products.findIndex(p => p.id === parseInt(req.params.id));
    if (productIndex === -1) return res.status(404).send('Product not found.');

    db.products.splice(productIndex, 1);
    writeDB(db);
    res.send(`Product with id ${req.params.id} deleted`);
});

// Orders Routes
app.post('/orders', (req, res) => {
    const db = readDB();
    const newOrder = { id: db.orders.length + 1, ...req.body };
    db.orders.push(newOrder);
    writeDB(db);
    res.status(201).json(newOrder);
});

app.get('/orders/:userId', (req, res) => {
    const db = readDB();
    const userOrders = db.orders.filter(order => order.userId === parseInt(req.params.userId));
    res.json(userOrders);
});

// Cart Routes
app.post('/cart/:userId', (req, res) => {
    const db = readDB();
    const { userId } = req.params;
    const { productId, quantity } = req.body;

    if (!db.carts[userId]) {
        db.carts[userId] = [];
    }
    db.carts[userId].push({ productId, quantity });
    writeDB(db);

    res.json({ message: 'Product added to cart', cart: db.carts[userId] });
});

app.get('/cart/:userId', (req, res) => {
    const db = readDB();
    const userCart = db.carts[req.params.userId] || [];
    res.json(userCart);
});

app.delete('/cart/:userId/item/:productId', (req, res) => {
    const db = readDB();
    const userCart = db.carts[req.params.userId];
    if (!userCart) return res.status(404).send('Cart not found.');

    const productIndex = userCart.findIndex(item => item.productId === parseInt(req.params.productId));
    if (productIndex === -1) return res.status(404).send('Product not found in cart.');

    userCart.splice(productIndex, 1);
    writeDB(db);
    res.send(`Product with id ${req.params.productId} removed from cart`);
});




// Start the server
app.listen(port, () => {
    console.log(`E-commerce API server listening at http://localhost:${port}`);
});

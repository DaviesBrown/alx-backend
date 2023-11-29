const express = require("express");
const redis = require("redis");
const { promisify } = require("util");

const app = express();
app.use(express.json());
const PORT = 1245;

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
client.on("error", err => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});
client.on("connect", (stream) => {
    console.log("Redis client connected to the server");
});

const listProducts = [
    {itemId: 1, itemName: "Suitcase 250", price: 50, initialAvailableQuantity: 4},
    {itemId: 2, itemName: "Suitcase 450", price: 100, initialAvailableQuantity: 10},
    {itemId: 3, itemName: "Suitcase 650", price: 350, initialAvailableQuantity: 2},
    {itemId: 4, itemName: "Suitcase 1050", price: 550, initialAvailableQuantity: 5}
];

const getItemById = (id) => {
    return listProducts.filter(product => product.itemId === id)[0];
};

const reserveStockById = (itemId, stock) => {
    client.decr(itemId);
};

const getCurrentReservedStockById = async (itemId) => {
    try {
        const response = await getAsync(itemId);
        //console.log(response)
        if (!response) {
            client.set(itemId, getItemById(itemId).initialAvailableQuantity);
            console.log(response)
        }
        return response;
    } catch (err) {
        console.log(`Redis error: ${err}`);
    }
};

app.get("/list_products", (req, res) => {
    res.status(200);
    res.send(JSON.stringify(listProducts));
});

app.get("/list_products/:itemId(\\d+)", async (req, res) => {
    res.status(200);
    const itemId = Number(req.params.itemId);
    const item = getItemById(itemId);
    if (item === undefined) {
        return res.status(400).send(JSON.stringify({status: "Product not found"}));
    }
    const stock = await getCurrentReservedStockById(itemId);
    const current_item = {...item, currentQuantity: stock};
    res.send(JSON.stringify(current_item));
});

app.get("/reserve_product/:itemId(\\d+)", async (req, res) => {
    res.status(200);
    const itemId = Number(req.params.itemId);
    const item = getItemById(itemId);
    if (item === undefined) {
        return res.status(400).send(JSON.stringify({status: "Product not found"}));
    }
    const stock = await getCurrentReservedStockById(itemId);
    if (stock < 1) {
        return res.status(400).send(JSON.stringify({status: "Reservation confirmed", itemId}));
    };
    reserveStockById(itemId, 1);
    const status = {status: "Reservation confirmed",itemId};
    res.send(JSON.stringify(status));
});


app.listen(PORT, () => console.log(`listening on port ${PORT}`));

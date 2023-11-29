const express = require("express");
const redis = require("redis");
const { promisify } = require("util");
const kue = require("kue");

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


const reserveSeat = (number) => {
    client.set("available_seats", number);
};

const getCurrentAvailableSeats = async () => {
    try {
        const response = await getAsync("available_seats");
        return response;
    } catch (err) {
        console.log(`Redis error: ${err}`);
    }
};

client.set("available_seats", 50);
const reservationEnabled = true;

const queue = kue.createQueue();

app.get("/available_seats", async (req, res) => {
    res.status(200);
    const numberOfAvailableSeats = await getCurrentAvailableSeats();
    res.send(JSON.stringify({numberOfAvailableSeats}));
});

app.get("/reserve_seat", async (req, res) => {
    res.status(200);
    if (reservationEnabled === false) {
        return res.status(400).send(JSON.stringify({status: "Reservation are blocked"}));
    }
    const reserve_seat_job = queue.create("reserve_seat", {}).save((err) => {
        if (!err) {
            res.send(JSON.stringify({status: "Reservation in process"}));
        }else {
            return res.status(400).send(JSON.stringify({status: "Reservation failed"}));
        }
    });
    reserve_seat_job.on("complete", () => {
        console.log(`Seat reservation job ${reserve_seat_job.id} completed`);
    });
    reserve_seat_job.on("failed", (err) => {
        console.log(`Seat reservation job ${reserve_seat_job.id} failed: ${err}`);
    });
});

app.get("/process", (req, res) => {
    
});

app.listen(PORT);

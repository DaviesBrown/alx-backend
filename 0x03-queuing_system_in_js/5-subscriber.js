import redis from "redis";

const client = redis.createClient();

client.on("error", err => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});
client.on("connect", (stream) => {
    console.log("Redis client connected to the server");
});
client.subscribe("holberton school channel");
const listener = (channel, message) => {
    if (message === "KILL_SERVER") {
        client.unsubscribe("holberton school channel");
        client.quit();
    }
    console.log(message);
};
client.on("message", listener);

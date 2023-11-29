import { createClient } from "redis";

async function redisClient() {
    const client = await createClient()
    .on("error", err => {
        console.log(`Redis client not connected to the server: ${err.message}`);
    })
    .on("connect", (stream) => {
        console.log("Redis client connected to the server");
    });
}

redisClient();
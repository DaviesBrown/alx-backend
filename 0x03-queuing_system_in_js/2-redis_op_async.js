import redis from "redis";
const { promisify } = require("util");



const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
client.on("error", err => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});
client.on("connect", (stream) => {
    console.log("Redis client connected to the server");
});


function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
    
}

async function displaySchoolValue(schoolName) {
    try {
        const response = await getAsync(schoolName);
        console.log(response);
    } catch (err) {
        console.log(`Redis error: ${err}`);
    }
}

async function main() {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
}

main();

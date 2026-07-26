const express = require('express');
const app = express();

const weather = {
    Ahmedabad: { temperature: "35°C", description: "Sunny" },
    Delhi: { temperature: "30°C", description: "Cloudy" },
    Mumbai: { temperature: "28°C", description: "Rainy" }
};

app.get("/", (req, res) => {
    res.send (`<h2>Weather Information</h2>`)
})

app.get("waether/",(req,res)=>{
    const location=req.query.location;
    if(!location){
        return res.send("Please enter location")
    }
    if(weather[location]){
        res.send(`<h2>Weather Details</h2>
            Location:${location}<br>
            Temperature:${weather[location].temperature}<br>
            Description:${weather[location].description}<br>`)
        }
        else{
            res.send(`<h2>Location Not Found</h2>`)
        }
}).listen(3000)
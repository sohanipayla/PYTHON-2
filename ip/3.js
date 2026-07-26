const express = require("express");
const app = express();
const cookieParser = require("cookie-parser");
app.use(cookieParser());
app.use(express.urlencoded({ extended: true }));

app.get("/", (req, res) => {
    res.send(`<h2>User Signup FORM </h2>
        <form method="POST" action="/register">
        name:<input type='text' name='name'><br>
        contact:<input type='text' name='contact'><br>
        email:<input type='email' name='email'><br>
        address:<textarea name='address'></textarea><br>
        gender:<input type='radio' name='gender' value='male'>Male<br>
        <input type='radio' name='gender' value='female'>Female<br>
        <input type='radio' name='gender' value='other'>Other<br>
        dob:<input type='date' name='dob'><br>
        <input type='submit' value='Register'>
        </form>`)
})

app.post("/register", (req, res) => {
    res.cookie("registered",req.body,{maxAge:15000});
    res.send(`<h2>Registration Successful</h2>
        <a href='/details'>view details</a>`)
    })

app.get("/details", (req, res) => {
    const data=res.cokies.registered;
    if(!data){
        res.send(`<h2>Session Expired</h2>
        <a href='/'>Register Again</a>`)
    }
    const user=JSON.parse(data);
    res.send(`<h2>User Details</h2>
        Name:${user.name}<br>
        Contact:${user.contact}<br>
        Email:${user.email}<br>
        Address:${user.address}<br>
        Gender:${user.gender}<br>
        DOB:${user.dob}<br>
        <a href='/'>Register Again</a>`)
})
app.get("/logout",(req,res)=>{
    res.clearCookie("registered");
    res.redirect('/') 
}).listen(3000)
const express=require("express");
const app=express();
const session=require("express-session");
app.use(session({
    secret:"mysecret",
    resave:false,
    saveUninitialized:true
}))
app.use(express.ststic("public"));
app.post("/savesession",(req,res)=>{
    req.session.username=req.body.username;
    res.redirect("/fetchsession")
})
app.get("/fetcnsession",(req,res)=>{
    res.send(`<h2>Welcome ${req.session.username}</h2>
        <a href="/deletesession">Logout</a>`)
    })
app.get("/deletesession",(req,res)=>{
    req.session.desteroy(()=>{
        res.redirect("/")   
    })
}).listen(3000)
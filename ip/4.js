const express=require("express");
const app=express();
app.use(express.urlencoded({extended:true}));   

app.get("/",(req,res)=>{
    res.send(`<h2>User Signup FORM </h2>
        <form method="POST action="/data">
        RollNo:<input type="number"name=rollno><br>
        Name:<input type="text"name=name><br>
        Division:<input type="text"name=division><br>
        Email:<input type="email"name=email><br>
        Subject:<input type="radio"name="subject"value="FSD-2">FSD-2<br>
        <input type="radio"name="subject"value="COA">COA<br>
        <input type="radio"name="subject"value="PYTHON-2">PYTHON-2<br>
        <input type=radio"name="subject"value="DM">DM<br>
        <input type="radio"name="subject"value="TOC">TOC<br>
        <input type="submit"value="submit">
        </form>`)
    })
app.post("/data",(req,res)=>{
    res.send(`<h2>Student Details</h2>
        RollNo:${req.body.rollno}<br>
        Name:${req.body.name}<br>
        Division:${req.body.division}<br>   
        Email:${req.body.email}<br>
        Subject:${req.body.subject}<br>
        <a href='/'>back</a>`)
    }).listen(3000)

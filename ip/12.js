const express=require("express");
const app=express();

app.use(express.urlencoded({extended:true}));

app.get("/",(req,res)=>{
    res.send(`<h2>Student Form</h2>
        <form method="POST"action="student">
        Name:<input type="text"name="name"><br>
        Email:<input type="email"name="email"><br>
        Course:
        <input type="radio"name="course"value="CE">CE
        <input type="radio"name="course"value="IT">IT
        <input type="radio"name="course"value="CSE">CSE<br>
        <input type="submit"value="submit">
        </form>`)
    })

app.post("/student",(req,res)=>{
    res.send(`<h2>Student Details</h2>
        <p>Name:${req.body.name}</p>
        <p>Email:${req.body.email}</p>
        <p>Course:${req.body.course}</p>
        <a href='/'>back</a>`)
}).listen(3000)
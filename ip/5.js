const express=require("express");
const app=express();
const multer=require("multer");

const storage=multer.diksStorage({
    destination:(req,file,cb)=>{
        cb(null,"uploads/")
    },
    filename:(req,file,cb)=>{
        cb(null,file.originalname)
    }
})
const upload=multer({
    storage:storage,
    limits:{fileSize:1024*1024},
    fileFilter:(req,file,cb)=>{
        if(file.mimetype==="text/plain"){
            cb(null,true)
        }
        else{
            cb(new Error("Only text files are allowed"))
        }
    }
});

app.get("/",(req,res)=>{
    res.send(`<h2>File Upload Form</h2>
        <form method="POST"action="/upload"enctype="multipart/form-data">
        <input type="file"name="myfile"><br>
        <input type="submit"value="upload">
        </form>`)
    })

app.post("upload/",upload.single("myfile"),(req,res)=>{
    res.send(`<h2>File Uploaded Successfully</h2>
        <a href='/'>back</a>`)
}).listen(3000)
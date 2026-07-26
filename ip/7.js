const http=require("http");
const fs=require("fs");

http.createServer((req,res)=>{
    fs.readFile("7simple.html",(err,data)=>{
        if(err){
            res.write("File is Not Found");
        }
        else{
            res.writeHead(200,{"Content-Type":"text/html"});
            res.write(data);
        }   
        res.end();
    })
}).listen(3000)
const fs=require("fs");
fs.readFile("source.txt","utf8",(err,data)=>{
    if(err) throw err;
    console.log(data);
    fs.writeFile("destinaton.txt",data,(err)=>{
        if(err) throw err;
})
 console.log("File copied successfully");
})

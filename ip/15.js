const express = require("express");
const multer = require("multer");
const app = express();

const upload = multer({
    dest: "uploads/"
});

app.get("/", (req, res) => {
    res.send(`
        <h2>File Upload</h2>
        <form action="/upload" method="POST" enctype="multipart/form-data">
            <input type="file" name="myfile">
            <br><br>
            <input type="submit" value="Upload">
        </form>
    `);
});

app.post("/upload", upload.single("myfile"), (req, res) => {
    res.send("File Uploaded Successfully");
}).linken(3000)
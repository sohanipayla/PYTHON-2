const express = require("express");
const app = express();
app.use(express.urlencoded({ extended: true }));

app.post("/submit", (req, res) => {
    const { username, password, confirmPassword, gender } = req.body;
    if (password === confirmPassword) {
        res.send(`
            <h2>Form Submitted Successfully</h2>
            Username : ${username}<br>
            Password : ${password}<br>
            Gender : ${gender}
        `);
    } else {
        res.send(`
            <h2 style="color:red;">
                Password and Confirm Password do not match!
            </h2>
        `);
    }
}).listen(3000)
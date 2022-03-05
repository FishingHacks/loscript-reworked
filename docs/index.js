const ejs = require("ejs");
const express = require("express");

const app = express();
app.set("view-engine", "ejs");

app.get("*", (req, res) => {
    let url = req.url.substring(1).split("?")[0];
    if(url.endsWith("/") || url == "") url += "index";
    console.log(url+".ejs")
    res.render(url+".ejs");
});

app.listen(8080);
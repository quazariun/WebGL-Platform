var express = require("express");

var app = express();

var cors = require('cors');
app.use(cors())

app.listen(3000, () => {
    console.log("Server running on port 3000");
});

app.get("/Models/Geometries/:id", (req, res) => {
    let data = require('./Models/Geometries/' + req.params.id + '.json');
    res.json(data);
});

app.get("/Models/Maps/:id", (req, res) => {
    let data = require('./Models/Maps/' + req.params.id + '.json');
    res.json(data);
});
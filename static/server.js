//NodeJS
var express = require("express");
var app = express();
var http = require("http").Server(app);
var fs = require("fs");
var io = require("socket.io")(http);
var path = require('path');

console.log(__dirname, "/dist");

var text = "toto"

var encoded_text = Buffer.from(text).toString('base64')
app.use("/public", express.static(__dirname + "/dist"));

io.on("connection", function(socket) {
    fs.readFile(path.join(__dirname, "images", "watch.jpg"), function(err, data) {
        socket.emit("camera", { text: encoded_text, buffer: data });
        // socket.emit(
        //     "imageConversionByServer",
        //     "data:image/png;base64," + data.toString("base64")
        // );
    });
});

app.get("/", (req, res) => {
    res.sendfile(path.join(__dirname, "dist", "index.html"));
});
http.listen(3000, function() {
    console.log("listening on *:3000");
});

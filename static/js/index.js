import * as io from "socket.io-client";
var camera = document.getElementById("camera");
var socket = io.connect("http://" + document.domain + ":" + location.port);

// MODIFY THIS TO THE APPROPRIATE URL IF IT IS NOT BEING RUN LOCALLY

// var canvas = document.getElementById('canvas-video');
// var context = canvas.getContext('2d');
// var img = new Image();

// // show loading notice
// context.fillStyle = '#333';
// context.fillText('Loading...', canvas.width / 2 - 30, canvas.height / 3);
function b64(e) {
    var t = "";
    var n = new Uint8Array(e);
    var r = n.byteLength;
    for (var i = 0; i < r; i++) {
        t += String.fromCharCode(n[i]);
    }
    // var str = new TextDecoder("utf-8").decode(n);

    return window.btoa(t);
}
socket.on("connect", function() {
    console.log("connect");
    socket.emit("myevent", {
        data: "I'm connected!"
    });
});

socket.on("response", function(msg) {
    console.log("response", msg);
});

socket.on("camera", function(msg) {
    // var str = new TextDecoder("utf-8").decode(uint8Arr);
    // var base64String = b64(msg.buffer);
    // img.onload = function() {
    //     context.drawImage(img, 0, 0, canvas.width, canvas.height);
    //     console.log("load");
    // };
    console.log(msg.buffer);
    if (typeof msg.text === "string") {
        console.log(atob(msg.text));
    }
    camera.src = msg.buffer;
})

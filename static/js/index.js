import * as io from "socket.io-client";
var camera = document.getElementById('camera');
var socket = io.connect("http://" + document.domain + ":" + location.port);

// MODIFY THIS TO THE APPROPRIATE URL IF IT IS NOT BEING RUN LOCALLY

// var canvas = document.getElementById('canvas-video');
// var context = canvas.getContext('2d');
// var img = new Image();

// // show loading notice
// context.fillStyle = '#333';
// context.fillText('Loading...', canvas.width / 2 - 30, canvas.height / 3);

socket.on('connect', function() {
    console.log('connect')
    socket.emit('myevent', {
        data: 'I\'m connected!'
    });
});

socket.on('response', function(msg) {
    console.log('response', msg)
});

socket.on('camera', function(msg) {
    var uint8Arr = new Uint8Array(msg.buffer);
    var str = new TextDecoder("utf-8").decode(uint8Arr);
    var base64String = btoa(str);
    // img.onload = function() {
    //     context.drawImage(img, 0, 0, canvas.width, canvas.height);
    //     console.log("load");
    // };
    camera.src = 'data:image/jpg;base64,' + uint8Arr;
    // camera.src = img.src;   

});
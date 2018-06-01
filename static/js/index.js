import * as io from "socket.io-client";

var socket = io.connect("http://" + document.domain + ":" + location.port);
socket.on('connect', function() {
    console.log('connect')
    socket.emit('myevent', {
        data: 'I\'m connected!'
    });
});

socket.on('response', function(msg) {
    console.log('response', msg)
});

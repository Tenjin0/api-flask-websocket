import * as io from "socket.io-client";

var socket = io.connect("http://" + document.domain + ":" + location.port);
socket.on("connect", function() {
    // we emit a connected message to let knwo the client that we are connected.
    console.log('Websocket connected!');
});
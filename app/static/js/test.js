$(document).ready(function(){
    var socket = io.connect('https://' + document.domain + ':' + location.port + '/test', {secure: true});
    socket.on('connect', function(msg){
      console.log("test alert");
    });
    // var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    // socket.on('my response', function(msg) {
    //     $('#log').append('<p>Received: ' + msg.data + '</p>');
    // });
    // $('form#emit').submit(function(event) {
    //     socket.emit('my event', {data: $('#emit_data').val()});
    //     return false;
    // });
    // $('form#broadcast').submit(function(event) {
    //     socket.emit('my broadcast event', {data: $('#broadcast_data').val()});
    //     return false;
    // });
});
var http = require("http");

http.createServer(
    function (request, response){
        response.writeHead(200, {'Content-Type':'text/plain'});
        response.end("This is a Node JS Web Server");
    }
).listen(9009);

console.log('Server started at localhost:9009');
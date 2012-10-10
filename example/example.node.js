var app = require('http').createServer(handler)
  , io = require('socket.io').listen(app)
  , op = require('oppressive')(__dirname, io)
  , url = require('url')
  , fs = require('fs')
  , idx = fs.readFileSync('index.online.html');

function handler(req, res) {
    var path = url.parse(req.url).path.substr(1);
    res.writeHead(200);
    if(path in op.code) {
        // serve opressive client-side javascript
        res.end(op.code[path]);
    }
    else {
        // serve index
        res.end(idx);
    }
}

app.listen(8000);

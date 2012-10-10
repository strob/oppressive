// Load the socket.io library, and on completion define a socket
// object.

OP.ready = function(fn) {
    OP.onload = fn;
};

var $socketscript = document.createElement('script');
$socketscript.setAttribute('src', '/socket.io/socket.io.js');
$socketscript.onload = function() {
    console.log("loaded socket");
    OP.io = io.connect();
    if(OP.onload)
        OP.onload(OP);
}
console.log("loading socket");
document.head.appendChild($socketscript);

OP.Subjectification.load = function(jsonClassMap, cb) {
    var nrem = 0;

    for(var key in jsonClassMap) {
        nrem += 1;
        var cls = jsonClassMap[key];
        OP.io.emit("load", key, function(res) {
            nrem -= 1;
            for(var id in res) {
                var obj = new cls(id, res[id]);
                obj.save();
            }
            if(nrem == 0) {
                cb();
            }
        });
    }
};

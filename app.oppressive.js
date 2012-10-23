// Hold off until QT injection is complete
OP.ready = function(fn) {
    // race condition?
    if(qbridge) { fn(); }
    else { OP.onload = fn; }
};

OP.Subjectification.load = function(jsonClassMap, cb) {
    for(var key in jsonClassMap) {
        var cls = jsonClassMap[key];

        var res = JSON.parse(qbridge.load(key));
        
        for(var id in res) {
            var obj = new cls(id, res[id]);
            obj.save();
        }
    }
    cb();
};

// Hold off until QT injection is complete
OP.ready = function(fn) {
    // race condition?
    if(qbridge) { fn(); }
    else { OP.onload = fn; }
};

OP.Objection.prototype.save = function() {
    // XXX: Should _id be returned by a callback?
    qbridge.save(this.store, this._id, JSON.stringify(this.getDoc()));
};

OP.Subjectification.load = function(jsonClassMap, cb) {
    for(var key in jsonClassMap) {

        var cls = jsonClassMap[key];
        cls.prototype.store = key;

        var res = JSON.parse(qbridge.load(key));
        
        for(var id in res) {
            var obj = new cls(id, res[id]);
        }
    }
    cb();
};

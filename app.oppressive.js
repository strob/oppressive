OP.app = true;

OP.quote = function(x) {
    return encodeURI(x);
}

// Hold off until QT injection is complete
OP.ready = function(fn) {
    // race condition?
    if(window.qbridge !== undefined) { fn(); }
    else { OP.onload = fn; }
};

OP.Objection.prototype.save = function() {
    // XXX: Should _id be returned by a callback?
    qbridge.save(OP.quote(this.store), OP.quote(this._id), OP.quote(OP.JSON.stringify(this.getDoc())));
    this.onchange();
};
OP.Objection.prototype.deleteme = function() {
    qbridge.deleteme(OP.quote(this.store), OP.quote(this._id));
    this.ondelete();
};

OP.Subjectification.load = function(jsonClassMap, cb) {
    for(var key in jsonClassMap) {

        var cls = jsonClassMap[key];
        cls.prototype.store = key;

        var res = JSON.parse(qbridge.load(OP.quote(key)));
        
        for(var id in res) {
            var obj = new cls(id, res[id]);
        }
    }
    cb();
};

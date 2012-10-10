var OP = {};

// A poor-man's access to relational data.
OP.Objection = function(id, doc) {
    this._id = id;
    for(var k in doc) {
        this[k] = doc[k];
    }
};
OP.Objection.prototype.get = function(k) {
    return OP.Subjectification.obj[this[k]];
};
OP.Objection.prototype.getAll = function(ks) {
    return ks.map(function(k) { return this.get(k); });
};
OP.Objection.prototype.getDoc = function() {
    var doc = {};
    for(var key in this) {
        if(this.hasOwnProperty(key) && key !== '_id') {
            doc[key] = this[key];
        }
    }
    return doc;
};
OP.Objection.prototype.save = function() {
    OP.Subjectification.obj[this._id] = this;
};

// Load all object data on startup; anything too large for that can be
// asynchronously loaded.
OP.Subjectification = {
    obj: {},
    all: function(dtype) {
        var out = [];
        for(var key in OP.Subjectification.obj) {
            if(OP.Subjectification.obj[key] instanceof dtype) {
                out.push(OP.Subjectification.obj[key]);
            }
        }
        return out;
    }
};

// May be overwritten if necessary.
OP.ready = function(fn) {
    // XXX: wait for the DOM to populate?
    fn(OP);
};

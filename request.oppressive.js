OP.Subjectification.load =function(jsonClassMap, cb) {
    var nrem = 0;
    for(var jsonPath in jsonClassMap) {
        nrem += 1;
        (function(cls) {
            OP.UTIL.loadJson(jsonPath, function(res) {
                for(var key in res) {
                    var obj = new cls(key, res[key]);
                    obj.save();
                }
                nrem -= 1;
                if(nrem === 0) {
                    cb();
                }
            });
        })(jsonClassMap[jsonPath])
    }
};

OP.UTIL = {};
OP.UTIL.load = function(uri, cb) {
    var req = new XMLHttpRequest();
    req.open("GET", uri, true);

    req.onreadystatechange = function() { 
        if(req.readyState == 4) {
            if(req.status == 200) {
                cb(req.responseText);
            }
            else {
                console.log("error loading " + uri, req.status);
            }
        }
    };
    req.send();
};
OP.UTIL.loadJson = function (uri, cb) {
    OP.UTIL.load(uri, function(txt) { cb(JSON.parse(txt)); });
};

// All of these `js' files must be json objects wrapped in an `offload' call.
// See `script/json2js.py' for reference transformation implementation.
OP.Subjectification.load = function(jsClassMap, cb) {

    var make_load_function = function(cls) {
        return (function(res) {
            for(var key in res) {
                var obj = new cls(key, res[key]);
            }
            load_next();
        });
    }

    var jspaths = [];
    var jsidx = 0;

    for(var jspath in jsClassMap) {
        jspaths.push(jspath);
    }

    var load_next = function() {
        if(jsidx >= jspaths.length) {
            return cb();
        }

        var jspath = jspaths[jsidx];

        window.offload = make_load_function(jsClassMap[jspath]);

        var $el = document.createElement('script');
        $el.setAttribute('src', jspath + '.js');
        document.body.appendChild($el);

        jsidx += 1;
    }

    load_next();
};

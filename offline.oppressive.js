// All of these `js' files must be json objects wrapped in an `offload' call.
// See `script/json2js.py' for reference transformation implementation.
OP.Subjectification.load = function(jsClassMap, cb) {

    var nrem = 0;

    var make_load_function = function(cls) {
        return (function(res) {
            nrem -= 1;
            for(var key in res) {
                var obj = new cls(key, res[key]);
                obj.save();
            }

            console.log("nrem", nrem);
            if(nrem === 0) {
                cb();
            }
        });
    }

    for(var jspath in jsClassMap) {
        nrem += 1;

        window.offload = make_load_function(jsClassMap[jspath]);

        var $el = document.createElement('script');
        $el.setAttribute('src', jspath + '.js');
        document.body.appendChild($el);
    }
};

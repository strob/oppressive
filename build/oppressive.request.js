var OP={Objection:function(a,c){this._id=a;for(var b in c)this[b]=c[b]}};OP.Objection.prototype.get=function(a){return OP.Subjectification.obj[this[a]]};OP.Objection.prototype.getAll=function(a){return a.map(function(a){return this.get(a)})};OP.Objection.prototype.getDoc=function(){var a={},c;for(c in this)this.hasOwnProperty(c)&&"_id"!==c&&(a[c]=this[c]);return a};OP.Objection.prototype.save=function(){OP.Subjectification.obj[this._id]=this};
OP.Subjectification={obj:{},all:function(a){var c=[],b;for(b in OP.Subjectification.obj)OP.Subjectification.obj[b]instanceof a&&c.push(OP.Subjectification.obj[b]);return c}};OP.ready=function(a){a(OP)};OP.Subjectification.load=function(a,c){var b=0,d;for(d in a)b+=1,function(a){OP.UTIL.loadJson(d+".json",function(d){for(var e in d)(new a(e,d[e])).save();b-=1;0===b&&c()})}(a[d])};OP.UTIL={};OP.UTIL.load=function(a,c){var b=new XMLHttpRequest;b.open("GET",a,!0);b.onreadystatechange=function(){4==b.readyState&&(200==b.status?c(b.responseText):console.log("error loading "+a,b.status))};b.send()};OP.UTIL.loadJson=function(a,c){OP.UTIL.load(a,function(a){c(JSON.parse(a))})};

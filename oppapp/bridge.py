from PyQt4 import QtCore

import json
import os
import codecs
import urllib2

def unquote(x):
    return urllib2.unquote(x)

class OppressiveBridge(QtCore.QObject):
    def __init__(self, basepath='.'):
        QtCore.QObject.__init__(self)
        self.basepath = basepath
        self.STATE = {}

    def jsonpath(self, uid):
        return os.path.join(self.basepath, uid) + '.json'

    @QtCore.pyqtSlot(str, result=str)
    def load(self, path):
        path = unquote(path)

        # XXX: Think about (abs/rel)paths for bundled applications
        if path not in self.STATE:
            print 'jsonpath', self.jsonpath(path)
            if os.path.exists(self.jsonpath(path)):
                self.STATE[path] = json.load(open(self.jsonpath(path)))
            else:
                print 'cache fail'
                self.STATE[path] = {}

        return json.dumps(self.STATE[path])

    @QtCore.pyqtSlot(str, str, str)
    def save(self, store, _id, doc):
        store, _id, doc = unquote(store), unquote(_id), unquote(doc) # QStrings can cause problems.
        print 'got doc', doc
        self.STATE[store][_id] = json.loads(doc)
        print 'now it is', self.STATE[store][_id]
        # XXX: Think about a better way to do this.
        json.dump(self.STATE[store], open(self.jsonpath(store), 'w'))

    @QtCore.pyqtSlot(QtCore.QString)
    def echo(self, blargh):
        # print blargh
        print unquote(blargh)

    def inject(self, webview):
        frame = webview.page().mainFrame()
        frame.addToJavaScriptWindowObject("qbridge", self)
        frame.evaluateJavaScript("if(OP && OP.onload) { console.log('onload'); OP.onload(); }\n else { console.log('noop'); }")

    @QtCore.pyqtSlot(str, str)
    def deleteme(self, store, _id):
        store, _id = unquote(store), unquote(_id)
        del self.STATE[store][_id]

        json.dump(self.STATE[store], open(self.jsonpath(store), 'w'))

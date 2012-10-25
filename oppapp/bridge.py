from PyQt4 import QtCore

import json
import os

class OppressiveBridge(QtCore.QObject):
    def __init__(self, basepath='.'):
        QtCore.QObject.__init__(self)
        self.basepath = basepath
        self.STATE = {}

    def jsonpath(self, uid):
        return os.path.join(self.basepath, uid) + '.json'

    @QtCore.pyqtSlot(str, result=str)
    def load(self, path):
        path = str(path)

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
        store, _id, doc = str(store), str(_id), str(doc) # QStrings can cause problems.
        self.STATE[store][_id] = json.loads(doc)

        # XXX: Think about a better way to do this.
        json.dump(self.STATE[store], open(self.jsonpath(store), 'w'))

    def inject(self, webview):
        frame = webview.page().mainFrame()
        frame.addToJavaScriptWindowObject("qbridge", self)
        frame.evaluateJavaScript("if(OP && OP.onload) { OP.onload(); }\n else { console.log('noop'); }")
        

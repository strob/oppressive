# PyQt-based application engine for persistent oppressive sketches.

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import QtWebKit

import json

import sys
import os

app = QtGui.QApplication(sys.argv)
app.setApplicationName('appressive')

class OppressiveBridge(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)
        self.STATE = {}

    @QtCore.pyqtSlot(str, result=str)
    def load(self, path):
        path = str(path)

        # XXX: Think about (abs/rel)paths for bundled applications
        if path not in self.STATE:
            if os.path.exists(path + '.json'):
                self.STATE[path] = json.load(open(path + '.json'))
            else:
                self.STATE[path] = {}

        return json.dumps(self.STATE[path])

    @QtCore.pyqtSlot(str, str, str)
    def save(self, store, _id, doc):
        store, _id, doc = str(store), str(_id), str(doc) # QStrings can cause problems.
        self.STATE[store][_id] = json.loads(doc)

        # XXX: Think about a better way to do this.
        json.dump(self.STATE[store], open(store + '.json', 'w'))

web = QtWebKit.QWebView()

web.settings().setAttribute(QtWebKit.QWebSettings.DeveloperExtrasEnabled, True)

base = os.path.abspath('.') + '/'
web.setHtml(open("../example/index.html").read(), baseUrl=QtCore.QUrl.fromLocalFile(base))

bridge = OppressiveBridge()
frame = web.page().mainFrame()
frame.addToJavaScriptWindowObject("qbridge", bridge);
frame.evaluateJavaScript("console.log('opping'); \nif(OP && OP.onload) { OP.onload(); }\n else { console.log('noop'); }");

web.show()

if __name__=='__main__':
    app.exec_()

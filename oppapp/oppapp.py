# PyQt-based application engine for persistent oppressive sketches.

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import QtWebKit

import json

import sys

app = QtGui.QApplication(sys.argv)
app.setApplicationName('appressive')

class OppressiveBridge(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)
        self.STATE = {}

    @QtCore.pyqtSlot(str, result=str)
    def load(self, path):
        print "LOAD", path
        # XXX: Think about paths for bundled applications
        if path not in self.STATE:
            print "cache fail"
            self.STATE[path] = json.load(open(path + '.json'))
        print "dump & return"
        return json.dumps(self.STATE[path])

web = QtWebKit.QWebView()

web.settings().setAttribute(QtWebKit.QWebSettings.DeveloperExtrasEnabled, True)

web.load(QtCore.QUrl("../example/index.app.html"))

bridge = OppressiveBridge()
frame = web.page().mainFrame()
frame.addToJavaScriptWindowObject("qbridge", bridge);
frame.evaluateJavaScript("console.log('evaluation');");
frame.evaluateJavaScript("OP.onload();");

web.show()

if __name__=='__main__':
    app.exec_()

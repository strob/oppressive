# PyQt-based application engine for persistent oppressive sketches.

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import QtWebKit

import json

import sys
import os

from bridge import OppressiveBridge

app = QtGui.QApplication(sys.argv)
app.setApplicationName('appressive')

web = QtWebKit.QWebView()

web.settings().setAttribute(QtWebKit.QWebSettings.DeveloperExtrasEnabled, True)

base = os.path.abspath('.') + '/'
web.setHtml(open("../example/index.html").read(), baseUrl=QtCore.QUrl.fromLocalFile(base))

bridge = OppressiveBridge()
frame = web.page().mainFrame()
frame.addToJavaScriptWindowObject("qbridge", bridge);
frame.evaluateJavaScript("if(OP && OP.onload) { OP.onload(); }\n else { console.log('noop'); }");

web.show()

if __name__=='__main__':
    app.exec_()

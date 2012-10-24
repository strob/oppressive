# PyQt-based application engine for persistent oppressive sketches.

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import QtWebKit


import sys
import os

from bridge import OppressiveBridge

app = QtGui.QApplication(sys.argv)
app.setApplicationName('appressive')

web = QtWebKit.QWebView()

web.settings().setAttribute(QtWebKit.QWebSettings.DeveloperExtrasEnabled, True)

base = os.path.abspath('.') + '/'
web.setHtml(open("../example/index.html").read(), baseUrl=QtCore.QUrl.fromLocalFile(base))

bridge = OppressiveBridge(basepath='../example')
bridge.inject(web)
web.show()

if __name__=='__main__':
    app.exec_()

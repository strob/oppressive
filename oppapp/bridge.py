from PyQt4 import QtCore

import json
import os

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

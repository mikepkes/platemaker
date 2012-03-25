# Created by Michael Kessler, 2012
"""Scene model for representing 3d objects"""

import sys
try:
	from PyQt4 import QtCore,QtGui
except ImportError, exc:
	from PySide import QtCore

class PlateScene(QtCore.QAbstractListModel):
	def __init__(self, parent=None):
		QtCore.QAbstractListModel.__init__(self, parent)
	def data(self, index, role):
		row = index.row()
		return QtCore.QVariant("Test")
	def rowCount(self, parent):
		return 3
	def columnCount(self, parent):
		return 2

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	w = QtGui.QListView()
	m = PlateScene()
	w.setModel(m)
	w.show()
	app.exec_()


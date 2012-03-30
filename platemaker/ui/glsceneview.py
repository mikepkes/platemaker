# Created by Michael Kessler, 2012
"""OpenGL view for a scene."""

import sys
import platemaker.model.scene

try:
    from PyQt4 import QtGui, QtCore
    from PyQt4.QtOpenGL import *
except ImportError, exc:
    from PySide import QtGui, QtCore
    from PySide.QtOpenGL import *

try:
    from OpenGL.GL import * #pylint: disable-msg=W0614
    from OpenGL.GLU import * #pylint: disable-msg=W0614
except Exception, exc:
    print "Could not initialize OpenGL.", exc
    sys.exit(1)


class GlSceneView(QGLWidget, QtGui.QAbstractItemView):
    def __init__(self, parent=None):
	QGLWidget.__init__(self, parent)
	self.cameraRotate = [0, 0, 0]
	self.cameraTranslate = [0, 0, -20]
	self.model = None

    def setModel(self, model):
	self.model = model

    def bakeItem(self, index):
	_index = self.model.index(index, 0, QtCore.QModelIndex())
	node = self.model.nodeFromIndex(_index)

        node.drawList = glGenLists(1)
        glNewList(node.drawList, GL_COMPILE)

        glBegin(GL_TRIANGLES)
        for polygon in node.polygons:
            for vertex in polygon.vertex:
                glVertex3f( vertex[0], vertex[1], vertex[2] )
                glNormal3f( polygon.nx, polygon.ny, polygon.nz )
        glEnd()
        glEndList()


    def initializeGL(self):
        """
        GL Setup Routine
        """
        glEnable( GL_LIGHTING )
        glColorMaterial ( GL_FRONT_AND_BACK, GL_DIFFUSE )
        glEnable ( GL_COLOR_MATERIAL )
        glEnable(GL_LIGHT0)
        glShadeModel (GL_SMOOTH)
        glEnable(GL_DEPTH_TEST)
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.1, 0.1, 0.1, 0] )
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [.2, .2, .2, 0])
        glLightfv(GL_LIGHT0, GL_SPECULAR, [0, 0, 0, 0])
	self.x = 1.0
	self.y = 1.0

    def paintGL(self):
	"""Drawing Routine"""
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glMatrixMode( GL_PROJECTION )
	glLoadIdentity()
	#glOrtho(-5, 5, -5, 5, .1, 100)

	ratio = float(self.x) / float(self.y)
	gluPerspective(30.0, ratio, 0.1, 1000)

	glMatrixMode( GL_MODELVIEW )
	glLoadIdentity()
	glLightfv(GL_LIGHT0, GL_POSITION, (100, 100, 100))

	glTranslate(
		self.cameraTranslate[0],
		self.cameraTranslate[1],
		self.cameraTranslate[2] )
	glRotate( -45, 1, 0, 0 )
	glRotate( self.cameraRotate[0], 1, 0, 0)
	glRotate( self.cameraRotate[1], 0, 1, 0)
	glRotate( self.cameraRotate[2], 0, 0, 1)
	glScale( 0.1, 0.1, 0.1 )
	
	index = self.model.index(0, 0, QtCore.QModelIndex())
	node = self.model.nodeFromIndex(index)
	glCallList(node.drawList)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = GlSceneView()
    m = platemaker.model.scene.SceneModel()
    m.addBranch(QtCore.QModelIndex(), 'BigGearMod', '/Users/mkessler/Downloads/biggearmod_fixed-1.stl')
    w.setModel(m)
    w.show()
    w.bakeItem(0);
    app.exec_()

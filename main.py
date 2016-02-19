from PyQt4 import QtCore, QtGui
from viewController import *

ticketNumber = '3111111111111'
app = QtGui.QApplication(sys.argv)
myapp = MyForm(ticketNumber)
myapp.show()
sys.exit(app.exec_())
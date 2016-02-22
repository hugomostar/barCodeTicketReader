from PyQt4 import QtCore, QtGui
from viewController import *

app = QtGui.QApplication(sys.argv)
myapp = MyForm()
myapp.show()
sys.exit(app.exec_())


#if __name__ == "__main__":
# app = QtGui.QApplication(sys.argv)
# myapp = MyForm()
# myapp.show()
# sys.exit(app.exec_())
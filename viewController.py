import sys

from PyQt4 import QtCore, QtGui
from mainView import Ui_MainWindow
from ticketStatus import *

class MyForm(QtGui.QMainWindow):

    ticketNumber = ''
    def __init__(self, ticketNumber, parent=None):
        self.ticketNumber = ticketNumber
        ticketStatus()
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.showFullScreen()
        self.ui.pushButton.clicked.connect(self.checkIsTicketValid)
    def checkIsTicketValid(self):
        self.status = ticketStatus.checkTicketNumber(self.ticketNumber)
        if self.status == 'ok':
            self.ui.textEdit.setText('Tiket je validiran, mozete krenuti prema izlazu!')
            print (self.status)
        else:
            self.ui.textEdit.setText('Dogodila se pogreska, pokusajte ponovo!')
            print (self.status)

#if __name__ == "__main__":
# app = QtGui.QApplication(sys.argv)
# myapp = MyForm()
# myapp.show()
# sys.exit(app.exec_())
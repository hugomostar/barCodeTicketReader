import sys

from PyQt4 import QtCore, QtGui
from mainView import Ui_ticketReaderView, _translate
from ticketStatus import *

class MyForm(QtGui.QMainWindow):

    def __init__(self, parent=None):
        self.ticketNumber = ''
        ticketStatus()
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_ticketReaderView()
        self.ui.setupUi(self)
        #self.showFullScreen()
    def keyPressEvent(self, event):
         key = event.key()
         if key != QtCore.Qt.Key_Return:
             self.ticketNumber+=chr(key)
             print('pressed: ', chr(key))
         if key == QtCore.Qt.Key_Return:
            print('Ticket:', self.ticketNumber)
            self.checkIsTicketValid()
            self.ticketNumber = ''

    def checkIsTicketValid(self):
        self.status = ticketStatus.checkTicketNumber(self.ticketNumber)
        if self.status == 'ok':
            self.ui.textEdit.setHtml(_translate("ticketReaderView", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#eeeeee;\"><span style=\" font-family:\'Consolas,Menlo,Monaco,Lucida Console,Liberation Mono,DejaVu Sans Mono,Bitstream Vera Sans Mono,Courier New,monospace,sans-serif\'; font-size:28pt; font-weight:600; color:#3117c7; background-color:#eeeeee;\">Vaš tiket je validiran <br /> za izlaz!<br /> </span></p></body></html>", None))
            print (self.status)
        else:
            self.ui.textEdit.setHtml(_translate("ticketReaderView", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#eeeeee;\"><span style=\" font-family:\'Consolas,Menlo,Monaco,Lucida Console,Liberation Mono,DejaVu Sans Mono,Bitstream Vera Sans Mono,Courier New,monospace,sans-serif\'; font-size:28pt; font-weight:600; color:#3117c7; background-color:#eeeeee;\">Dogodila se pogreška! <br /> Pokušajte ponovo!<br /> </span></p></body></html>", None))
            print (self.status)
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ticketreaderview.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ticketReaderView(object):
    def setupUi(self, ticketReaderView):
        ticketReaderView.setObjectName(_fromUtf8("ticketReaderView"))
        ticketReaderView.resize(480, 320)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ticketReaderView.sizePolicy().hasHeightForWidth())
        ticketReaderView.setSizePolicy(sizePolicy)
        ticketReaderView.setMaximumSize(QtCore.QSize(480, 320))
        ticketReaderView.setAutoFillBackground(False)

        self.centralWidget = QtGui.QWidget(ticketReaderView)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.centralWidget.setStyleSheet("background-color: #0000FF");
        self.verticalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-10, 0, 502, 271))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.textEdit = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setFrameStyle(0)
        self.textEdit.setEnabled(False)
        self.textEdit.setMinimumSize(QtCore.QSize(500, 90))
        self.textEdit.setMaximumSize(QtCore.QSize(500, 90))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setMargin(11)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))

        locationGif = r'arrow.gif'
        self.arrow = QtGui.QLabel(self.verticalLayoutWidget)
        self.arrow.setAlignment(QtCore.Qt.AlignHCenter)
        movie = QtGui.QMovie(locationGif)
        movie.setScaledSize(QtCore.QSize(140, 140))
        self.arrow.setMovie(movie)
        movie.start()
        self.arrow.setLayout(QtGui.QHBoxLayout())
        #self.arrow.layout().addWidget(QLabel('Loading...'))
        self.arrow.setObjectName(_fromUtf8("arrow"))
        self.verticalLayout_3.addWidget(self.arrow, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        ticketReaderView.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(ticketReaderView)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        ticketReaderView.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(ticketReaderView)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        ticketReaderView.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(ticketReaderView)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        ticketReaderView.setStatusBar(self.statusBar)

        self.retranslateUi(ticketReaderView)
        QtCore.QMetaObject.connectSlotsByName(ticketReaderView)

    def retranslateUi(self, ticketReaderView):
        ticketReaderView.setWindowTitle(_translate("ticketReaderView", "ticketReaderView", None))
        self.textEdit.setHtml(_translate("ticketReaderView", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#0000FF;\"><span style=\" font-family:\'Consolas,Menlo,Monaco,Lucida Console,Liberation Mono,DejaVu Sans Mono,Bitstream Vera Sans Mono,Courier New,monospace,sans-serif\'; font-size:28pt; font-weight:600; color:#ffffff; background-color:#0000FF;\">Molimo nanesite <br /> vaš tiket<br /> </span></p></body></html>", None))

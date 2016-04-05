# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConvertFromQtToPy.ui'
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

class Ui_ConverterUitoPy(object):
    def setupUi(self, ConverterUitoPy):
        ConverterUitoPy.setObjectName(_fromUtf8("ConverterUitoPy"))
        ConverterUitoPy.resize(524, 251)
        ConverterUitoPy.setDocumentMode(True)
        self.centralWidget = QtGui.QWidget(ConverterUitoPy)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 120, 291, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 120, 71, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 120, 121, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_3 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 160, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 160, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(130, 20, 151, 91))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("LogoConverter.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        ConverterUitoPy.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(ConverterUitoPy)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 524, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        ConverterUitoPy.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(ConverterUitoPy)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        ConverterUitoPy.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(ConverterUitoPy)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        ConverterUitoPy.setStatusBar(self.statusBar)
        self.actionOpen = QtGui.QAction(ConverterUitoPy)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionClose = QtGui.QAction(ConverterUitoPy)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(ConverterUitoPy)
        QtCore.QMetaObject.connectSlotsByName(ConverterUitoPy)

    def retranslateUi(self, ConverterUitoPy):
        ConverterUitoPy.setWindowTitle(_translate("ConverterUitoPy", "MainWinTraining", None))
        self.label.setText(_translate("ConverterUitoPy", "QT File Path", None))
        self.pushButton.setText(_translate("ConverterUitoPy", "Select File Path", None))
        self.pushButton_3.setText(_translate("ConverterUitoPy", "Generate", None))
        self.label_2.setText(_translate("ConverterUitoPy", "Done By AZAHID@mu-e.com", None))
        self.menuFile.setTitle(_translate("ConverterUitoPy", "File", None))
        self.actionOpen.setText(_translate("ConverterUitoPy", "Open", None))
        self.actionClose.setText(_translate("ConverterUitoPy", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ConverterUitoPy = QtGui.QMainWindow()
    ui = Ui_ConverterUitoPy()
    ui.setupUi(ConverterUitoPy)
    ConverterUitoPy.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Converter.py'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import ConvertFromQtToPy
import os
from subprocess import Popen

class  converter(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.Win = ConvertFromQtToPy.Ui_ConverterUitoPy()
        self.Win.setupUi(self)

        QtCore.QObject.connect(self.Win.pushButton,QtCore.SIGNAL("clicked()"),self.Ui_PathFile)
        QtCore.QObject.connect(self.Win.pushButton_3,QtCore.SIGNAL("clicked()"),self.Convert)


        self.Win.actionClose .triggered.connect(self.close_application)


    def Ui_PathFile(self):
        Ui_path = QtGui.QFileDialog.getOpenFileName(self, 'OpenFile')
        self.Win.lineEdit.setText(Ui_path)

    def Py_PathFile(self):
        Py_path = QtGui.QFileDialog.getOpenFileName(self, 'OpenFile')
        self.Win.lineEdit_2.setText(Py_path)

    def to_string(self,my_list):
        result = ''
        last = len(my_list) - 1
        for pos, elem in enumerate(my_list):
            result += elem
            if pos != last:
                result += ''
        return result

    def Convert(self):
        s1 = self.to_string(str(self.Win.lineEdit.text()))
        print s1
        s2= s1.split("/")
        str1 = ''
        print s2
        for  i in range(0,len(s2) - 1):
           str1 = str1 + s2[i] + '/'
        cmd1 = 'cd ' + str1
        string1 = self.to_string(s2[-1:])
        string2 =  string1.replace(".ui",".py")
        print cmd1

        cmd2 = 'C:\Python27\Lib\site-packages\PyQt4\pyuic4.bat  -x  ' + string1 + ' -o ' +  string2
        print string1
        print string2
        print cmd2
        BatFile = str1+'Converter.bat'
        with open(BatFile, "w") as f1:
                f1.write(cmd1)
                f1.write('\n')
                f1.write(cmd2)
                print "file created"

        p = Popen(BatFile, cwd=r""+str1)
        stdout, stderr = p.communicate()
        #os.remove(BatFile)

    def close_application(self):
        print("closed ...!!")
        sys.exit()

    def openfile(self) :
        print "ok"


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ConvWin = converter()
    ConvWin.show()
    sys.exit(app.exec_())
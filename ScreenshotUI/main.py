import sys
from mainwindow import Mymainwindow 
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Mymainwindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
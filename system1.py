from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import matplotlib.pyplot as plt
from system2 import Ui_MainWindow1

db=sqlite3.connect('travel.db')
cr=db.cursor()

class Ui_MainWindow(object):
    
    def nextwindow1(self):
        username=self.lineEdit.text()
        password=self.lineEdit_2.text()
        if (username == 'admin' and password == 'admin123'):
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow1()
            self.ui.setupUi(self.window)
            MainWindow.hide()
            self.window.show()
        else:
            self.warning1('Alert','You are not admin')
            
    def warning1(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
        
    def nextwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.setupUi1(self.window)
        MainWindow.hide()
        self.window.show()
        
    def loaddata(self):
        name = self.login()
        result = cr.execute('select place,pickup_point from data where uname=?',(name,))                                 
        self.tableWidget1.setRowCount(1)
        
        for row_no, row_data in enumerate(result):
            self.tableWidget1.insertRow(row_no)
            for col_no, data in enumerate(row_data):
                self.tableWidget1.setItem(row_no,col_no,QtWidgets.QTableWidgetItem(str(data)))
     
    def warning(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    
    def login(self):
        username=self.lineEdit.text()
        password=self.lineEdit_2.text()
        list = []
        list1 = []
        cr.execute('select uname,pword from login where uname=?',(username,))
        for row1 in cr.fetchall():
            list.append(row1 [0])
            list1.append(row1 [1])
        
        if(username==list[0] and password==list1[0]):
            self.nextwindow()
            
        else:
            self.warning('Alert','check username or password')
            
        return(username)
        
    def graph(self):
        name = self.login()
        list = []
        list1 = []
        cr.execute('select place,pickup_point from data where uname=?',(name,))
        for row in cr.fetchall():
            list.append(row [0])
            list1.append(row [1])


        slice=[list1]
        activity=(list)
        colors=['b','g','r','c','m','y','k','w']
        plt.title('Graph Analysis')
        plt.pie(slice,labels=activity,colors=colors,startangle=90,autopct='%.1f%%')
        plt.show(block=False)
        plt.pause(7)
        plt.close()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(662, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 90, 121, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 140, 121, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(340, 90, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 140, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login)
        self.pushButton.clicked.connect(self.loaddata)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 220, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(-20, -10, 741, 401))
        self.graphicsView.setStyleSheet("background-image: url(E:/Project/Python/img/regis.jpg);")
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 220, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.nextwindow1)
        self.graphicsView.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.lineEdit_2.clear)
        self.pushButton_2.clicked.connect(self.lineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Username</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Password</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.pushButton_4.setText(_translate("MainWindow", "Admin"))
        
    def setupUi1(self, vtn_load):
        vtn_load.setObjectName("vtn_load")
        vtn_load.resize(403, 373)
        self.centralwidget = QtWidgets.QWidget(vtn_load)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget1 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget1.setGeometry(QtCore.QRect(90, 90, 221, 171))
        self.tableWidget1.setRowCount(3)
        self.tableWidget1.setColumnCount(2)
        self.tableWidget1.setObjectName("tableWidget1")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(1, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-30, -30, 871, 511))
        self.label.setStyleSheet("background-image: url(E:/Project/Python/img/regis.jpg);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 30, 201, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 290, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.graph)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 290, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(QtWidgets.qApp.quit)
        self.label.raise_()
        self.tableWidget1.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        vtn_load.setCentralWidget(self.centralwidget)

        self.retranslateUi1(vtn_load)
        QtCore.QMetaObject.connectSlotsByName(vtn_load)

    def retranslateUi1(self, vtn_load):
        _translate = QtCore.QCoreApplication.translate
        vtn_load.setWindowTitle(_translate("vtn_load", "MainWindow"))
        item = self.tableWidget1.horizontalHeaderItem(0)
        item.setText(_translate("vtn_load", "Place"))
        item = self.tableWidget1.horizontalHeaderItem(1)
        item.setText(_translate("vtn_load", "Total Pickups"))
        self.label_2.setText(_translate("vtn_load", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Record of Employee</span></p></body></html>"))
        self.pushButton.setText(_translate("vtn_load", "Result"))
        self.pushButton_2.setText(_translate("vtn_load", "Exit"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

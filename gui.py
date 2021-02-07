from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 91, 61))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 90, 91, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 90, 91, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_5.setGeometry(QtCore.QRect(120, 10, 64, 23))
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_6.setGeometry(QtCore.QRect(200, 10, 64, 23))
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.lcdNumber_7 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_7.setGeometry(QtCore.QRect(120, 50, 64, 23))
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        self.lcdNumber_8 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_8.setGeometry(QtCore.QRect(200, 50, 64, 23))
        self.lcdNumber_8.setObjectName("lcdNumber_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 160, 421, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 230, 201, 41))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 434, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.on_click)
        self.pushButton_2.clicked.connect(self.on_click2)
        self.pushButton_6.clicked.connect(self.on_click3)

    def on_click3(self):
            exec(open("opencv_object_tracking.py").read())
    def on_click2(self):
            exec(open("live.py").read())
        
    def on_click(self):
        import cv2
        from time import sleep

        signal1 = cv2.imread('Images/1.jpg')
        signal2 = cv2.imread('Images/2.jpg')
        signal3 = cv2.imread('Images/3.jpg')
        signal4 = cv2.imread('Images/4.jpg')

        car_cascade = cv2.CascadeClassifier('cars.xml')
        gray = cv2.cvtColor(signal1, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        i_1=0
        i_2=0
        i_3=0
        i_4=0
        for (x, y, w, h) in cars:
                cv2.rectangle(signal1, (x, y), (x + w, y + h), (0, 0, 255), 2)
                i_1=i_1+1
        text="Number of cars = "+str(i_1)
        cv2.putText(signal1, text,(100,200),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)
        cv2.namedWindow('signal 1')
        cv2.moveWindow('signal 1',100,100)
        cv2.imshow('signal 1', signal1)
        cv2.waitKey()
        print(text+" at signal 1")

        gray = cv2.cvtColor(signal2, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        for (x, y, w, h) in cars:
                cv2.rectangle(signal2, (x, y), (x + w, y + h), (0, 0, 255), 2)
                i_2 = i_2 + 1
        text="Number of cars = "+str(i_2)
        cv2.putText(signal2, text,(100,200),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)
        cv2.namedWindow('signal 2')
        cv2.moveWindow('signal 2',420,100)
        cv2.imshow('signal 2', signal2)
        cv2.waitKey()
        print(text+" at signal 2")

        gray = cv2.cvtColor(signal3, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        for (x, y, w, h) in cars:
                cv2.rectangle(signal3, (x, y), (x + w, y + h), (0, 0, 255), 2)
                i_3 = i_3 + 1
        text = "Number of cars = " + str(i_3)
        cv2.putText(signal3, text, (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.namedWindow('signal 3')
        cv2.moveWindow('signal 3',100,365)
        cv2.imshow('signal 3', signal3)
        cv2.waitKey()
        print(text+" at signal 3")

        gray = cv2.cvtColor(signal4, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        for (x, y, w, h) in cars:
                cv2.rectangle(signal4, (x, y), (x + w, y + h), (0, 0, 255), 2)
                i_4 = i_4 + 1
        text = "Number of cars = " + str(i_4)
        cv2.putText(signal4, text, (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.namedWindow('signal 4')
        cv2.moveWindow('signal 4',420,365)
        cv2.imshow('signal 4', signal4)
        cv2.waitKey()
        cv2.destroyAllWindows()
        print(text+" at signal 4")

        print("========================================")
        traffic=[i_1,i_2,i_3,i_4]
        index=[]
        if max(traffic)==i_1:
                print("Traffic at signal 1 is maximum")
        if max(traffic)==i_2:
                print("Traffic at signal 2 is maximum")
        if max(traffic)==i_3:
                print("Traffic at signal 3 is maximum")
        if max(traffic)==i_4:
                print("Traffic at signal 4 is maximum")
        print("========================================")
        self.lcdNumber_5.display(i_1)
        self.lcdNumber_6.display(i_2)
        self.lcdNumber_7.display(i_3)
        self.lcdNumber_8.display(i_4)
        traffic.sort(reverse=True)
        print(traffic)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Traffic\n"
" per\n"
" Road"))
        self.pushButton_2.setText(_translate("MainWindow", "Live Feed\n"
" Camera 1"))
        self.pushButton_6.setText(_translate("MainWindow", "Live \n"
" Tracking"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
from MainLogin import Ui_LoginWindow
from registrationNew import Ui_registrationPage
import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('BankNH.db')
        self.create_table()

    def create_table(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS NEWBANK(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            USERNAME CHAR(20) NOT NULL,
            FIRSTNAME TEXT NOT NULL,
            LASTNAME TEXT NOT NULL,
            EMAIL TEXT NOT NULL,
            PASSWORD TEXT NOT NULL,
            CONFIRM_PASSWORD TEXT NOT NULL,
            PHONE CHAR(11) NOT NULL,
            SEX TEXT,
            ADDRESS CHAR(50) NOT NULL);''')

class Ui_Page(object):
    def setupUi(self, WelcomePage):
        WelcomePage.setObjectName("WelcomePage")
        self.window = WelcomePage 
        WelcomePage.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(WelcomePage)
        self.centralwidget.setObjectName("centralwidget")


        self.centralwidget.setStyleSheet("""
QWidget#centralwidget {
    border-image: url(bank.jpg) 0 0 0 0 stretch stretch;
}
""")




        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)


        self.overlay = QtWidgets.QWidget()
        self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 120);")
        main_layout.addWidget(self.overlay)


        self.verticalLayout = QtWidgets.QVBoxLayout(self.overlay)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setContentsMargins(50, 80, 50, 80)
        self.verticalLayout.setAlignment(QtCore.Qt.AlignCenter)


        self.label = QtWidgets.QLabel("Welcome to BOI Bank Limited")
        self.label.setStyleSheet("font: bold 36pt 'Arial'; color: white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label)


        self.label_2 = QtWidgets.QLabel("Do You Have An Existing Account?")
        self.label_2.setStyleSheet("font: 26pt 'Arial'; color: white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_2)


        button_style = """
        QPushButton {
             background-color: #3498db;
             color: white;
             font: bold 16pt 'Arial';
             padding: 14px;
             border-radius: 12px;
    }
       QPushButton:hover {
    background-color: rgba(255, 255, 255, 80);
}
    QPushButton:pressed {
    background-color: rgba(220, 220, 220, 220);
}
    """


        self.pushButton_WELCOME_YES = QtWidgets.QPushButton("YES")
        self.pushButton_WELCOME_YES.setStyleSheet(button_style)
        self.pushButton_WELCOME_YES.setMinimumSize(250, 60)
        self.verticalLayout.addWidget(self.pushButton_WELCOME_YES, alignment=QtCore.Qt.AlignHCenter)


        self.pushButton_WELCOME_NO = QtWidgets.QPushButton("NO")
        self.pushButton_WELCOME_NO.setStyleSheet(button_style)
        self.pushButton_WELCOME_NO.setMinimumSize(250, 60)
        self.verticalLayout.addWidget(self.pushButton_WELCOME_NO, alignment=QtCore.Qt.AlignHCenter)


        self.pushButton_QUIT_WELCOME = QtWidgets.QPushButton("QUIT PROGRAM")
        self.pushButton_QUIT_WELCOME.setStyleSheet(button_style)
        self.pushButton_QUIT_WELCOME.setMinimumSize(250, 60)
        self.verticalLayout.addWidget(self.pushButton_QUIT_WELCOME, alignment=QtCore.Qt.AlignHCenter)

        WelcomePage.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(WelcomePage)
        self.menuQuit = QtWidgets.QMenu("Quit", self.menubar)   # ✅ FIXED
        self.menubar.addMenu(self.menuQuit)
        WelcomePage.setMenuBar(self.menubar)


        self.statusbar = QtWidgets.QStatusBar(WelcomePage)
        WelcomePage.setStatusBar(self.statusbar)


        self.connect_buttons()
        self.retranslateUi(WelcomePage)


    def connect_buttons(self):
        self.pushButton_WELCOME_NO.clicked.connect(self.reg)
        self.pushButton_WELCOME_YES.clicked.connect(self.Login)
        self.pushButton_QUIT_WELCOME.clicked.connect(self.Quitprogram)

    def Quitprogram(self):
        exit()

    def Login(self):
        self.LoginWindow = QtWidgets.QMainWindow()
        self.ui = Ui_LoginWindow()
        self.ui.beginLogin(self.LoginWindow)
        self.LoginWindow.showMaximized()
        self.window.close()


    def reg(self):
        self.registrationPage = QtWidgets.QMainWindow()
        self.ui = Ui_registrationPage()
        self.ui.setupUi(self.registrationPage)
        self.registrationPage.showMaximized()
        self.window.close()


    def open_window(self, ui_class):
        window = QtWidgets.QMainWindow()
        ui = ui_class()
        ui.setupUi(window)
        window.showMaximized()
        self.window.close()

    def retranslateUi(self, WelcomePage):
        _translate = QtCore.QCoreApplication.translate
        WelcomePage.setWindowTitle(_translate("WelcomePage", "Welcome to BOI"))
        self.label.setText(_translate("WelcomePage", "Welcome to BOI Bank Limited"))
        self.label_2.setText(_translate("WelcomePage", "Do You Have An Existing Account?"))
        self.pushButton_WELCOME_YES.setText(_translate("WelcomePage", "YES"))
        self.pushButton_WELCOME_NO.setText(_translate("WelcomePage", "NO"))
        self.pushButton_QUIT_WELCOME.setText(_translate("WelcomePage", "QUIT PROGRAM"))
        self.menuQuit.setTitle(_translate("WelcomePage", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WelcomePage = QtWidgets.QMainWindow()
    ui = Ui_Page()
    ui.setupUi(WelcomePage)

    WelcomePage.showMaximized()   # 🔥 FULL SCREEN

    sys.exit(app.exec_())


import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

from MainProfile import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox

#
# from faker import Faker
#
# # Specify the database filename
db_filename = 'BankMT.db'

# Create a connection to the database (this will also create the database file)
conn = sqlite3.connect(db_filename)

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Create a table
create_table_query = '''
CREATE TABLE IF NOT EXISTS MTBANK (

    TYPE TEXT,
    AMOUNT INTEGER,
    SENDER TEXT,
    SENDEROLDBAL INTEGER,
    SENDERNEWBAL INTEGER,
    RECEIVER TEXT,
    RECOLDBAL INTEGER,
    RECNEWBAL INTEGER
);
'''
cursor.execute(create_table_query)

c = conn.cursor()
conn.commit()
class Ui_LoginWindow(object):
    def beginLogin(self, LoginWindow):
        self.login = LoginWindow
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(900, 600)

        LoginWindow.setStyleSheet("""
        QMainWindow {
            background: qlineargradient(
                x1:0, y1:0, x2:1, y2:1,
                stop:0 #2c3e50,
                stop:1 #4ca1af
            );
        }
        """)


        self.centralwidget = QtWidgets.QWidget(LoginWindow)


        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setAlignment(QtCore.Qt.AlignCenter)


        self.card = QtWidgets.QFrame()
        self.card.setFixedWidth(400)
        self.card.setStyleSheet("""
        QFrame {
          background-color: rgba(255, 255, 255, 60);
          border-radius: 20px;
          border: 1px solid rgba(255,255,255,120);
        }
        """)



        card_layout = QtWidgets.QVBoxLayout(self.card)
        card_layout.setSpacing(20)
        card_layout.setContentsMargins(40, 40, 40, 40)


        self.title = QtWidgets.QLabel("LOGIN")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setStyleSheet("""
            font-size: 32px;
            font-weight: bold;
            color: black;
        """)
        card_layout.addWidget(self.title)


        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setPlaceholderText("Enter Username")
        self.lineEdit.setStyleSheet("""
        QLineEdit {
            padding: 12px;
            border-radius: 10px;
            background: rgba(255,255,255,180);
            font-size: 14pt;
        }
        """)
        card_layout.addWidget(self.lineEdit)


        self.lineEdit_2 = QtWidgets.QLineEdit()
        self.lineEdit_2.setPlaceholderText("Enter Password")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setStyleSheet("""
        QLineEdit {
            padding: 12px;
            border-radius: 10px;
            background: rgba(255,255,255,180);
            font-size: 14pt;
        }
        """)
        card_layout.addWidget(self.lineEdit_2)


        button_style = """
        QPushButton {
            background-color: rgba(255,255,255,80);
            color: black;
            font-size: 14pt;
            padding: 12px;
            border-radius: 12px;
        }
        QPushButton:hover {
            background-color: rgba(255,255,255,120);
        }
        QPushButton:pressed {
            background-color: rgba(255,255,255,180);
        }
        """


        self.pushButton_Login = QtWidgets.QPushButton("LOGIN")
        self.pushButton_Login.setStyleSheet(button_style)
        card_layout.addWidget(self.pushButton_Login)


        self.pushButton_Sign_up = QtWidgets.QPushButton("BACK TO SIGN-UP")
        self.pushButton_Sign_up.setStyleSheet(button_style)
        card_layout.addWidget(self.pushButton_Sign_up)

        main_layout.addWidget(self.card)

        LoginWindow.setCentralWidget(self.centralwidget)


        self.pushButton_Login.clicked.connect(self.loginLogin)
        self.pushButton_Sign_up.clicked.connect(self.reg)


    def general_message(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Question)
        msg.exec_()


    def profile(self):

        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.showMaximized()



    def loginLogin(self):
        self.login.close()
        import sqlite3
        dbb = sqlite3.connect('BankNH.db')
        cur = dbb.cursor()
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        cur.execute("SELECT * FROM NEWBANK WHERE USERNAME = ? AND PASSWORD = ?", ([(username), (password)]))
        result = cur.fetchall()

        if result:
            self.profile()
        else:
            self.general_message('User Error', 'User does not Exist')
        

    def reg(self):
        self.login.close()
        from registrationNew import Ui_registrationPage
        self.general_message('Back', 'Will you like to go Back')
        self.registrationPage = QtWidgets.QMainWindow()
        self.ui = Ui_registrationPage()
        self.ui.setupUi(self.registrationPage)
        self.registrationPage.showMaximized()
        
        

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login Page"))
        self.label_2.setText(_translate("LoginWindow", "UserName"))
        self.label_3.setText(_translate("LoginWindow", "PassWord"))
        self.pushButton_Login.setText(_translate("LoginWindow", "LOGIN"))
        self.pushButton_Sign_up.setText(_translate("LoginWindow", "BACK TO SIGN-UP PAGE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.beginLogin(LoginWindow)
    LoginWindow.showMaximized()
    sys.exit(app.exec_())


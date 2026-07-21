# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
import sqlite3
from MainLogin import Ui_LoginWindow
from PyQt5.QtWidgets import QMessageBox

dbb = sqlite3.connect('BankNH.db')
c = dbb.cursor()


class Ui_registrationPage(object):
    def setupUi(self, registrationPage):
        self.register = registrationPage
        registrationPage.setObjectName("registrationPage")
        registrationPage.resize(900, 700)

        # 🎨 Background
        registrationPage.setStyleSheet("""
        QMainWindow {
            background-color: #d6ecff;
        }
        """)

        self.centralwidget = QtWidgets.QWidget(registrationPage)
        self.centralwidget.setObjectName("centralwidget")

        # 📦 Main Layout
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setAlignment(QtCore.Qt.AlignCenter)
        main_layout.setContentsMargins(30, 30, 30, 30)

        # 🧊 Card
        card = QtWidgets.QFrame()
        card.setMaximumWidth(700)
        card.setStyleSheet("""
        QFrame {
            background-color: white;
            border-radius: 20px;
        }
        """)

        card_layout = QtWidgets.QVBoxLayout(card)
        card_layout.setSpacing(20)
        card_layout.setContentsMargins(35, 35, 35, 35)

        # 📝 Title
        self.label_10 = QtWidgets.QLabel("📝 Create Account")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            color: #2c3e50;
        """)
        card_layout.addWidget(self.label_10)

        # 🎨 Input Style
        input_style = """
        QLineEdit {
            padding: 10px;
            border-radius: 10px;
            border: 2px solid #e0e0e0;
            font-size: 12pt;
            background-color: white;
        }
        QLineEdit:focus {
            border: 2px solid #3498db;
        }
        """

        label_style = """
        QLabel {
            font-size: 11pt;
            font-weight: bold;
            color: #2c3e50;
        }
        """

        combo_style = """
        QComboBox {
            padding: 10px;
            border-radius: 10px;
            border: 2px solid #e0e0e0;
            font-size: 12pt;
            background-color: white;
        }
        QComboBox:focus {
            border: 2px solid #3498db;
        }
        """

        button_style = """
        QPushButton {
            background-color: #3498db;
            color: white;
            border-radius: 12px;
            padding: 12px;
            font-size: 13pt;
            font-weight: bold;
        }
        QPushButton:hover {
            background-color: #2980b9;
        }
        """

        # 📋 Form Layout
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeft)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)

        # Username
        self.label_username = QtWidgets.QLabel("Username")
        self.label_username.setStyleSheet(label_style)
        self.lineEdit_Username = QtWidgets.QLineEdit()
        self.lineEdit_Username.setPlaceholderText("Enter username")
        self.lineEdit_Username.setStyleSheet(input_style)
        self.formLayout.addRow(self.label_username, self.lineEdit_Username)

        # First Name
        self.label_fname = QtWidgets.QLabel("First Name")
        self.label_fname.setStyleSheet(label_style)
        self.lineEdit_Firstname = QtWidgets.QLineEdit()
        self.lineEdit_Firstname.setPlaceholderText("Enter first name")
        self.lineEdit_Firstname.setStyleSheet(input_style)
        self.formLayout.addRow(self.label_fname, self.lineEdit_Firstname)


        self.label_Lname = QtWidgets.QLabel("Last Name")
        self.label_Lname.setStyleSheet(label_style)
        self.lineEdit_Lastname = QtWidgets.QLineEdit()
        self.lineEdit_Lastname.setPlaceholderText("Enter last name")
        self.lineEdit_Lastname.setStyleSheet(input_style)
        self.formLayout.addRow(self.label_Lname, self.lineEdit_Lastname)

        self.label_email = QtWidgets.QLabel("Email")
        self.label_email.setStyleSheet(label_style)
        self.lineEdit_email = QtWidgets.QLineEdit()
        self.lineEdit_email.setPlaceholderText("Enter email")
        self.lineEdit_email.setStyleSheet(input_style)
        self.formLayout.addRow(self.label_email, self.lineEdit_email)


        self.label_password = QtWidgets.QLabel("Password")
        self.label_password.setStyleSheet(label_style)
        self.lineEdit_password = QtWidgets.QLineEdit()
        self.lineEdit_password.setPlaceholderText("Enter password")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setStyleSheet(input_style)
        self.formLayout.addRow(self.label_password, self.lineEdit_password)


        self.label_password_confirm = QtWidgets.QLabel("Confirm Password")
        self.label_password_confirm.setStyleSheet(label_style)
        self.lineEdit_confirmPassword = QtWidgets.QLineEdit()
        self.lineEdit_confirmPassword.setPlaceholderText("Confirm password")
        self.lineEdit_confirmPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_confirmPassword.setStyleSheet(input_style)
        self.formLayout.addRow(self.label_password_confirm, self.lineEdit_confirmPassword)


        self.label_phone = QtWidgets.QLabel("Phone")
        self.label_phone.setStyleSheet(label_style)
        self.lineEdit_phone = QtWidgets.QLineEdit()
        self.lineEdit_phone.setPlaceholderText("Enter phone number")
        self.lineEdit_phone.setStyleSheet(input_style)
        self.formLayout.addRow(self.label_phone, self.lineEdit_phone)


        self.label_sex = QtWidgets.QLabel("Gender")
        self.label_sex.setStyleSheet(label_style)
        self.comboBox_sex = QtWidgets.QComboBox()
        self.comboBox_sex.addItems(["Male", "Female", "Other"])
        self.comboBox_sex.setStyleSheet(combo_style)
        self.formLayout.addRow(self.label_sex, self.comboBox_sex)

        # Address
        self.label_address = QtWidgets.QLabel("Address")
        self.label_address.setStyleSheet(label_style)
        self.lineEdit_address = QtWidgets.QLineEdit()
        self.lineEdit_address.setPlaceholderText("Enter address")
        self.lineEdit_address.setStyleSheet(input_style)
        self.formLayout.addRow(self.label_address, self.lineEdit_address)

        # 4-digit PIN (used for authorising large transfers)
        self.label_pin = QtWidgets.QLabel("4-digit PIN")
        self.label_pin.setStyleSheet(label_style)
        self.lineEdit_pin = QtWidgets.QLineEdit()
        self.lineEdit_pin.setPlaceholderText("Set a 4-digit PIN")
        self.lineEdit_pin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pin.setMaxLength(4)
        self.lineEdit_pin.setStyleSheet(input_style)
        self.formLayout.addRow(self.label_pin, self.lineEdit_pin)

        card_layout.addLayout(self.formLayout)

        # Buttons
        self.pushButton_Register = QtWidgets.QPushButton("REGISTER")
        self.pushButton_Register.setStyleSheet(button_style)
        card_layout.addWidget(self.pushButton_Register)

        self.pushButton_reglogin = QtWidgets.QPushButton("LOGIN")
        self.pushButton_reglogin.setStyleSheet(button_style)
        card_layout.addWidget(self.pushButton_reglogin)

        main_layout.addWidget(card)

        registrationPage.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(registrationPage)
        self.statusbar.setObjectName("statusbar")
        registrationPage.setStatusBar(self.statusbar)

        # Connect Buttons
        self.pushButton_Register.clicked.connect(self.CreateDB)
        self.pushButton_reglogin.clicked.connect(self.login)

    def general_message(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def CreateDB(self):
        c.execute(''' CREATE TABLE IF NOT EXISTS NEWBANK(
           ID INTEGER PRIMARY KEY AUTOINCREMENT,
           USERNAME CHAR(20) NOT NULL,
           FIRSTNAME STR NOT NULL,
           LASTNAME STR NOT NULL,
           EMAIL STR NOT NULL,
           PASSWORD STR NOT NULL,
           CONFIRM STR NOT NULL,
           PHONE CHAR(10) NOT NULL,
           SEX STR,
           ADDRESS CHAR(50) NOT NULL,
           BAL REAL(200) DEFAULT 0,
           PIN TEXT
           );
        ''')
        self.insertdb()

    def insertdb(self):
        username = self.lineEdit_Username.text()
        firstname = self.lineEdit_Firstname.text()
        lastname = self.lineEdit_Lastname.text()
        email = self.lineEdit_email.text()
        password = self.lineEdit_password.text()
        confirmPass = self.lineEdit_confirmPassword.text()
        phone = self.lineEdit_phone.text()
        sex = self.comboBox_sex.currentText()
        address = self.lineEdit_address.text()
        pin = self.lineEdit_pin.text()

        if '@' not in email:
            self.general_message('Invalid Email', 'Please check your email again.')
            return

        if password != confirmPass:
            self.general_message('Password Error', 'Passwords do not match.')
            return

        if len(phone) != 10 or not phone.isdigit():
            self.general_message('Invalid Number', 'Please enter a valid 10-digit phone number.')
            return

        if len(pin) != 4 or not pin.isdigit():
            self.general_message('Invalid PIN', 'Please enter a 4-digit numeric PIN.')
            return

        c.execute("""
INSERT INTO NEWBANK(USERNAME, FIRSTNAME, LASTNAME, EMAIL, PASSWORD, CONFIRM, PHONE, SEX, ADDRESS, BAL, PIN)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    str(username),
    str(firstname),
    str(lastname),
    str(email),
    str(password),
    str(confirmPass),
    str(phone),
    str(sex),
    str(address),
    1000.0,
    str(pin)
))


        dbb.commit()
        self.general_message("Success", "Registration successful!")
        self.login()

    def login(self):
        self.register.close()
        self.LoginWindow = QtWidgets.QMainWindow()
        self.ui = Ui_LoginWindow()
        self.ui.beginLogin(self.LoginWindow)
        self.LoginWindow.showMaximized()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registrationPage = QtWidgets.QMainWindow()
    ui = Ui_registrationPage()
    ui.setupUi(registrationPage)
    registrationPage.showMaximized()
    sys.exit(app.exec_())
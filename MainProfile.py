# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QTableWidgetItem
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.mainwindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 750)

        # =========================
        # BACKGROUND
        # =========================
        MainWindow.setStyleSheet("""
        QMainWindow {
            background-color: #d6ecff;
        }
        """)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setAlignment(QtCore.Qt.AlignTop)
        main_layout.setSpacing(30)
        main_layout.setContentsMargins(40, 30, 40, 30)

        # =========================
        # HEADER
        # =========================
        self.label = QtWidgets.QLabel("🏦 BOI Banking Dashboard")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("""
            font-size: 40px;
            font-weight: 800;
            color: #2c3e50;
        """)
        main_layout.addWidget(self.label)

        self.subtitle = QtWidgets.QLabel("Manage your account easily")
        self.subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitle.setStyleSheet("""
            font-size: 18px;
            color: #7f8c8d;
        """)
        main_layout.addWidget(self.subtitle)

        # =========================
        # BIG CARD CONTAINER
        # =========================
        card = QtWidgets.QFrame()
        card.setStyleSheet("""
        QFrame {
            background-color: white;
            border-radius: 25px;
        }
        """)
        card.setMinimumWidth(950)
        card.setMinimumHeight(500)

        card_layout = QtWidgets.QGridLayout(card)
        card_layout.setSpacing(35)
        card_layout.setContentsMargins(50, 50, 50, 50)


        btn_style = """
        QPushButton {
            background-color: #ffffff;
            border-radius: 18px;
            padding: 18px;
            font-size: 16pt;
            font-weight: 600;
            color: #2c3e50;
            border: 2px solid #e0e0e0;
        }
        QPushButton:hover {
            background-color: #3498db;
            color: white;
            border: none;
        }
        """


        self.pushButton_balance = QtWidgets.QPushButton("💰 Check Balance")
        self.pushButton_balance.setStyleSheet(btn_style)

        self.pushButton_transfer = QtWidgets.QPushButton("🔁 Transfer Money")
        self.pushButton_transfer.setStyleSheet(btn_style)

        self.pushButton_history = QtWidgets.QPushButton("📜 Transaction History")
        self.pushButton_history.setStyleSheet(btn_style)

        self.pushButton_deleteAccount = QtWidgets.QPushButton("❌ Delete Account")
        self.pushButton_deleteAccount.setStyleSheet(btn_style)

        self.pushButton_logout = QtWidgets.QPushButton("🚪 Logout")
        self.pushButton_logout.setStyleSheet(btn_style)

        # Bigger same size for all buttons
        for btn in [
            self.pushButton_balance,
            self.pushButton_transfer,
            self.pushButton_history,
            self.pushButton_deleteAccount,
            self.pushButton_logout
        ]:
            btn.setFixedSize(360, 95)


        card_layout.addWidget(self.pushButton_balance, 0, 0)
        card_layout.addWidget(self.pushButton_transfer, 0, 1)
        card_layout.addWidget(self.pushButton_history, 1, 0)
        card_layout.addWidget(self.pushButton_deleteAccount, 1, 1)
        card_layout.addWidget(self.pushButton_logout, 2, 0, 1, 2, alignment=QtCore.Qt.AlignCenter)

        # Center card
        wrapper = QtWidgets.QHBoxLayout()
        wrapper.addStretch()
        wrapper.addWidget(card)
        wrapper.addStretch()

        main_layout.addLayout(wrapper)

        # =========================
        # CONNECT BUTTONS
        # =========================
        self.pushButton_balance.clicked.connect(self.CheckBal)
        self.pushButton_transfer.clicked.connect(self.Transfer)
        self.pushButton_history.clicked.connect(self.TransactionHistory)
        self.pushButton_deleteAccount.clicked.connect(self.DeleteAcc)
        self.pushButton_logout.clicked.connect(self.Logout)

    # =========================
    # LOGOUT
    # =========================
    def Logout(self):
        reply = QMessageBox.question(
            self.mainwindow,
            'Logout',
            'Are you sure you want to logout?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.mainwindow.close()

            from MainLogin import Ui_LoginWindow
            self.loginWindow = QtWidgets.QMainWindow()
            self.ui = Ui_LoginWindow()
            self.ui.beginLogin(self.loginWindow)
            self.loginWindow.showMaximized()

    # =========================
    # DELETE ACCOUNT
    # =========================
    def DeleteAcc(self):
        conn = sqlite3.connect("BankNH.db")
        cur = conn.cursor()

        username, ok1 = QInputDialog.getText(
            self.mainwindow,
            "Delete Account",
            "Please Enter Your Username:"
        )

        if not (ok1 and username):
            conn.close()
            QMessageBox.warning(
                self.mainwindow,
                "Cancelled",
                "Account deletion cancelled."
            )
            return

        password, ok2 = QInputDialog.getText(
            self.mainwindow,
            "Delete Account",
            "Please Enter Your Password:",
            QtWidgets.QLineEdit.Password
        )

        if ok2 and password:
            cur.execute("SELECT * FROM NEWBANK WHERE USERNAME = ? AND PASSWORD = ?",
                        (username, password))
            user_data = cur.fetchone()

            if user_data is not None:
                cur.execute("DELETE FROM NEWBANK WHERE USERNAME = ? AND PASSWORD = ?",
                            (username, password))
                conn.commit()
                conn.close()

                QMessageBox.information(
                    self.mainwindow,
                    "Account Deleted",
                    "Your account has been successfully deleted."
                )
            else:
                conn.close()
                QMessageBox.warning(
                    self.mainwindow,
                    "Deletion Failed",
                    "Incorrect username or password. Account not deleted."
                )
        else:
            conn.close()
            QMessageBox.warning(
                self.mainwindow,
                "Cancelled",
                "Account deletion cancelled."
            )

    # =========================
    # TRANSFER PAGE
    # =========================
    def Transfer(self):
        self.mainwindow.close()
        from Transfer import Ui_TransferWindow
        self.TransferWindow = QtWidgets.QMainWindow()
        self.ui = Ui_TransferWindow()
        self.ui.setupUi(self.TransferWindow)
        self.TransferWindow.showMaximized()

    # =========================
    # CHECK BALANCE
    # =========================
    def CheckBal(self):
        username, okPressed = QInputDialog.getText(
            self.mainwindow,
            "Check Balance",
            "Please Enter Your Username:"
        )

        if okPressed and username:
            conn = sqlite3.connect('BankNH.db')
            cur = conn.cursor()

            cur.execute("SELECT BAL FROM NEWBANK WHERE USERNAME = ?", (username,))
            data = cur.fetchone()
            conn.close()

            if data is not None:
                balance = data[0]
                if balance is None:
                    balance = 0.0

                QMessageBox.information(
                    self.mainwindow,
                    "Balance",
                    f"Your balance is: ₹{balance}"
                )
            else:
                QMessageBox.warning(
                    self.mainwindow,
                    "User Not Found",
                    "No account found with that username."
                )
        else:
            QMessageBox.warning(
                self.mainwindow,
                "Invalid Input",
                "Please enter your username."
            )

    # =========================
    # TRANSACTION HISTORY
    # =========================
    def TransactionHistory(self):
        self.historyWindow = QtWidgets.QDialog(self.mainwindow)
        self.historyWindow.setWindowTitle("Transaction History")
        self.historyWindow.resize(1000, 550)
        self.historyWindow.setStyleSheet("""
            QDialog {
                background-color: #f4faff;
            }
            QTableWidget {
                background-color: white;
                border-radius: 10px;
                gridline-color: #dcdcdc;
                font-size: 11pt;
            }
            QHeaderView::section {
                background-color: #3498db;
                color: white;
                padding: 8px;
                font-size: 11pt;
                border: none;
            }
        """)

        layout = QtWidgets.QVBoxLayout(self.historyWindow)

        title = QtWidgets.QLabel("📜 Transaction History")
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #2c3e50;
            margin: 10px;
        """)
        layout.addWidget(title)

        table = QtWidgets.QTableWidget()
        layout.addWidget(table)

        conn = sqlite3.connect("BankNH.db")
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS NEWT (
                SENDER TEXT,
                RECEIVER TEXT,
                TTYPE TEXT,
                AMOUNT REAL,
                SENDEROLDBAL REAL,
                SENDERNEWBAL REAL,
                RECOLDBAL REAL,
                RECNEWBAL REAL
            )
        """)

        cur.execute("SELECT * FROM NEWT")
        rows = cur.fetchall()
        conn.close()

        headers = [
            "Sender",
            "Receiver",
            "Type",
            "Amount",
            "Sender Old Bal",
            "Sender New Bal",
            "Receiver Old Bal",
            "Receiver New Bal"
        ]

        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)
        table.setRowCount(len(rows))

        for row_num, row_data in enumerate(rows):
            for col_num, data in enumerate(row_data):
                table.setItem(row_num, col_num, QTableWidgetItem(str(data)))

        table.resizeColumnsToContents()
        table.horizontalHeader().setStretchLastSection(True)

        self.historyWindow.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
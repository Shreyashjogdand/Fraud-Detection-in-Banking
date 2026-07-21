import sys
import sqlite3
import random
import joblib
import pandas as pd

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

from twilio.rest import Client
from MainProfile import Ui_MainWindow
from config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_PHONE_NUMBER,
    USER_PHONE_NUMBER
)


class Ui_TransferWindow(object):
    def setupUi(self, TransferWindow):
        self.transfer = TransferWindow
        TransferWindow.setObjectName("TransferWindow")
        TransferWindow.resize(900, 650)

        # 🌈 Main Background
        TransferWindow.setStyleSheet("""
        QMainWindow {
            background-color: #d6ecff;
        }
        """)

        self.centralwidget = QtWidgets.QWidget(TransferWindow)
        TransferWindow.setCentralWidget(self.centralwidget)

        # =========================
        # MAIN LAYOUT
        # =========================
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setAlignment(QtCore.Qt.AlignCenter)
        main_layout.setContentsMargins(40, 30, 40, 30)
        main_layout.setSpacing(20)

        # =========================
        # TITLE
        # =========================
        self.titleLabel = QtWidgets.QLabel("💸 Transfer Money")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setStyleSheet("""
            font-size: 34px;
            font-weight: bold;
            color: #2c3e50;
        """)
        main_layout.addWidget(self.titleLabel)

        self.subtitleLabel = QtWidgets.QLabel("Send money securely and quickly")
        self.subtitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitleLabel.setStyleSheet("""
            font-size: 15px;
            color: #5d6d7e;
        """)
        main_layout.addWidget(self.subtitleLabel)

        # =========================
        # CARD
        # =========================
        card = QtWidgets.QFrame()
        card.setMaximumWidth(750)
        card.setStyleSheet("""
        QFrame {
            background-color: white;
            border-radius: 20px;
        }
        """)
        main_layout.addWidget(card, alignment=QtCore.Qt.AlignCenter)

        card_layout = QtWidgets.QVBoxLayout(card)
        card_layout.setContentsMargins(35, 35, 35, 35)
        card_layout.setSpacing(20)

        # =========================
        # STYLES
        # =========================
        label_style = """
        QLabel {
            font-size: 12pt;
            font-weight: 600;
            color: #2c3e50;
        }
        """

        input_style = """
        QLineEdit {
            padding: 12px;
            border-radius: 10px;
            border: 2px solid #dcdcdc;
            font-size: 12pt;
            background-color: #fdfdfd;
        }
        QLineEdit:focus {
            border: 2px solid #3498db;
        }
        """

        combo_style = """
        QComboBox {
            padding: 12px;
            border-radius: 10px;
            border: 2px solid #dcdcdc;
            font-size: 12pt;
            background-color: #fdfdfd;
            color: #2c3e50;
        }
        QComboBox:focus {
            border: 2px solid #3498db;
        }
        """

        btn_style = """
        QPushButton {
            background-color: white;
            border-radius: 12px;
            padding: 14px;
            font-size: 13pt;
            font-weight: bold;
            color: #2c3e50;
            border: 2px solid #dcdcdc;
        }
        QPushButton:hover {
            background-color: #3498db;
            color: white;
            border: none;
        }
        """


        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeft)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(18)

        # Amount
        self.label_amount2txf = QtWidgets.QLabel("Enter Amount")
        self.label_amount2txf.setStyleSheet(label_style)
        self.lineEdit_amount2txf = QtWidgets.QLineEdit()
        self.lineEdit_amount2txf.setPlaceholderText("Enter amount")
        self.lineEdit_amount2txf.setStyleSheet(input_style)
        self.formLayout.addRow(self.label_amount2txf, self.lineEdit_amount2txf)


        self.label_name2txf = QtWidgets.QLabel("Sender Username")
        self.label_name2txf.setStyleSheet(label_style)
        self.lineEdit_name2txf = QtWidgets.QLineEdit()
        self.lineEdit_name2txf.setPlaceholderText("Enter sender username")
        self.lineEdit_name2txf.setStyleSheet(input_style)
        self.formLayout.addRow(self.label_name2txf, self.lineEdit_name2txf)


        self.label_number2txf = QtWidgets.QLabel("Receiver Username")
        self.label_number2txf.setStyleSheet(label_style)
        self.lineEdit_number2txf = QtWidgets.QLineEdit()
        self.lineEdit_number2txf.setPlaceholderText("Enter receiver username")
        self.lineEdit_number2txf.setStyleSheet(input_style)
        self.formLayout.addRow(self.label_number2txf, self.lineEdit_number2txf)

        # Transaction Type
        self.label_type = QtWidgets.QLabel("Transaction Type")
        self.label_type.setStyleSheet(label_style)
        self.comboBox_accountType = QtWidgets.QComboBox()
        self.comboBox_accountType.addItems(["Type", "CASH_OUT", "TRANSFER"])
        self.comboBox_accountType.setStyleSheet(combo_style)
        self.formLayout.addRow(self.label_type, self.comboBox_accountType)

        # Bank Name
        self.label_bank = QtWidgets.QLabel("Bank Name")
        self.label_bank.setStyleSheet(label_style)
        self.comboBox_bankType = QtWidgets.QComboBox()
        self.comboBox_bankType.addItems([
            "Choose Bank Name",
            "SBI",
            "HDFC",
            "KOTAK",
            "AXIS",
            "PDCC",
            "BOM",
            "Others"
        ])
        self.comboBox_bankType.setStyleSheet(combo_style)
        self.formLayout.addRow(self.label_bank, self.comboBox_bankType)

        card_layout.addLayout(self.formLayout)

        # =========================
        # BUTTONS
        # =========================
        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.setSpacing(20)

        self.pushButton_transferTransfer = QtWidgets.QPushButton("💸 TRANSFER")
        self.pushButton_transferTransfer.setStyleSheet(btn_style)
        self.pushButton_transferTransfer.setFixedHeight(55)

        self.pushButton_transferCancle = QtWidgets.QPushButton("↩ CANCEL")
        self.pushButton_transferCancle.setStyleSheet(btn_style)
        self.pushButton_transferCancle.setFixedHeight(55)

        btn_layout.addWidget(self.pushButton_transferTransfer)
        btn_layout.addWidget(self.pushButton_transferCancle)

        card_layout.addLayout(btn_layout)

        # CONNECT BUTTONS
        self.pushButton_transferTransfer.clicked.connect(self.SendTransfer)
        self.pushButton_transferCancle.clicked.connect(self.CancleTxf)


    def message(self, title, message):
        mssg = QMessageBox()
        mssg.setWindowTitle(title)
        mssg.setIcon(QMessageBox.Warning)
        mssg.setStandardButtons(QMessageBox.Ok)
        mssg.setText(message)
        mssg.exec_()

    def send_sms(self, text_message):
        try:
            from twilio.rest import Client
            from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, USER_PHONE_NUMBER

            client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

            message = client.messages.create(
                body=text_message,
                from_=TWILIO_PHONE_NUMBER,
                to=USER_PHONE_NUMBER
            )

            print("SMS sent successfully:", message.sid)

        except Exception as e:
            print("SMS sending failed:", e)


    def SendTransfer(self):
        conn = sqlite3.connect("BankNH.db")
        cur = conn.cursor()

        create_new_table_sql = """
        CREATE TABLE IF NOT EXISTS NEWT (
            SENDER TEXT,
            RECEIVER TEXT,
            TTYPE TEXT,
            AMOUNT REAL,
            SENDEROLDBAL REAL,
            SENDERNEWBAL REAL,
            RECOLDBAL REAL,
            RECNEWBAL REAL
        );
        """
        cur.execute(create_new_table_sql)

        sender_username = self.lineEdit_name2txf.text().strip()
        amount_str = self.lineEdit_amount2txf.text().strip()
        receiver_username = self.lineEdit_number2txf.text().strip()
        selected_type = self.comboBox_accountType.currentText()


        if not sender_username or not receiver_username or not amount_str:
            self.message("Missing Fields", "Please fill all required fields.")
            conn.close()
            return

        if selected_type == "Type":
            self.message("Invalid Type", "Please select a valid transaction type.")
            conn.close()
            return

        if sender_username == receiver_username:
            self.message("Invalid Transfer", "Sender and Receiver cannot be the same.")
            conn.close()
            return

        try:

            cur.execute("SELECT USERNAME, BAL FROM NEWBANK WHERE USERNAME = ?", (sender_username,))
            sender_data = cur.fetchone()

            if sender_data is None:
                self.message("Sender Not Found", "Sender username not found.")
                conn.close()
                return

            sender_balance = sender_data[1]

            if sender_balance is None:
                sender_balance = 0.0


            try:
                amount = float(amount_str)
                if amount <= 0:
                    raise ValueError
            except ValueError:
                self.message("Invalid Amount", "Please enter a valid positive amount.")
                conn.close()
                return

            if sender_balance < amount:
                self.message("Insufficient Balance", "You have insufficient balance for this transfer.")
                conn.close()
                return


            PIN_THRESHOLD = 10000
            if amount > PIN_THRESHOLD:
                from PyQt5.QtWidgets import QInputDialog
                cur.execute("SELECT PIN FROM NEWBANK WHERE USERNAME = ?", (sender_username,))
                pin_row = cur.fetchone()
                real_pin = pin_row[0] if pin_row else None

                entered_pin, ok = QInputDialog.getText(
                    self.transfer,
                    "Security Check",
                    "Large transfer detected.\nPlease enter your 4-digit PIN:",
                    QtWidgets.QLineEdit.Password
                )

                if not ok or not entered_pin:
                    self.send_sms(
                        f"\u26a0 FRAUD ALERT!\n"
                        f"Suspicious transaction blocked.\n"
                        f"No PIN entered for a large transfer.\n"
                        f"From: {sender_username}\n"
                        f"Amount: \u20b9{amount_str}"
                    )
                    self.message("\u26a0 Unauthorized / Fraud",
                                 "No PIN entered for a large transfer. Transaction blocked.")
                    conn.close()
                    return

                if entered_pin != real_pin:
                    self.send_sms(
                        f"\u26a0 FRAUD ALERT!\n"
                        f"Suspicious transaction blocked.\n"
                        f"Incorrect PIN entered for a large transfer.\n"
                        f"From: {sender_username}\n"
                        f"Amount: \u20b9{amount_str}"
                    )
                    self.message("\u26a0 Unauthorized / Fraud",
                                 "Incorrect PIN. Transaction blocked as suspicious.")
                    conn.close()
                    return


            cur.execute("SELECT USERNAME, BAL FROM NEWBANK WHERE USERNAME = ?", (receiver_username,))
            receiver_data = cur.fetchone()

            if receiver_data is None:
                self.message("Receiver Not Found", "Receiver username not found.")
                conn.close()
                return

            receiver_balance = receiver_data[1]

            if receiver_balance is None:
                receiver_balance = 0.0


            sender_old_balance = sender_balance
            sender_new_balance = sender_balance - amount

            receiver_old_balance = receiver_balance
            receiver_new_balance = receiver_balance + amount


            cur.execute("UPDATE NEWBANK SET BAL = ? WHERE USERNAME = ?",
                        (sender_new_balance, sender_username))

            cur.execute("UPDATE NEWBANK SET BAL = ? WHERE USERNAME = ?",
                        (receiver_new_balance, receiver_username))

            conn.commit()


            cur.execute("""
                INSERT INTO NEWT (SENDER, RECEIVER, TTYPE, AMOUNT, SENDEROLDBAL, SENDERNEWBAL, RECOLDBAL, RECNEWBAL)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                sender_username,
                receiver_username,
                selected_type,
                amount,
                sender_old_balance,
                sender_new_balance,
                receiver_old_balance,
                receiver_new_balance
            ))

            conn.commit()


            fraud_input = [
                random.randint(0, 9),
                selected_type,
                amount,
                sender_old_balance,
                sender_new_balance,
                receiver_old_balance,
                receiver_new_balance
            ]

            self.load(
                fraud_input,
                sender_username,
                receiver_username,
                amount,
                sender_new_balance
            )


            self.lineEdit_name2txf.clear()
            self.lineEdit_number2txf.clear()
            self.lineEdit_amount2txf.clear()
            self.comboBox_accountType.setCurrentIndex(0)
            self.comboBox_bankType.setCurrentIndex(0)

        except sqlite3.Error as e:
            self.message("Database Error", str(e))

        finally:
            conn.close()


    def CancleTxf(self):
        self.transfer.close()
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.showMaximized()


    def load(self, fraud_list, sender_username, receiver_username, amount, sender_new_balance):
        df = pd.DataFrame([fraud_list])
        df.rename(columns={
            0: 'count',
            1: 'type',
            2: 'amount',
            3: 'oldbalanceOrig',
            4: 'newbalanceOrig',
            5: 'oldbalanceDest',
            6: 'newbalanceDest'
        }, inplace=True)

        try:
            loaded_model = joblib.load("banking_app_rf.pkl")

        # Direct prediction
            prediction = loaded_model.predict(df)

            if prediction[0] == 1:
                message = "⚠ Fraud Transaction Detected!"

            # Fraud SMS
                self.send_sms(
                    f"⚠ FRAUD ALERT!\n"
                    f"Suspicious transaction detected.\n"
                    f"From: {sender_username}\n"
                    f"To: {receiver_username}\n"
                    f"Amount: ₹{amount}\n"
                    f"Available Balance: ₹{sender_new_balance}"
                )

            else:
                message = "✅ Transaction Successful!"

            # Success SMS
                self.send_sms(
                    f"✅ Money Transfer Successful!\n"
                    f"From: {sender_username}\n"
                    f"To: {receiver_username}\n"
                    f"Amount: ₹{amount}\n"
                    f"Available Balance: ₹{sender_new_balance}"
                )

        except Exception as e:
            message = f"Transaction completed, but fraud model error:\n{str(e)}"

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Transaction Result")
        msg.exec_()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    TransferWindow = QtWidgets.QMainWindow()
    ui = Ui_TransferWindow()
    ui.setupUi(TransferWindow)
    TransferWindow.showMaximized()
    sys.exit(app.exec_())
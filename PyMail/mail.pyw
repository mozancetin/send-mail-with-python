import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLineEdit , QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5 import QtGui


class Window(QWidget):

    def __init__(self):

        super().__init__()
        self.emailmime()
        self.init_ui()

    def emailmime(self):
        
        self.msg = MIMEMultipart()
        
    def init_ui(self):
        
        self.email = QLineEdit()
        self.emailstr = QLabel("Email:")
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.passwordstr = QLabel("Password:")
        self.to = QLineEdit()
        self.tostr = QLabel("To:")
        self.subject = QLineEdit()
        self.subjectstr = QLabel("Subject:")
        self.finish = QLabel("")

        
        self.string = QLabel("\nMessage:")
        self.msg2 = QTextEdit()
        self.msg2.resize(400,100)
        self.send = QPushButton("Send")

        #----------------------------
        h_box = QHBoxLayout()
        h_box.addWidget(self.emailstr)
        #-----------------------------
        h_box2 = QHBoxLayout()
        h_box2.addWidget(self.passwordstr)
        #-----------------------------
        h_box3 = QHBoxLayout()
        h_box3.addWidget(self.tostr)
        #-----------------------------
        h_box4 = QHBoxLayout()
        h_box4.addWidget(self.subjectstr)
        #-----------------------------
        h2_box = QHBoxLayout()
        h2_box.addWidget(self.email)
        #-----------------------------
        h2_box2 = QHBoxLayout()
        h2_box2.addWidget(self.password)
        #-----------------------------
        h2_box3 = QHBoxLayout()
        h2_box3.addWidget(self.to)
        #-----------------------------
        h2_box4 = QHBoxLayout()
        h2_box4.addWidget(self.subject)
        #-----------------------------

        v_box = QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addLayout(h_box4)

        v_box2 = QVBoxLayout()
        v_box2.addLayout(h2_box)
        v_box2.addLayout(h2_box2)
        v_box2.addLayout(h2_box3)
        v_box2.addLayout(h2_box4)

        h3_box = QHBoxLayout()
        h3_box.addLayout(v_box)
        h3_box.addLayout(v_box2)
        
        #-----------------------------

        v_box3 = QVBoxLayout()
        v_box3.addWidget(self.string)
        v_box3.addStretch()
        v_box3.addWidget(self.msg2)
        v_box3.addStretch()
        v_box3.addWidget(self.finish)
        v_box3.addStretch()
        v_box3.addWidget(self.send)

        h4_box = QHBoxLayout()
        h4_box.addLayout(v_box3)

        v2_box = QVBoxLayout()
        v2_box.addLayout(h3_box)
        v2_box.addStretch()
        v2_box.addLayout(h4_box)
        
        #-----------------------------
        
        self.setLayout(v2_box)
        self.setWindowTitle("Mail")
        self.setWindowIcon(QtGui.QIcon("mail.jpg"))
        self.setMinimumHeight(380)
        self.setMaximumHeight(380)
        self.setMinimumWidth(500)
        self.setMaximumWidth(500)
        self.send.clicked.connect(self.click)
        self.show()

        
    def click(self):
        self.msg["From"] = self.email.text()
        self.msg["To"] = self.to.text()
        self.msg["Subject"] = self.subject.text()

        text = self.msg2.toPlainText()
        msg_body = MIMEText(text, "plain")
        self.msg.attach(msg_body)
        
        try:
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login(self.email.text(),self.password.text())
            mail.sendmail(self.msg["From"], self.msg["To"], self.msg.as_string())
            
            mail.close()
            self.finish.setText("Mail has been sent successfully.")
        except:

            self.finish.setText("There is a problem!\nCheck your internet connection and email information.")


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())

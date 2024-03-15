#This Script defines a PyQt5 based GUI applicatio for user info login.
#it includes a loginWindow class that process users to input their mobile  and passWord
#add upon submission, it verifies the credential against firestore database
#if the credential are valid, it desplays the user profile form from the 'home' module.

#import neccesary libraries
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGraphicsDropShadowEffect, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPixmap
# from Home.home import UserProfileForm # importing user profile form from Home module.
from google.cloud import firestore
import json
from dbConfig import db

#LoginWindow class defination
class LoginWindow(QWidget):
    def __init(self):
        super().__init__()
        self.layout=QVBoxLayout()

        #Creating outer window for login interface.
        self.outerWidgetLogin=QWidget()
        self.outerWidgetLogin.setStyleSheet("background:#f9f9fc; max-height:600px, max-width:400px; border-radius:15px; margin-left:160px")
        
        #loading logo image
        pixmap=QPixmap("./assets/image/windowlogo.png")

        #Displaying logo image
        self.image_label=QLabel(self)
        self.image_label.setPixmap(pixmap)
        self.image_label.setGeometry(0,0,10,10)
        self.image_label.setAlignment(Qt.AlignHCenter)
        self.image_label.setStyleSheet("margin-bottom:20px; margin-top:10px")

        #Adding Shadow effect to the login interface
        shadow=QGraphicsDropShadowEffect(self.outerWidgetLogin)
        shadow.setColor(QColor(63,63,63,180)) #set the shadow color and opacity.
        shadow.setBlurRadius(20) #set blur radius
        shadow.setXOffset(5) #set horizontal offset
        shadow.setYOffset(5) # set vertical offset
        self.outerWidgetLogin.setGraphicsEffect(shadow)

        #layout ffor out widget
        outer_layout=QVBoxLayout(self.outerWidgetLogin)

        #creating UI element
        self.heading=QLabel("Core2Web")
        self.heading.setAlignment(Qt.AlignTop | Qt.AlignGCenter)
        self.heading.setStyleSheet("font-size:25px; font_weight:500; margin-top:20px, heigt:60pxl font-family:Poppins")
        
        self.pageHeading=QLabel("Login")
        self.pageHeading.setAlignment(Qt.AlignCenter)
        self.pageHeading.setStyleSheet("width:350px; font-size:30px; color:qlinerargradient(x1:0, y1:0, y2:0, stop:0 #013565, stop:1#857be7);")
        
        self.userEmailLabel=QLineEdit()
        self.userEmailLabel.setPlaceholderText("Enter mobile no")
        self.userEmailLabel.setStyleSheet("border:1px solid $918a8ae8; max-width:300px; padding-left:20px; font-size:15; margin-top:40px")

        self.userPassLabel=QLineEdit()
        self.userPassLabel.setPlaceholderText("Enter password")
        self.userPassLabel.setEchoMode(QLineEdit.Password)
        self.userPassLabel.setStyleSheet('border:1px; solid #918a8ae8; max-width: 300px, padding-left20px; font-size:15px; margin-top:40')

        self.submitBtn=QPushButton("Submit")
        self.submitBtn.clicked.connect(self.submit)
        self.submitBtn.setStyleSheet("background:qlineargradient(x1:0, y1:0, x2:1, y2:0, stops:0 #o13565, stop:1 #057be7); widthL350px; font-size:20px; color:#ffffff; margin-top:50px")
        self.submitBtn.enterEvent=self.on_enter_btn
        self.submitBtn.leaveEvent=self.on_leave_btn
        
        self.inputFaildHolder =QVBoxLayout()
        self.inputFaildHolder.addWidget(self.userEmailLabel)
        self.inputFaildHolder.addWidget(self.userPassLabel)
        self.inputFaildHolder.addWidget(self.submitBtn)

        #adding UI elements to outer layout 
        outer_layout.addWidget(self.image_label)
        outer_layout.addWidget(self.pageHeading)
        outer_layout.addLayout(self.inputFaildHolder)
        self.formLayout=QVBoxLayout()
        outer_layout.addLayout(self.formLayout)
        outer_layout.setAlignment(Qt.AlignmentHCenter)
        outer_layout.addStretch(1)

        #setting main layout
        self.layout.addWidget(self.outerWidgetLogin)
        self.setStyleSheet("backgroundLqlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #012565, stop:1 #o57be7); min-height:40px")

    #Event handlers for UI elements
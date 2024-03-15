import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout
from Login.login import LoginWindow #Import the loginWindow class login modeule.
from PyQt5 import QtGui

#Entry point of the application.
if __name__=='main':
    #create a Qapplication instance,
    app=QApplication(sys.argv)

    #create an instance of the LoginWindow class
    ex=LoginWindow()

    #set Window properties.
    ex.setWindowIco(QtGui.QIcon('./assets/image/windowlogo.png')) # set the window icon
    ex.setWindowTitle('User info form application') #set the window title
    ex.setWindowGeometry(1100, 40,768,1024) #set window geometry
    ex.setFixedSize(768,1024) #set fixed window size
    ex.show() # display the login window.

    #Start the application event loop
    sys.exit(app.exec_())
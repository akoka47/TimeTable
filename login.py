import os, sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QDateTime, Qt, QTimer
from accountHandle import userTools





class WindowMain(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(WindowMain, self).__init__(parent)
        self.setWindowTitle("Gestion Emploi De Temp - Université Ghardaia")
        self.InitwelcomeScreen()
		
		

    def InitwelcomeScreen(self):
        mainWidgetlayout = QtWidgets.QVBoxLayout(self)
		
		
		
        welcomeScreen = QtWidgets.QLabel(self)
        photo = QtGui.QPixmap('logo.jpg')
		
        welcomeScreen.setPixmap(photo)
        self.setFixedSize(WIDTH, HEIGHT)
		
        

        self.buttonLogin = QtWidgets.QPushButton('Se Connecter', self)
        self.buttonLogin.move(100, 400)
        self.buttonLogin.clicked.connect(self.getLoginWindow)
        self.buttonCreateAcc = QtWidgets.QPushButton('Créer Un Compte', self)
        self.buttonCreateAcc.move(200, 400)
        self.buttonCreateAcc.clicked.connect(self.getCreateAccountWindow)

        mainWidgetlayout.addWidget(welcomeScreen)

    def getCreateAccountWindow(self):
        self.obj = windowCreateAccount()

    def getLoginWindow(self):
        self.obj = windowLogin()


class windowCreateAccount(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(windowCreateAccount, self).__init__(parent)
        self.setWindowTitle("Créer Un Compte")

        # Accessed by multiple functions
        self.nameID = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        # Hides password field
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.comboBox = QtWidgets.QComboBox()

        self.InitCreateAccount()

    def InitCreateAccount(self):
        organization = ["Admin", "ch.Faculté", "ch.Departement", "Prof"]

        mainWidgetlayout = QtWidgets.QGridLayout()
        mainWidgetlayout.addWidget(QtWidgets.QLabel("ID: "), 1, 0)
        mainWidgetlayout.addWidget(self.nameID, 1, 1)
        mainWidgetlayout.addWidget(QtWidgets.QLabel("Password: "), 2, 0)
        mainWidgetlayout.addWidget(self.password, 2, 1)
        mainWidgetlayout.addWidget(QtWidgets.QLabel("Organization: "), 3, 0)

        self.comboBox.addItems(organization)
        mainWidgetlayout.addWidget(self.comboBox, 3, 1)

        buttonSubmit = QtWidgets.QPushButton('Entre', self)
        buttonSubmit.clicked.connect(self.submitHandler)
        buttonCancel = QtWidgets.QPushButton('Annuler', self)
        buttonCancel.clicked.connect(self.close)
        mainWidgetlayout.addWidget(buttonCancel, 4, 0)
        mainWidgetlayout.addWidget(buttonSubmit, 4, 1)

        self.setLayout(mainWidgetlayout)
        self.show()

    def submitHandler(self):
        dataPacket = (self.nameID.text(), self.password.text(),
                      str(self.comboBox.currentText()))

        handle = userTools()
        # returns flag if user already exist
        newUser = handle.pushNewUser(dataPacket)
        if newUser == 0:
            QtWidgets.QMessageBox.warning(
                self, "Attention", "Cet utilisateur existe déjà.")
        else:
            QtWidgets.QMessageBox.warning(
                self, "Succès", "Un nouvel utilisateur a été créé")
            self.close()


class windowLogin(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(windowLogin, self).__init__(parent)
        self.setWindowTitle("Se connecter")
        # Accessed by multiple functions
        self.nameID = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.InitLogin()

    def InitLogin(self):
        mainWidgetlayout = QtWidgets.QGridLayout()
        mainWidgetlayout.addWidget(QtWidgets.QLabel("ID: "), 1, 0)
        mainWidgetlayout.addWidget(self.nameID, 1, 1)
        mainWidgetlayout.addWidget(QtWidgets.QLabel("Mot de passe: "), 2, 0)
        mainWidgetlayout.addWidget(self.password, 2, 1)
        buttonSubmit = QtWidgets.QPushButton('Entre', self)
        buttonSubmit.clicked.connect(self.submitHandler)
        buttonCancel = QtWidgets.QPushButton('Annuler', self)
        buttonCancel.clicked.connect(self.close)
        mainWidgetlayout.addWidget(buttonCancel, 4, 0)
        mainWidgetlayout.addWidget(buttonSubmit, 4, 1)
        self.setLayout(mainWidgetlayout)
        self.show()

    def submitHandler(self):
        dataPacket = (self.nameID.text(), self.password.text())
        handle = userTools()
        loginStatus = handle.loginUser(dataPacket)

        if loginStatus != 1:
            QtWidgets.QMessageBox.warning(
                self, "Attention "," Nom d'utilisateur ou mot de passe incorrect")
        else:
            self.close()
            # Go to another main window
            self.obj = windowFinal()


class windowFinal():
	def __init__(self):
	    os.system('python file_akoka.py')
		


		
       


if __name__ == '__main__':
    import sys
    HEIGHT = 500
    WIDTH = 500
    # GTK 3 will force a warning:
    # (QApplication: invalid style override passed, ignoring it.)
    QtWidgets.QApplication.setDesktopSettingsAware(False)
    # This flag does not fix the issue under Pantheon (eOS)
    app = QtWidgets.QApplication(sys.argv)
    main1 = WindowMain()
    main1.show()
    sys.exit(app.exec_())

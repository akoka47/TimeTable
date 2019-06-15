import PyQt5
from components import Database as db
from containers import Main
import sys




# Entry point for application
if __name__ == '__main__':
	if not db.checkSetup():
		db.setup()
	app = PyQt5.QtWidgets.QApplication(sys.argv)
	parent = PyQt5.QtWidgets.QMainWindow()
	Main.MainWindow(parent)
	parent.show()
	sys.exit(app.exec_())

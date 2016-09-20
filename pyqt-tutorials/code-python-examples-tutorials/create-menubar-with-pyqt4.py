# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Thoi gian: 20-09-2016
# Noi dung: Tao nut nhan voi PyQt4
# Tham khao:
#	1. https://pythonprogramming.net/menubar-pyqt-tutorial/
#	2. http://zetcode.com/gui/pyqt4/firstprograms/

import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
	def __init__(self):			# Cu phap khi su dung class trong Python
		super(Window, self).__init__()
		self.InitWindow()
		self.CreateButton_Quit()
		self.CreateMenubar()

	def InitWindow(self):			# Tao ra mot cua so don 
		self.setGeometry(50, 50, 500, 300)		# Xac dinh vi tri va kich thuoc cua so
		self.setWindowTitle("PyQT Tuts!")		# Dat tieu de cho cua so
		self.setWindowIcon(QtGui.QIcon('python.jpg'))	# Dat Icon cho cua so giao dien
	
	def CreateButton_Quit(self):		# Tao nut nhan chuc nang
		btn = QtGui.QPushButton("Quit!", self)
		btn.clicked.connect(QtCore.QCoreApplication.instance().quit)	# Thuc hien chuc nang Exit
		btn.setGeometry(150, 100, 150, 50)              		# Xac dinh vi tri va kich thuoc cua nut nhan
		self.show()							# Hien thi cua so vua tao len man hinh

	def CreateMenubar(self):		# Tao menubar thuc hien chuc nang
		extractAction = QtGui.QAction("&Exit", self)			# Menu con Edit trong Menu chinh
		extractAction.setShortcut("Ctrl+Q")				# Phim tat cho Menu con
		extractAction.setStatusTip('Leave The App')			# Bao trang thai khi chon Menu
		extractAction.triggered.connect(self.close_application)		# Thuc hien chuc nang trong ham close_application

		self.statusBar()
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')				# Tao menu chinh ten la File
		fileMenu.addAction(extractAction)				# Menu chinh gom menu con dinh nghia o extractAction
		

	def close_application(self):
		sys.exit()


def CreatGUI():					# Tao ung dung giao dien
	app = QtGui.QApplication(sys.argv)
	GUI = Window()						
	sys.exit(app.exec_())

if __name__ == '__main__':
	CreatGUI()

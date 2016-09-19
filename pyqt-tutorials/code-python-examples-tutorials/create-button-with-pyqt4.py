# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Thoi gian: 19-09-2016
# Noi dung: Tao nut nhan voi PyQt4
# Tham khao:
#	1. https://pythonprogramming.net/buttons-pyqt-tutorial/
#	2. https://pythonprogramming.net/button-functions-pyqt-tutorial/	
#	3. http://zetcode.com/gui/pyqt4/firstprograms/

import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
	def __init__(self):			# Cu phap khi su dung class trong Python
		super(Window, self).__init__()
		self.InitWindow()
		self.CreateButton_Hello()
		self.CreateButton_Quit()

	def InitWindow(self):			# Tao ra mot cua so don 
		self.setGeometry(50, 50, 500, 300)		# Xac dinh vi tri va kich thuoc cua so
		self.setWindowTitle("PyQT Tuts!")		# Dat tieu de cho cua so
		self.setWindowIcon(QtGui.QIcon('python.jpg'))	# Dat Icon cho cua so giao dien
	
	def CreateButton_Hello(self):		# Tao nut nhan chuc nang
		# Dinh nghia nut nhan thu nhat
		btn = QtGui.QPushButton("Button Hello!", self)	# Ten cua nut nhan
		btn.clicked.connect(self.ButtonFunction_Hello)	# Nut nhan thuc hien cac lenh trong ham ButtonFunction_Hello
		btn.setGeometry(100, 100, 150, 50)              # Xac dinh vi tri va kich thuoc cua nut nhan
	
	def CreateButton_Quit(self):		# Tao nut nhan chuc nang
		# Dinh nghia nut nhan thu hai
		btn = QtGui.QPushButton("Quit!", self)
		btn.clicked.connect(QtCore.QCoreApplication.instance().quit)	# Thuc hien chuc nang Exit
		btn.setGeometry(300, 100, 150, 50)              		# Xac dinh vi tri va kich thuoc cua nut nhan
		self.show()							# Hien thi cua so vua tao len man hinh

	def ButtonFunction_Hello(self):
		print 'Hello PyQt4!'

def CreatGUI():					# Tao ung dung giao dien
	app = QtGui.QApplication(sys.argv)
	GUI = Window()						
	sys.exit(app.exec_())

if __name__ == '__main__':
	CreatGUI()

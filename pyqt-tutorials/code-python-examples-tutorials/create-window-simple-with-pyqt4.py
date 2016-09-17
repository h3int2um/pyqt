# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Thoi gian: 18-09-2016
# Noi dung: Tao cua so don gian voi PyQt4
# Tham khao:
#	1. http://zetcode.com/gui/pyqt4/firstprograms/
#	2. https://pythonprogramming.net/application-structure-pyqt-tutorial/?completed=/basic-gui-pyqt-tutorial/

import sys
from PyQt4 import QtGui

class Window(QtGui.QMainWindow):
	def __init__(self):			# Cu phap khi su dung class trong Python
		super(Window, self).__init__()
		self.InitWindow()

	def InitWindow(self):			# Tao ra mot cua so don 
		self.setGeometry(50, 50, 500, 300)		# Xac dinh vi tri va kich thuoc cua so
		self.setWindowTitle("PyQT Tuts!")		# Dat tieu de cho cua so
		self.setWindowIcon(QtGui.QIcon('python.jpg'))	# Dat Icon cho cua so giao dien
		self.show()					# Hien thi cua so vua tao len man hinh

def CreatGUI():					# Tao ung dung giao dien
	app = QtGui.QApplication(sys.argv)
	GUI = Window()						
	sys.exit(app.exec_())

if __name__ == '__main__':
	CreatGUI()

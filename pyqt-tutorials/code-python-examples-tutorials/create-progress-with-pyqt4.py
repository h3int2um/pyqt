# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Thoi gian: 24-09-2016
# Noi dung: Tao thanh xu ly voi PyQt4
# Tham khao:
#	1. https://pythonprogramming.net/progress-bar-pyqt-tutorial/
#	2. http://zetcode.com/gui/pyqt4/firstprograms/

import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
	def __init__(self):			# Cu phap khi su dung class trong Python
		super(Window, self).__init__()
		self.InitWindow()
		self.CreateButton_Quit()
		self.CreateMenubar()
		self.CreateToolbar()
		self.CreateCheckbox()
		self.CreateProgress()

	def InitWindow(self):			# Tao ra mot cua so don 
		self.setGeometry(50, 50, 500, 300)		# Xac dinh vi tri va kich thuoc cua so
		self.setWindowTitle("PyQT Tuts!")		# Dat tieu de cho cua so
		self.setWindowIcon(QtGui.QIcon('python.jpg'))	# Dat Icon cho cua so giao dien
	
	def CreateButton_Quit(self):		# Tao nut nhan chuc nang
		btn = QtGui.QPushButton("Quit!", self)
		btn.clicked.connect(QtCore.QCoreApplication.instance().quit)	# Thuc hien chuc nang Exit
		btn.setGeometry(150, 100, 150, 50)              		# Xac dinh vi tri va kich thuoc cua nut nhan

	def CreateMenubar(self):		# Tao menubar thuc hien chuc nang
		extractAction = QtGui.QAction("&Exit", self)			# Menu con Edit trong Menu chinh
		extractAction.setShortcut("Ctrl+Q")				# Phim tat cho Menu con
		extractAction.setStatusTip('Leave The App')			# Bao trang thai khi chon Menu
		extractAction.triggered.connect(self.close_application)		# Thuc hien chuc nang trong ham close_application

		self.statusBar()
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')				# Tao menu chinh ten la File
		fileMenu.addAction(extractAction)				# Menu chinh gom menu con dinh nghia o extractAction
		
	def CreateToolbar(self):
		extractAction = QtGui.QAction(QtGui.QIcon('quit.png'), 'Exit', self)	# Dat icon va tieu de bieu tuong tren toolbar
		extractAction.triggered.connect(self.close_application)			# Thuc hien chuc nang trong ham close_application
        
		self.toolBar = self.addToolBar("Extraction")				# Dinh nghia ten toolbar, click chuot phai de quan sat
		self.toolBar.addAction(extractAction)					# Them chuc nang vua xay dung len thanh toolbar		
		
	def CreateCheckbox(self):		# Tao nut checkbox thuc hien chuc nang
		checkBox = QtGui.QCheckBox('Quit', self)				# Dat ten cho nut Checkbox
		checkBox.move(50, 10)							# Vi tri cua nut checkbox
		checkBox.stateChanged.connect(self.close_gui)				# Khi click vao checkbox thi thuc hien chuc nang trong ham close_gui
		
	def CreateProgress(self):		# Tao thanh xu ly
		self.progress = QtGui.QProgressBar(self)				# Khai bao tao thanh xu ly
		self.progress.setGeometry(200, 60, 250, 20)				# Vi tri va kich thuoc cua thanh xu ly
		self.btn = QtGui.QPushButton("Download",self)				# Ten nut nhan cua thanh xu ly la Download
		self.btn.move(270,20)							# Vi tri cua nut nhan Download
		self.btn.clicked.connect(self.download)					# Click vao nut Download the hien toc do cua thanh trang thai
		self.show()								# Hien thi cua so vua tao len man hinh
		
	def close_application(self):
		# Dat ten cua khung tin nhan la 'Extract!', thong bao xac nhan la "You are sure?" va tao 2 nut Yes, No trong khung thong bao
		choice = QtGui.QMessageBox.question(self, 'Extract!', "You are sure?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)                                            
		if choice == QtGui.QMessageBox.Yes:					# Neu chon Yes thi thoat
			sys.exit()
		else:									# Neu chon No thi khong lam gi
			pass

	def close_gui(self, state):
		if state == QtCore.Qt.Checked:
			sys.exit()
		else:
			pass
			
	def download(self):		# Tinh phan tram cua thanh xu ly
		self.completed = 0

		while self.completed < 100:
			self.completed += 0.0001
			self.progress.setValue(self.completed)

def CreatGUI():					# Tao ung dung giao dien
	app = QtGui.QApplication(sys.argv)
	GUI = Window()						
	sys.exit(app.exec_())

if __name__ == '__main__':
	CreatGUI()

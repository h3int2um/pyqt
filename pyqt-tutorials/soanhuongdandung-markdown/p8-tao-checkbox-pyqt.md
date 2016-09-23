# Tạo checkbox với PyQt4

Thực hiện: Thi Minh Nhựt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 23 tháng 9 năm 2016

## Tài liệu tham khảo

1. [PyQT Check box](https://pythonprogramming.net/check-box-pyqt-tutorial/)

2. [First programs in PyQt4](http://zetcode.com/gui/pyqt4/firstprograms/)

## Tạo checkbox với PyQt4

* Khởi tạo nút checkbox.

* Của sổ giao diện được khởi tạo như hình dưới:

![](https://raw.githubusercontent.com/h3int2um/pyqt/master/pyqt-tutorials/images-examples-tutorials/create-checkbox-with-pyqt4.png)

* Mô tả chức năng: kích chọn checkbox (`Quit`) thì thực hiện một chức năng nào đó (cụ thể là đóng giao diện).

## Cách thực hiện

* Phần code

		import sys

		from PyQt4 import QtGui, QtCore

		class Window(QtGui.QMainWindow):
	
			def __init__(self):
				
				super(Window, self).__init__()
				
				self.InitWindow()
				
				self.CreateButton_Quit()
				
				self.CreateMenubar()
				
				self.CreateToolbar()
				
				self.CreateCheckbox()

			
			def InitWindow(self):
				
				self.setGeometry(50, 50, 500, 300)
				
				self.setWindowTitle("PyQT Tuts!")
				
				self.setWindowIcon(QtGui.QIcon('python.jpg'))
	
			
			def CreateButton_Quit(self):
				
				btn = QtGui.QPushButton("Quit!", self)
				
				btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
				
				btn.setGeometry(150, 100, 150, 50)

			
			def CreateMenubar(self):
				
				extractAction = QtGui.QAction("&Exit", self)
				
				extractAction.setShortcut("Ctrl+Q")
				
				extractAction.setStatusTip('Leave The App')
				
				extractAction.triggered.connect(self.close_application)

		
				self.statusBar()
				
				mainMenu = self.menuBar()
				
				fileMenu = mainMenu.addMenu('&File')
				
				fileMenu.addAction(extractAction)
		
			
			def CreateToolbar(self):
			
				extractAction = QtGui.QAction(QtGui.QIcon('quit.png'), 'Exit', self)
				
				extractAction.triggered.connect(self.close_application)
				
        
				self.toolBar = self.addToolBar("Extraction")
				
				self.toolBar.addAction(extractAction)
			
			
			def CreateCheckbox(self):
			
				checkBox = QtGui.QCheckBox('Quit', self)
				
				checkBox.move(50, 10)
				
				checkBox.stateChanged.connect(self.close_gui)
				
				self.show()	
				

			def close_application(self):
		
				choice = QtGui.QMessageBox.question(self, 'Extract!', "You are sure?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
				
				if choice == QtGui.QMessageBox.Yes:
				
					sys.exit()
				
				else:
					pass
					
					
			def close_gui(self, state):
				
				if state == QtCore.Qt.Checked:
					
					sys.exit()
				
				else:
					
					pass
					

		def CreatGUI():
			
			app = QtGui.QApplication(sys.argv)
			
			GUI = Window()						
			
			sys.exit(app.exec_())


		if __name__ == '__main__':
			
			CreatGUI()

* Phần mã nguồn tải về: 
	
	+ [Code](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/code-python-examples-tutorials/create-checkbox-with-pyqt4.py).
	
	+ [Python Logo](https://raw.githubusercontent.com/h3int2um/pyqt/master/pyqt-tutorials/code-python-examples-tutorials/python.jpg).
	
	+ [Quit button](https://raw.githubusercontent.com/h3int2um/pyqt/master/pyqt-tutorials/code-python-examples-tutorials/quit.png).

* Phần giải thích:

	+ Một số phần được giải thích tương tự như hướng dẫn trong:
		
		- [Phần 3: Tạo cửa sổ giao diện đơn giản với PyQt4](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/soanhuongdandung-markdown/p3-tao-cuaso-dongian-pyqt.md).
		
		- [Phần 4: Tạo nút nhấn chức năng với PyQt4](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/soanhuongdandung-markdown/p4-tao-nutnhan-pyqt.md).
		
		- [Phần 5: Tạo menubar giao tiếp giao diện với PyQt4](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/soanhuongdandung-markdown/p5-tao-menubar-pyqt.md).
		
		- [Phần 6: Tạo thanh toolbar giao tiếp giao diện với PyQt4](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/soanhuongdandung-markdown/p6-tao-toolbar-pyqt.md).
		
		- [Phần 7: Tạo thông báo tin nhắn với PyQt4](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/soanhuongdandung-markdown/p7-bat-message-pyqt.md).
	
	+ Tạo nút checkbox:
	
		- Lệnh `checkBox = QtGui.QCheckBox('Quit', self)`: Đặt tên cho nút checkbox.
		
		- Lệnh `checkBox.move(50, 10)`: Vị trí của nút checkbox.
		
		- Lệnh `checkBox.stateChanged.connect(self.close_gui)`: khi click chọn nút checkbox thì thực hiện chức năng 
		trong hàm `close_gui`.
		
		- Lệnh `self.show()`: lệnh `show()` nằm trong phần tạo checkbox thì khi tạo giao diện mới xuất hiện nút checkbox.

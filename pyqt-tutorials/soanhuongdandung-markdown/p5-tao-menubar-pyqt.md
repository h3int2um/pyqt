# Tạo menubar giao tiếp giao diện với PyQt4

Thực hiện: Thi Minh Nhựt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 20 tháng 9 năm 2016

## Tài liệu tham khảo

1. [PyQT Menubar](https://pythonprogramming.net/menubar-pyqt-tutorial/)

2. [First programs in PyQt4](http://zetcode.com/gui/pyqt4/firstprograms/)

## Tạo menubar với PyQt4

* Khởi tạo thanh menubar.

* Trong menubar có các lệnh con thực hiện chức năng.

* Của sổ giao diện được khởi tạo như hình dưới:

![](https://raw.githubusercontent.com/h3int2um/pyqt/master/pyqt-tutorials/images-examples-tutorials/create-menu-with-pyqt4.png)

* Mô tả chức năng của menu `File`: kích vào menu `File` có menu con là `Exit Ctrl+Q`. Khi chọn `Exit` hoặc nhấn phím tắt `Ctrl+Q` 
thì đều đóng giao diện lại.

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

			
			def InitWindow(self):
				
				self.setGeometry(50, 50, 500, 300)
				
				self.setWindowTitle("PyQT Tuts!")
				
				self.setWindowIcon(QtGui.QIcon('python.jpg'))
	
			
			def CreateButton_Quit(self):
				
				btn = QtGui.QPushButton("Quit!", self)
				
				btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
				
				btn.setGeometry(150, 100, 150, 50)
				
				self.show()

			
			def CreateMenubar(self):
				
				extractAction = QtGui.QAction("&Exit", self)
				
				extractAction.setShortcut("Ctrl+Q")
				
				extractAction.setStatusTip('Leave The App')
				
				extractAction.triggered.connect(self.close_application)

		
				self.statusBar()
				
				mainMenu = self.menuBar()
				
				fileMenu = mainMenu.addMenu('&File')
				
				fileMenu.addAction(extractAction)
		

			def close_application(self):
		
				sys.exit()


		def CreatGUI():
			
			app = QtGui.QApplication(sys.argv)
			
			GUI = Window()						
			
			sys.exit(app.exec_())


		if __name__ == '__main__':
			
			CreatGUI()

* Phần mã nguồn tải về: 
	
	+ [Code](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/code-python-examples-tutorials/create-menubar-with-pyqt4.py).
	
	+ [Python Logo](https://raw.githubusercontent.com/h3int2um/pyqt/master/pyqt-tutorials/code-python-examples-tutorials/python.jpg).

* Phần giải thích:

	+ Một số phần được giải thích tương tự như hướng dẫn trong:
		
		- [Phần 3: Tạo cửa sổ giao diện đơn giản với PyQt4](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/soanhuongdandung-markdown/p3-tao-cuaso-dongian-pyqt.md).
		
		- [Phần 4: Tạo nút nhấn chức năng với PyQt4](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/soanhuongdandung-markdown/p4-tao-nutnhan-pyqt.md).
	
	+ Tạo menubar:
	
		- Lệnh `extractAction = QtGui.QAction("&Exit", self)`: tạo menu con có tên là `Exit` trong menu chính (được định nghĩa phía dưới).
		
		- Lệnh `extractAction.setShortcut("Ctrl+Q")`: tạo phím tắt cho menu con.
		
		- Lệnh `extractAction.setStatusTip('Leave The App')`: báo trạng thái khi chọn menu.
		
		- Lệnh `extractAction.triggered.connect(self.close_application)`: khi chọn vào menu con là `Exit` 
		thực hiện chức năng được viết trong hàm `close_application` (cụ thể là đóng giao diện).
		
		- Các lệnh `self.statusBar()` và `mainMenu = self.menuBar()`: định nghĩa theo cú pháp trong PyQt4.
		
		- Lệnh `fileMenu = mainMenu.addMenu('&File')`: tạo menu chính tên là `File`.
		
		- Lệnh `fileMenu.addAction(extractAction)`: trong menu chính `File` có menu con `Exit` được định nghĩa ở `extractAction`.

# Tạo thông báo tin nhắn với PyQt4

Thực hiện: Thi Minh Nhựt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 22 tháng 9 năm 2016

## Tài liệu tham khảo

1. [Pop up Message PyQT](https://pythonprogramming.net/pop-up-messages-pyqt-tutorial/)

2. [First programs in PyQt4](http://zetcode.com/gui/pyqt4/firstprograms/)

## Tạo thông báo tin nhắn với PyQt4

* Khởi tạo khung thông báo.

* Trên khung thông báo có 2 nút: `Yes` và `No`.

* Của sổ giao diện được khởi tạo như hình dưới:

![](https://raw.githubusercontent.com/h3int2um/pyqt/master/pyqt-tutorials/images-examples-tutorials/pop-up-message-with-pyqt4.png)

* Mô tả chức năng của nút trên khung thông báo: kích vào nút `Yes` thì đóng giao diện, click vào nút `No` thì trở lại trạng thái cũ.

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
		
			
			def CreateToolbar(self):
			
				extractAction = QtGui.QAction(QtGui.QIcon('quit.png'), 'Exit', self)
				
				extractAction.triggered.connect(self.close_application)
				
        
				self.toolBar = self.addToolBar("Extraction")
				
				self.toolBar.addAction(extractAction)
			

			def close_application(self):
		
				choice = QtGui.QMessageBox.question(self, 'Extract!', "You are sure?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
				
				if choice == QtGui.QMessageBox.Yes:
				
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
	
	+ [Code](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/code-python-examples-tutorials/pop-up-message-with-pyqt4.py).
	
	+ [Python Logo](https://raw.githubusercontent.com/h3int2um/pyqt/master/pyqt-tutorials/code-python-examples-tutorials/python.jpg).
	
	+ [Quit button](https://raw.githubusercontent.com/h3int2um/pyqt/master/pyqt-tutorials/code-python-examples-tutorials/quit.png).

* Phần giải thích:

	+ Một số phần được giải thích tương tự như hướng dẫn trong:
		
		- [Phần 3: Tạo cửa sổ giao diện đơn giản với PyQt4](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/soanhuongdandung-markdown/p3-tao-cuaso-dongian-pyqt.md).
		
		- [Phần 4: Tạo nút nhấn chức năng với PyQt4](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/soanhuongdandung-markdown/p4-tao-nutnhan-pyqt.md).
		
		- [Phần 5: Tạo menubar giao tiếp giao diện với PyQt4](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/soanhuongdandung-markdown/p5-tao-menubar-pyqt.md).
		
		- [Phần 6: Tạo thanh toolbar giao tiếp giao diện với PyQt4](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/soanhuongdandung-markdown/p6-tao-toolbar-pyqt.md).
	
	+ Tạo khung tin nhắn thông báo:
	
		- Lệnh `choice = QtGui.QMessageBox.question(self, 'Extract!', "You are sure?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)`: đặt tên cho khung thông báo là `Extract!`, 
		thông báo xác nhận `You are sure?` khi lựa chọn `Yes` hoặc `No` và tạo 2 nút `Yes`, `No`.
		
		- Lệnh `if choice == QtGui.QMessageBox.Yes:` so sánh hành động nếu click chọn nút `Yes` thì thực hiện chức năng gì đó bên dưới.

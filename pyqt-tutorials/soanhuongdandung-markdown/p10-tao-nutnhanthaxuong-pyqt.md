# Tạo nút nhấn thả xuống với PyQt4

Thực hiện: Thi Minh Nhựt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 25 tháng 9 năm 2016

## Tài liệu tham khảo

1. [PyQT Dropdown button and QT Styles](https://pythonprogramming.net/drop-down-button-window-styles-pyqt-tutorial/)

2. [First programs in PyQt4](http://zetcode.com/gui/pyqt4/firstprograms/)

## Tạo nút nhấn thả xuống với PyQt4

* Tạo nút nhấn thả xuống với các nút nhấn nhỏ, kích vào nút nhấn thay đổi giao diện.

* Của sổ giao diện được khởi tạo như hình dưới:

	+ Với hệ điều hành hiện tại - Ubuntu thì style của giao diện:
	
		![](https://raw.githubusercontent.com/h3int2um/pyqt/master/pyqt-tutorials/images-examples-tutorials/create-dropdown-button-style-ubuntu-with-pyqt4.png)
		
	+ Với hệ điều hành hiện tại - Ubuntu chọn `motif` thì style của giao diện:
	
		![](https://raw.githubusercontent.com/h3int2um/pyqt/master/pyqt-tutorials/images-examples-tutorials/create-dropdown-button-style-motif-with-pyqt4.png)
		
	+ Với hệ điều hành hiện tại - Ubuntu chọn `Windows` thì style của giao diện:
	
		![](https://raw.githubusercontent.com/h3int2um/pyqt/master/pyqt-tutorials/images-examples-tutorials/create-dropdown-button-style-windows-with-pyqt4.png)
		
	+ Với hệ điều hành hiện tại - Ubuntu chọn `cde` thì style của giao diện:
	
		![](https://raw.githubusercontent.com/h3int2um/pyqt/master/pyqt-tutorials/images-examples-tutorials/create-dropdown-button-style-cde-with-pyqt4.png)
		
	+ Với hệ điều hành hiện tại - Ubuntu chọn `Plastique` thì style của giao diện:
	
		![](https://raw.githubusercontent.com/h3int2um/pyqt/master/pyqt-tutorials/images-examples-tutorials/create-dropdown-button-style-plastique-with-pyqt4.png)
		
	+ Với hệ điều hành hiện tại - Ubuntu chọn `Cleanlooks` thì style của giao diện:
	
		![](https://raw.githubusercontent.com/h3int2um/pyqt/master/pyqt-tutorials/images-examples-tutorials/create-dropdown-button-style-cleanlooks-with-pyqt4.png)
		
	+ Với hệ điều hành hiện tại - Ubuntu chọn `windowsvista` thì style của giao diện:
	
		![](https://raw.githubusercontent.com/h3int2um/pyqt/master/pyqt-tutorials/images-examples-tutorials/create-dropdown-button-style-windowsvista-with-pyqt4.png)

* Mô tả chức năng: Khi click chọn vào các nút trong danh sách của nút nhấn thả xuống thì thay đổi giao diện và thông báo style 
của giao diện đang chọn.

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
				
				self.CreateProgress()
				
				self.CreatDropdownButton()

			
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
				
				
			def CreateProgress(self):
			
				self.progress = QtGui.QProgressBar(self)
				
				self.progress.setGeometry(200, 60, 250, 20)
				
				self.btn = QtGui.QPushButton("Download",self)
				
				self.btn.move(270,20)
								
				self.btn.clicked.connect(self.download)
				
			def CreatDropdownButton(self):
				
				self.styleChoice = QtGui.QLabel("Ubuntu", self)
				
        
				comboBox = QtGui.QComboBox(self)
		
				comboBox.addItem("motif")
						
				comboBox.addItem("Windows")
				
				comboBox.addItem("cde")
				
				comboBox.addItem("Plastique")
				
				comboBox.addItem("Cleanlooks")
				
				comboBox.addItem("windowsvista")
				
				self.styleChoice.move(50,150)
		
				
				comboBox.activated[str].connect(self.style_choice)
				
				comboBox.move(50, 250)
				
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
					
			
			def download(self):
			
				self.completed = 0

				while self.completed < 100:
				
					self.completed += 0.0001
					
					self.progress.setValue(self.completed)
					
		
			def style_choice(self, text):
			
				self.styleChoice.setText(text)
						
				QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))		
		
					

					
		def CreatGUI():
			
			app = QtGui.QApplication(sys.argv)
			
			GUI = Window()						
			
			sys.exit(app.exec_())


		if __name__ == '__main__':
			
			CreatGUI()

* Phần mã nguồn tải về: 
	
	+ [Code](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/code-python-examples-tutorials/create-dropdown-button-with-pyqt4.py).
	
	+ [Python Logo](https://raw.githubusercontent.com/h3int2um/pyqt/master/pyqt-tutorials/code-python-examples-tutorials/python.jpg).
	
	+ [Quit button](https://raw.githubusercontent.com/h3int2um/pyqt/master/pyqt-tutorials/code-python-examples-tutorials/quit.png).

* Phần giải thích:

	+ Một số phần được giải thích tương tự như hướng dẫn trong:
		
		- [Phần 3: Tạo cửa sổ giao diện đơn giản với PyQt4](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/soanhuongdandung-markdown/p3-tao-cuaso-dongian-pyqt.md).
		
		- [Phần 4: Tạo nút nhấn chức năng với PyQt4](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/soanhuongdandung-markdown/p4-tao-nutnhan-pyqt.md).
		
		- [Phần 5: Tạo menubar giao tiếp giao diện với PyQt4](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/soanhuongdandung-markdown/p5-tao-menubar-pyqt.md).
		
		- [Phần 6: Tạo thanh toolbar giao tiếp giao diện với PyQt4](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/soanhuongdandung-markdown/p6-tao-toolbar-pyqt.md).
		
		- [Phần 7: Tạo thông báo tin nhắn với PyQt4](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/soanhuongdandung-markdown/p7-bat-message-pyqt.md).
		
		- [Phần 8: Tạo checkbox với PyQt4](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/soanhuongdandung-markdown/p8-tao-checkbox-pyqt.md).
		
		- [Phần 9: Tạo thanh xử lý với PyQt4](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/soanhuongdandung-markdown/p9-tao-thanhxuly-pyqt.md).
	
	+ Tạo nút nhấn thả xuống:
	
		- Lệnh `self.styleChoice = QtGui.QLabel("Ubuntu", self)`: đặt label của style hiện tại.
		
		- Lệnh `comboBox = QtGui.QComboBox(self)`: định nghĩa một nút nhấn thả xuống.
		
		- Lệnh `comboBox.addItem` với các tham số `motif, Windows, cde, Plastique, Cleanlooks, windowsvista`: tên của nút nhấn 
		trong nút nhấn thả xuống.
		
		- Lệnh `self.styleChoice.move(50,150)`: vị trí của label tương ứng khi chọn nút nhấn trong nút nhấn thả xuống.
		
		- Lệnh `comboBox.activated[str].connect(self.style_choice)`: thực hiện chức năng trong hàm `style_choice` khi chọn 
		nút nhấn trong nút nhấn thả xuống.
		
		- Lệnh `comboBox.move(50, 250)`: vị trí của nút nhấn thả xuống.
		
		- Lệnh `self.show()`: lệnh `show()` nằm trong phần tạo nút nhấn thả xuống thì khi tạo giao diện mới xuất hiện 
		nút nhấn thả xuống.
		
		- Hàm `style_choice(self, text)` thực hiện chức năng thay đổi style của giao diện khi click chọn nút nhấn 
		thả xuống qua lệnh `QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))` (Xem tài liệu về [QStyleFactory](http://doc.qt.io/qt-4.8/qstylefactory.html) 
		để có nhiều thông tin hơn).
		
		- Lệnh `self.styleChoice.setText(text)` trong hàm `style_choice`: đặt label tương ứng khi thay style của 
		giao diện.

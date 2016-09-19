# Tạo nút nhấn giao tiếp trong giao diện với PyQt4

Thực hiện: Thi Minh Nhựt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 19 tháng 9 năm 2016

## Tài liệu tham khảo

1. [PyQT buttons](https://pythonprogramming.net/buttons-pyqt-tutorial/)

2. [Button Functions with PyQT](https://pythonprogramming.net/button-functions-pyqt-tutorial/)

3. [First programs in PyQt4](http://zetcode.com/gui/pyqt4/firstprograms/)

## Tạo nút nhấn chức năng với PyQt4

* Khởi tạo nút nhấn thực hiện chức năng cụ thể nào đó.

* Của sổ giao diện được khởi tạo như hình dưới:

![](https://raw.githubusercontent.com/h3int2um/pyqt/master/pyqt-tutorials/images-examples-tutorials/create-button-with-pyqt4.png)

* Mô tả chức năng của nút nhấn:
	
	+ Click chọn nút nhấn `Button Hello!`: print ra dòng chữ là `Hello PyQt4!` trên Terminal.
	
	+ Click chọn nút nhấn `Quit!`: thì đóng cửa sổ giao diện vừa tạo.


## Cách thực hiện

* Phần code
		
		import sys
		
		from PyQt4 import QtGui, QtCore

		class Window(QtGui.QMainWindow):
	
			def __init__(self):
		
				super(Window, self).__init__()
				
				self.InitWindow()
				
				self.CreateButton_Hello()
				
				self.CreateButton_Quit()


			def InitWindow(self):
			
				self.setGeometry(50, 50, 500, 300)
			
				self.setWindowTitle("PyQT Tuts!")
			
				self.setWindowIcon(QtGui.QIcon('python.jpg'))
	
	
			def CreateButton_Hello(self):
		
				btn = QtGui.QPushButton("Button Hello!", self)
		
				btn.clicked.connect(self.ButtonFunction_Hello)
		
				btn.setGeometry(100, 100, 150, 50)
	
		
			def CreateButton_Quit(self):
			
				btn = QtGui.QPushButton("Quit!", self)
		
				btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
			
				btn.setGeometry(300, 100, 150, 50)
			
				self.show()

			def ButtonFunction_Hello(self):
			
				print 'Hello PyQt4!'

		
		
		def CreatGUI():
			
			app = QtGui.QApplication(sys.argv)
			
			GUI = Window()						
			
			sys.exit(app.exec_())


		if __name__ == '__main__':
		
			CreatGUI()

* Phần mã nguồn tải về: 
	
	+ [Code](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/code-python-examples-tutorials/create-button-with-pyqt4.py).
	
	+ [Python Logo](https://raw.githubusercontent.com/h3int2um/pyqt/master/pyqt-tutorials/code-python-examples-tutorials/python.jpg).

* Phần giải thích:

	+ Một số phần được giải thích tương tự như hướng dẫn ở - [Phần 3: Tạo cửa sổ giao diện đơn giản với PyQt4](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/soanhuongdandung-markdown/p3-tao-cuaso-dongian-pyqt.md).
	
	+ Tạo nút nhấn chức năng:
		
		- Cần import thêm module `QtCore` (nếu sử dụng một số chức năng do PyQt4 định nghĩa sẵn).
		
		- Đặt tên cho nút nhấn `btn = QtGui.QPushButton("Ten nut nhan", self)`.
		
		- Liên kết nút nhấn đến một chức năng muốn thực hiện: `btn.clicked.connect(self.name_function)`
		
		Ví dụ 1: `btn.clicked.connect(self.ButtonFunction_Hello)`: thực hiện chức năng của hàm `ButtonFunction_Hello` 
		do người viết định nghĩa (in ra dòng chữ `Hello PyQt4!`).
		
		Ví dụ 2: `btn.clicked.connect(QtCore.QCoreApplication.instance().quit)`: thực hiện chức năng là thoát khỏi giao diện 
		(do PyQt4 định nghĩa).
		
		- Để hiển thị giao diện dùng lệnh `self.show()` trong hàm cuối cùng (nếu dùng ở những hàm trước thì các hàm còn lại 
		không được thể hiện lên giao diện).
		
		Ví dụ: Có 3 hàm `self.InitWindow()`, `self.CreateButton_Hello()` và `self.CreateButton_Quit()` trong lớp `Window` 
		và được gọi theo thứ tự này, hàm `self.show()` được khai báo ở hàm `CreateButton_Quit` (hàm cuối) thì mới thể hiện được 
		chức năng của giao diện.
		
		

# Tạo một cửa sổ giao diện đơn giản với PyQt4

Thực hiện: Thi Minh Nhựt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 17 tháng 9 năm 2016

## Tài liệu tham khảo

1. [PyQT Basic Tutorial](https://pythonprogramming.net/basic-gui-pyqt-tutorial/)

2. [PyQT Application Structure](https://pythonprogramming.net/application-structure-pyqt-tutorial/)

3. [First programs in PyQt4](http://zetcode.com/gui/pyqt4/firstprograms/)

## Tạo một cửa sổ giao diện đơn giản

* Trong phần này, chúng ta sẽ tạo một cửa sổ đơn giản gồm:

	- Xác định kích thước cửa sổ.

	- Đặt tiêu đề cho cửa sổ.

	- Đặt icon cho cửa sổ.
	
	- Hiển thị cửa sổ giao diện vừa tạo ra lên màn hình.
	
* Của sổ giao diện được khởi tạo như hình dưới:

![](https://raw.githubusercontent.com/h3int2um/pyqt/master/pyqt-tutorials/images-examples-tutorials/create-window-simple-with-pyqt4.png)

## Cách thực hiện

* Phần code

		import sys
		
		from PyQt4 import QtGui
		
		class Window(QtGui.QMainWindow):
		
			def __init__(self):
			
				super(Window, self).__init__()
				
				self.InitWindow()

			
			def InitWindow(self):
			
				self.setGeometry(50, 50, 500, 300)
				
				self.setWindowTitle("PyQT tuts!")
				
				self.setWindowIcon(QtGui.QIcon('python.jpg'))
				
				self.show()



		def CreatGUI():
		
			app = QtGui.QApplication(sys.argv)
			
			GUI = Window()
			
			sys.exit(app.exec_())

		if __name__ == '__main__':
			CreatGUI()
		
* Phần mã nguồn tải về: 

	+ [Code](https://github.com/h3int2um/pyqt/blob/master/pyqt-tutorials/code-python-examples-tutorials/create-window-simple-with-pyqt4.py).

	+ [Python Logo](https://raw.githubusercontent.com/h3int2um/pyqt/master/pyqt-tutorials/code-python-examples-tutorials/python.jpg).

* Phần giải thích:

	- Import vào những module cần thiết:
	
			import sys
			
			from PyQt4 import QtGui
			
		+ Module `sys` cho phép giao diện thao tác với chế độ dòng lệnh.
		
		+ Module `QtGui` là module cốt lõi cho phép thao tác với các lệnh tạo giao diện với PyQt4.
		
	- Tạo lớp có tên là `Window` kế thừa lớp `QtGui.QMainWindow`:
	
			class Window(QtGui.QMainWindow):
			
				def __init__(self):
			
					super(Window, self).__init__()
				
					self.InitWindow()
				

				def InitWindow(self):
			
					self.setGeometry(50, 50, 500, 300)
				
					self.setWindowTitle("PyQT tuts!")
				
					self.setWindowIcon(QtGui.QIcon('python.jpg'))
				
					self.show()
				
		+ Lệnh `self.InitWindow()`: gọi hàm `InitWindow` khi gọi lớp `Window` sau này.
		
		+ Hàm `InitWindow`: thực hiện chức năng tao một cửa sổ đơn giản gồm vị trí và kích thước cửa sổ, 
		tiêu đề và logo cho cửa sổ, hiển thị cửa sổ vừa tạo lên màn hình.
		
			- Lệnh `setGeometry(50, 50, 500, 300)`: Xác định vị trí và kích thước cửa sổ. 
			Vị trí là `(x, y) = (50,50)` và kích thước là chiều rộng `width = 500px`, chiều cao `height = 300px`.
			
			- Lệnh `setWindowTitle("PyQT tuts!")`: Đặt tiêu đề cho cửa sổ là `PyQT tuts!`.
			
			- Lệnh `setWindowIcon(QtGui.QIcon('python.jpg'))`: Đặt icon cho cửa sổ giao diện là logo của 
			[python](https://raw.githubusercontent.com/h3int2um/pyqt/master/pyqt-tutorials/code-python-examples-tutorials/python.jpg).
			
			- Lệnh `show()`: Hiển thị cửa sổ vừa tạo lên màn hình.
			
	- Hàm `CreatGUI`: tạo ra một ứng dụng giao diện.
	
		+ Lệnh `app = QtGui.QApplication(sys.argv)`: tạo ra ứng dụng (lệnh bắt buộc).
		
		+ Lệnh `GUI = Window()`: Gọi đến lớp `Window` được định nghĩa ở phần trên và thực hiện hàm `InitWindow` 
		(để tạo ra một cửa sổ đơn giản).
		
		+ Lệnh `sys.exit(app.exec_())`: xóa các mã code khi thoát (click vào biểu tượng exit).
			
				
		

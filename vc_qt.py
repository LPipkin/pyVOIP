import sys
from PyQt4 import QtGui, QtCore

class MainGui(QtGui.QMainWindow):
	def __init__(self):
		super(MainGui,self).__init__()
		self.initUI()
	
	def initUI(self):
		exitAction = QtGui.QAction('Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(QtGui.qApp.quit)
			
		menubar  = QtGui.QMenuBar(self) 
		fileMenu = menubar.addMenu('File')
		fileMenu.addAction(exitAction)

		btn = QtGui.QPushButton('Talk..',self)

		button_layout = QtGui.QHBoxLayout()
		button_layout.addWidget(btn)

		main_layout = QtGui.QVBoxLayout()
		main_layout.addStretch()
		main_layout.addLayout(button_layout)

		central_widget = QtGui.QWidget()
		central_widget.setLayout(main_layout)
		self.setCentralWidget(central_widget)

		self.setGeometry(700,700,450,450)
		self.show()

app = QtGui.QApplication(sys.argv)
ex = MainGui()
ex.move(300,300)
app.exec_()

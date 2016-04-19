import sys
import os
from workingplayback import WorkingPlayback
from workingrecording_presskey import WorkingRecording
from PyQt4 import QtGui, QtCore
import threading
import pyautogui

class Window(QtGui.QMainWindow):

	def __init__(self):
		super(Window,self).__init__()
		self.setGeometry(50,50,300,300)
		self.setWindowTitle("Voice chat")
		self.home()

	#def enter(self):
		#raw_input("hello")
		#os.system(cmd)


	def rec_thread(self):
		t = threading.Thread(target=WorkingRecording)
		t.start()
		#t.join()
	def rec_call(self,list):
		WorkingRecording


	def home(self):
		strt_btn = QtGui.QPushButton("Push me to start recording!", self)
		play_btn = QtGui.QPushButton("Push me to grab a message!", self)
		stop_btn = QtGui.QPushButton("Push me to stop recording!", self)


		strt_btn.clicked.connect(self.rec_thread)
		
		play_btn.clicked.connect(WorkingPlayback)
		play_btn.resize(300,100)
		play_btn.move(0,0)

		strt_btn.resize(300,100)
		strt_btn.move(0,100)
		
		#stop_btn.clicked.connect(self.enter)
		stop_btn.resize(300,100)
		stop_btn.move(0,200)

		self.show()

	
app = QtGui.QApplication(sys.argv)
gui = Window()
sys.exit(app.exec_())
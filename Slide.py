<<<<<<< HEAD
##################################################################################################
##################################################################################################
####                              Made by Maurice D'Moss                                    ######
####                Python Script to control/Emulate the windows Volume Mixer               ######
####    I use this while opening two separate youtube windows and changing the slider       ######
####          position to acheive a Fade-in/Fade-out Transition b/w two songs               ######
##################################################################################################
##################################################################################################
from __future__ import print_function
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLCDNumber, QSlider, QVBoxLayout)
from PyQt5.QtCore import Qt

class AppDemo(QWidget):
	def __init__(self):
		super().__init__()
		self.resize(500, 50)
		self.setWindowTitle('Volume Mixer!')

		slider = QSlider(Qt.Horizontal)
		slider.setMaximum(100)
		slider.setMinimum(0)
		vol = int(self.getVol()*100)
		slider.setValue(vol)

		layout = QVBoxLayout()
		layout.addWidget(slider)
		self.setLayout(layout)
		slider.valueChanged.connect(self.SetVol)

	def getVol(self):
		session = AudioUtilities.GetAllSessions()
		volume = session[1]._ctl.QueryInterface(ISimpleAudioVolume)
		return(float(volume.GetMasterVolume()))

	def SetVol(self,value):
		session = AudioUtilities.GetAllSessions()
		volume1 = session[1]._ctl.QueryInterface(ISimpleAudioVolume)
		vol1 = value/100
		volume1.SetMasterVolume(float(vol1), None)
		volume2 = session[2]._ctl.QueryInterface(ISimpleAudioVolume)
		vol2 = 1 - value/100
		volume2.SetMasterVolume(float(vol2), None)

if __name__ == '__main__':
	app = QApplication(sys.argv)

	demo = AppDemo()
	demo.show()

=======
##################################################################################################
##################################################################################################
####                              Made by Maurice D'Moss                                    ######
####                Python Script to control/Emulate the windows Volume Mixer               ######
####    I use this while opening two separate youtube windows and changing the slider       ######
####          position to acheive a Fade-in/Fade-out Transition b/w two songs               ######
##################################################################################################
##################################################################################################
from __future__ import print_function
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLCDNumber, QSlider, QVBoxLayout)
from PyQt5.QtCore import Qt

class AppDemo(QWidget):
	def __init__(self):
		super().__init__()
		self.resize(500, 50)
		self.setWindowTitle('Volume Mixer!')

		slider = QSlider(Qt.Horizontal)
		slider.setMaximum(100)
		slider.setMinimum(0)
		vol = int(self.getVol()*100)
		slider.setValue(vol)

		layout = QVBoxLayout()
		layout.addWidget(slider)
		self.setLayout(layout)
		slider.valueChanged.connect(self.SetVol)

	def getVol(self):
		session = AudioUtilities.GetAllSessions()
		volume = session[1]._ctl.QueryInterface(ISimpleAudioVolume)
		return(float(volume.GetMasterVolume()))

	def SetVol(self,value):
		session = AudioUtilities.GetAllSessions()
		volume1 = session[1]._ctl.QueryInterface(ISimpleAudioVolume)
		vol1 = value/100
		volume1.SetMasterVolume(float(vol1), None)
		volume2 = session[2]._ctl.QueryInterface(ISimpleAudioVolume)
		vol2 = 1 - value/100
		volume2.SetMasterVolume(float(vol2), None)

if __name__ == '__main__':
	app = QApplication(sys.argv)

	demo = AppDemo()
	demo.show()

>>>>>>> 55215aab5951ebff509d3d4ff32f5d533db5271f
	sys.exit(app.exec_())
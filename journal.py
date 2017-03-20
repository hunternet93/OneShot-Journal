import os
import sys
import time
import threading

from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

pipe_path = '/tmp/oneshot-pipe'

class WatchPipe(QThread):
    change_image = pyqtSignal(str)
    
    def run(self):
        while True:
            if os.path.exists(pipe_path): break
            else: time.sleep(0.1)

        pipe = open(pipe_path, 'r')
        pipe.flush()

        while True:
            message = os.read(pipe.fileno(), 256)
            if len(message) > 0:
                self.change_image.emit(message.decode())

            time.sleep(0.05)
            
class Journal(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.stay_on_top = False
        self.setFocusPolicy(Qt.ClickFocus)
                
        self.label = QLabel(self)
        self.change_image('default')
        
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowTitle('OneShot Journal')
        self.setMinimumSize(800, 600)
        self.setMaximumSize(800, 600)
        self.setGeometry(0, 0, 800, 600)
        self.show()
    
    def change_image(self, name):
        self.pixmap = QPixmap('images/{}.png'.format(name))
        self.label.setPixmap(self.pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    journal = Journal()
    
    thread = WatchPipe()
    thread.change_image.connect(journal.change_image)
    thread.start()
    
    app.exec_()

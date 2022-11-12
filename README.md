# linux-pyqt5-ransomeware
practice

# 윈도우 출력

``` python
import sys 
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    
app = QApplication(sys.argv)
window = MyWindow()
window.show() # 화면에 보여지게 함

app.exec_() # 이벤트 루프 시작
```


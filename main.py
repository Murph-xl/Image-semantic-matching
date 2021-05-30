from methods import Main
import sys
from PyQt5.QtWidgets import *
""" 2021年3月12日"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = Main()
    mainwin.show()
    sys.exit(app.exec_())

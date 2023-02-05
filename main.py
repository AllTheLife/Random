from PyQt6.QtWidgets import QApplication
from randomNum import Random
import sys

def main():
    app = QApplication(sys.argv)
    random = Random()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

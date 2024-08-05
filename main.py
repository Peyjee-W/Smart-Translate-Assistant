import sys
from PyQt5.QtWidgets import QApplication
from translator_app import TranslatorApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    translator_app = TranslatorApp()
    translator_app.show()
    sys.exit(app.exec_())

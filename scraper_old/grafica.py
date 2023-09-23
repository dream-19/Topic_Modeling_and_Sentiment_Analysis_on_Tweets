from PyQt5 import QtWidgets as qtw
from GUI_ui import Ui_MainWindow


class Window(qtw.QMainWindow, Ui_MainWindow):

    def __init__(self, operator):
        super(Window, self).__init__()
        self.setupUi(self)
        self.scraper = operator

        self.pushButton.clicked.connect(self.click_pushButton)

    def click_pushButton(self):
        if self.lineEdit.text() and self.lineEdit_2.text():
            hashtag = self.lineEdit.text()
            nomefile = self.lineEdit_2.text()
            self.scraper.execution(hashtag, nomefile)
            end_message = qtw.QMessageBox(self)
            end_message.setText("Scraping completato")
            end_message.setWindowTitle("Concluso")
            end_message.exec()
        else:
            error_message = qtw.QMessageBox(self)
            error_message.setText("Compila tutti i campi")
            error_message.setWindowTitle("Errore")
            error_message.exec()

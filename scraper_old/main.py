import sys
from threading import Thread
from scraping import Scraper
from PyQt5.QtWidgets import QApplication
from grafica import Window



def main():
    operator = Scraper()
    app = QApplication(sys.argv)
    mainW = Window(operator)
    mainW.setWindowTitle("Ricerca tramite hashtag")
    mainW.show()

    t = Thread(name="console", target=operator.start, daemon=True)
    t.start()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

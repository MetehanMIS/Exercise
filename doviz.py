import sys
import requests
from bs4 import BeautifulSoup

from PyQt5.QtWidgets import QWidget,QApplication,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout,QComboBox,QLabel


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.doviz_label = QLabel("Döviz Türü:")
        self.comboBox = QComboBox()


        self.miktar_label = QLabel("Miktarı Giriniz: ")
        self.lineEdit = QLineEdit()

        self.button = QPushButton("Hesapla")
        self.sonuc_label =QLabel("Sonuç:"+71*" ")

        v_box = QVBoxLayout()

        self.html()
        v_box.addWidget(self.doviz_label)
        v_box.addWidget(self.comboBox)
        v_box.addStretch()
        v_box.addWidget(self.miktar_label)
        v_box.addWidget(self.lineEdit)
        v_box.addStretch()
        v_box.addWidget(self.button)
        v_box.addWidget(self.sonuc_label)
        v_box.addStretch()

        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.setWindowTitle("TL/Döviz Alış Fiyatı Hesaplama")
        self.button.clicked.connect(self.hesapla)

        self.show()


    def html(self):
        url = "https://canlidoviz.com/doviz-kurlari"
        response = requests.get(url)
        html_icerigi = response.content
        soup = BeautifulSoup(html_icerigi, "html.parser")

        self.birimler = []
        birim = soup.find_all("div", {"class": "highlight"})
        for i in birim:
            self.birimler.append((i.text).strip())
            self.comboBox.addItem((i.text).strip())

        self.degerler = []
        deger = soup.find_all("td", {"class": "text-primary text-right text-title"})
        for i in deger:
            self.degerler.append(float((i.text).strip()))

        zipped = zip(self.birimler, self.degerler)
        self.a_dict = dict(zipped)


    def hesapla(self):
        try:
            miktar = self.lineEdit.text()

            sonuc = round(float(miktar) / self.a_dict[self.comboBox.currentText()], 3)
            self.sonuc_label.setText("Sonuç "+ str(sonuc))
        except:
            self.sonuc_label.setText("Lütfen bir sayı giriniz. Ondalıklı ise nokta koyarak yazınız.")




app = QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())
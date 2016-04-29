
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import receteClass
import vpRecete

class recete_edit(QDialog,vpRecete.Ui_Dialog):

    def __init__(self):
        super(recete_edit, self).__init__()
        self.setupUi(self)
        self.lineEditBas.setValidator(QIntValidator(0,65564))
        self.lineEditSon.setValidator(QIntValidator(0,65564))
        self.btnEkle.clicked.connect(self.ekleItem)
        self.list1.itemClicked.connect(self.list1Index)
        self.btnSil.clicked.connect(self.silItem)
        self.n_recete=receteClass.color_list()
        self._dosyakayit=receteClass.dosyakayit()
        self.btnKayit.clicked.connect(self.kayit)
        self.btnAc.clicked.connect(self.oku)

    def ekleItem(self):
        self.n_recete.ekle(self.comboBox.currentText(),self.lineEditBas.text(),self.lineEditSon.text())
        self.tableWidget.setRowCount(len(self.n_recete.my_dict))
        self.list1.clear()
        for n in range(len(self.n_recete.my_dict)):
            a=str(self.n_recete.my_dict[n])
            self.list1.addItem(a)
        self.n_recete.yazdir()

    def list1Index(self):
        self.list1_Index=self.list1.currentRow()
        return self.list1_Index

    def silItem(self):
        self.n_recete.kaldir(self.list1_Index)
        self.list1.clear()
        for n in range(len(self.n_recete.my_dict)):
            a = str(self.n_recete.my_dict[n])
            self.list1.addItem(a)
        self.n_recete.yazdir()

    def kayit(self):
        _dosya=str(self.lineEdit_3.text())
        self._dosyakayit.kayit(self.n_recete.my_dict,_dosya)
    #dosya okuma kısmında kalındı

    def oku(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setNameFilter(self.tr('Text Files(*.txt)'))

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            self.lblDosya.setText(filenames[0])
            _myDict={}
            _myDict=self._dosyakayit.oku(filenames[0])
            self.list1.clear()
            print(filenames)
            print(_myDict)
            self.n_recete.setDict(_myDict)

            for n in range(len(_myDict)):
                a = str(_myDict[n])
                self.list1.addItem(a)



if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=recete_edit()
    form.show()

    sys.exit(app.exec_())


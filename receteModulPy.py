
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
import receteClass
import vpRecete
__appname__="Reçete Edit"

class recete_edit(QDialog,vpRecete.Ui_Dialog):

    def __init__(self):
        super(recete_edit, self).__init__()
        self.setupUi(self)
        self.validator=QDoubleValidator(0.05,1000.00,2)
        self.validator.setNotation(QDoubleValidator.StandardNotation)
        self.lineEditBas.setValidator(self.validator)
        self.lineEditSon.setValidator(self.validator)
        self.btnEkle.clicked.connect(self.ekleItem)
        self.list1.itemClicked.connect(self.list1Index)
        self.btnSil.clicked.connect(self.silItem)
        self.n_recete=receteClass.color_list()
        self._dosyakayit=receteClass.dosyakayit()
        self.btnKayit.clicked.connect(self.kayit)
        self.btnAc.clicked.connect(self.oku)
        self.btnRenk_1.clicked.connect(self.renkSec)
        self.btnRenk_2.clicked.connect(self.renkSec)
        self.btnRenk_3.clicked.connect(self.renkSec)
        self.btnRenk_4.clicked.connect(self.renkSec)
        self.btnRenk_5.clicked.connect(self.renkSec)
        self.btnRenk_6.clicked.connect(self.renkSec)
        self.btnRenk_7.clicked.connect(self.renkSec)
        self.btnRenk_8.clicked.connect(self.renkSec)
        self.prgBarRec.hide()

    def ekleItem(self):
        text=(self.lineEditBas.text(),self.lineEditSon.text())
        for text_it in text:
            isFloat=checkIsFloat(text_it,self.validator)
            a=isFloat.checkText()
            if a[0]==False:
                QMessageBox.warning(self,__appname__,a[1])
                return
            if float(text[0])>=float(text[1]):
                QMessageBox.warning(self, __appname__, "başlangıç bitişten büyük ya da eşit olamaz")
                return

        self.n_recete.ekle(self.comboBox.currentText(),self.lineEditBas.text(),self.lineEditSon.text())
        self.list1.clear()
        for n in range(len(self.n_recete.my_dict)):
            a=str(self.n_recete.my_dict[n])
            self.list1.addItem(a)
        self.n_recete.yazdir()

    def list1Index(self):
        list1_Index=self.list1.currentRow()
        print("index_list", list1_Index)
        return list1_Index

    def silItem(self):
        index=self.list1Index()
        print("index_list",index)
        if index<0 or index==None:
            QMessageBox.warning(self,__appname__,"Listede Silinecek Satır Yok")
        else:
            self.n_recete.kaldir(index)
            self.list1.clear()
            for n in range(len(self.n_recete.my_dict)):
                a = str(self.n_recete.my_dict[n])
                self.list1.addItem(a)
            self.n_recete.yazdir()

    def kayit(self):
        # dlg = QFileDialog()
        # dlg.setFileMode(QFileDialog.AnyFile)
        # dlg.setNameFilter(self.tr('Text Files(*.txt)'))

        _dosya=QFileDialog.getSaveFileName(self,"dosya adı")
        filename=_dosya[0]
        print(_dosya[0]+".txt")
        if filename=="":
            QMessageBox.warning(self,__appname__,"dosya adı boş bırakılamaz")
        else:
            self._dosyakayit.kayit(self.n_recete.my_dict,filename)
            self.lblDosya.setText(filename)
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


    def renkSec(self):
        btn=self.sender()
        cDial = QColorDialog.getColor()
        palet=QPalette()


        if btn.text()=="renk 1":
            print(cDial)
            palet = QPalette()
            role=QPalette.Button
            palet.setColor(role,QColor(cDial))
            palet.setBrush(role,QBrush(QColor(cDial), Qt.SolidPattern))
            self.btnRenk_1.setPalette(palet)
            self.btnRenk_1.setAutoFillBackground(True)

        elif btn.text()=="renk 2":
            print(cDial)
            role=QPalette.Button
            palet.setColor(role,QColor(cDial))
            self.btnRenk_2.setPalette(palet)
            self.btnRenk_2.setAutoFillBackground(True)

        print(btn.text())

class  checkIsFloat():
    def __init__(self,text,validator):
        self.text=text
        self.validator=validator


    def checkText(self):
        text=self.text
        state = self.validator.validate(self.text, 0)[0]
        if "," in text:
            return (False,"virgül yerine nokta kullanılmalı")
        elif state ==QValidator.Intermediate:
            return (False,"girilen sayı belirlenen aralıkta değil")
        else:
            return (True,"başarılı")





if __name__ == '__main__':
    app=QApplication(sys.argv)

    sys._excepthook = sys.excepthook
    def my_exception_hook(exctype, value, traceback):
        # Print the error and traceback
        print(exctype, value, traceback)
        # Call the normal Exception hook after
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)


    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook
    form=recete_edit()
    form.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")




# if __name__ == '__main__':
#     app=QApplication(sys.argv)
#     form=recete_edit()
#     form.show()
#
#     sys.exit(app.exec_())


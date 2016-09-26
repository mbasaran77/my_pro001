
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
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

    def ekleItem(self):
        text=(self.lineEditBas.text(),self.lineEditSon.text())
        for text_it in text:
            isFloat=checkIsFloat(text_it,self.validator)
            a=isFloat.checkText()
            if a[0]==False:
                QMessageBox.warning(self,__appname__,a[1])
                return


        self.n_recete.ekle(self.comboBox.currentText(),self.lineEditBas.text(),self.lineEditSon.text())
        self.tableWidget.setRowCount(len(self.n_recete.my_dict))
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
        _dosya=str(self.lineEdit_3.text())
        print(type(_dosya))
        if _dosya=="":
            QMessageBox.warning(self,__appname__,"dosya adı boş bırakılamaz")
        else:
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
    form=recete_edit()
    form.show()

    sys.exit(app.exec_())


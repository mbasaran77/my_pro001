
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
import receteClass
import vpRecete
from lineMdl import LineWidget
__appname__="Reçete Edit"

class recete_edit(QDialog,vpRecete.Ui_Dialog):

    def __init__(self):
        super(recete_edit, self).__init__()
        self.setupUi(self)
        self.validator=QDoubleValidator(0.00,1000.00,2)
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

        self.lineWidget=LineWidget()
        frameLayout=QHBoxLayout(self.frameColor)
        frameLayout.addWidget(self.lineWidget)


        self.btnYeniRecete.clicked.connect(self.yeniRecete)
        self.prgBarRec.hide()
        self.renkDict={}

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
        return list1_Index

    def silItem(self):
        index=self.list1Index()
        if index<0 or index==None:
            QMessageBox.warning(self,__appname__,"Listede Silinecek Satır Yok")
        else:
            self.n_recete.kaldir(index)
            self.list1.clear()
            for n in range(len(self.n_recete.my_dict)):
                a = str(self.n_recete.my_dict[n])
                self.list1.addItem(a)
            self.n_recete.yazdir()
    def yeniRecete(self):
        self.list1.clear()
        self.renkDict={}
        self.boyabtn(self.renkDict)
        self.n_recete.my_dict={}
        self.n_recete.setDict({})
        pass


    def kayit(self):
        # dlg = QFileDialog()
        # dlg.setFileMode(QFileDialog.AnyFile)
        # dlg.setNameFilter(self.tr('Text Files(*.txt)'))

        _dosya=QFileDialog.getSaveFileName(self,"dosya adı")
        filename=_dosya[0]
        if filename=="":
            QMessageBox.warning(self,__appname__,"dosya adı boş bırakılamaz")
        else:
            self._dosyakayit.kayit((self.n_recete.my_dict,self.renkDict),filename)
            self.lblDosya.setText(filename)
        #dosya okuma kısmında kalındı

    def oku(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setNameFilter(self.tr('Text Files(*.txt)'))

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            self.lblDosya.setText(filenames[0])
            _myTuple=()
            _myDict={}
            _myTuple=self._dosyakayit.oku(filenames[0])
            _myDict=_myTuple[0]
            self.list1.clear()
            self.n_recete.setDict(_myDict)
            self.renkDict=_myTuple[1]
            self.boyabtn(_myTuple[1])

            for n in range(len(_myDict)):
                a = str(_myDict[n])
                self.list1.addItem(a)


    def renkSec(self):
        btn=self.sender()
        cDial = QColorDialog.getColor()
        palet=QPalette()
        role = QPalette.Button
        palet.setColor(role, QColor(cDial))
        for btn_ in (self.btnRenk_1,self.btnRenk_2,self.btnRenk_3,self.btnRenk_4,self.btnRenk_5,self.btnRenk_6,
                    self.btnRenk_7,self.btnRenk_8):

            if btn_.text()==btn.text():
                self.renkDict[btn.text()]=QColor.getHsv(cDial)
                btn_.setPalette(palet)
                btn_.setAutoFillBackground(True)

    def boyabtn(self,dicR):

        palet=QPalette()
        role = QPalette.Button

        for btn_ in (self.btnRenk_1,self.btnRenk_2,self.btnRenk_3,self.btnRenk_4,self.btnRenk_5,self.btnRenk_6,
                    self.btnRenk_7,self.btnRenk_8):
            try:
                a0,a1,a2,a3=dicR[btn_.text()]
                colorHsv=QColor.fromHsv(a0,a1,a2,a3)
                palet.setColor(role, colorHsv)
                btn_.setPalette(palet)
                btn_.setAutoFillBackground(True)
            except KeyError:
                color=Qt.lightGray
                palet.setColor(role, color)
                btn_.setPalette(palet)
                btn_.setAutoFillBackground(True)
        self.desen()
    def desen(self):
        f_w=self.frameColor.width()
        maxL=self.findMaxLength()
        skala=f_w/maxL
        self.lineWidget.setLine(self.desenListeYap(skala))
        self.lineWidget.repaint()

    def findMaxLength(self):
        maxL=0
        for a in self.n_recete.my_dict:
            liste=self.n_recete.my_dict[a]
            x=float(liste[2])
            if x>=maxL:
                maxL=x
        return maxL

    def desenListeYap(self, xSkala):
        liste,altListe,gecList=[],[],[]
        offset=-5
        sozluk=self.n_recete.my_dict
        coord = {'renk 1': 5, 'renk 2': 15, 'renk 3': 25, 'renk 4': 35, 'renk 5': 45, 'renk 6': 55, 'renk 7': 65,
                 'renk 8': 75}
        color=self.renkDict
        for a in sozluk:
            gecList=sozluk[a]
            for renk in coord:
                if renk==gecList[0]:
                    try:
                        altListe.append(color[renk])
                        altListe.append(round(xSkala*float(gecList[1])))
                        altListe.append(coord[renk])
                        altListe.append(round(xSkala*float(gecList[2]))+offset)
                        altListe.append(coord[renk])
                        liste.append(altListe)
                        altListe=[]
                    except KeyError:
                        pass
        return liste

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


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\user\PycharmProjects\my_pro001\vpRecete.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(830, 485)
        self.btnYeniRecete = QtWidgets.QPushButton(Dialog)
        self.btnYeniRecete.setGeometry(QtCore.QRect(10, 20, 151, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnYeniRecete.sizePolicy().hasHeightForWidth())
        self.btnYeniRecete.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnYeniRecete.setFont(font)
        self.btnYeniRecete.setObjectName("btnYeniRecete")
        self.list1 = QtWidgets.QListWidget(Dialog)
        self.list1.setGeometry(QtCore.QRect(10, 160, 311, 311))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.list1.setFont(font)
        self.list1.setObjectName("list1")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 80, 151, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.btnAc = QtWidgets.QPushButton(Dialog)
        self.btnAc.setGeometry(QtCore.QRect(330, 21, 151, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAc.sizePolicy().hasHeightForWidth())
        self.btnAc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnAc.setFont(font)
        self.btnAc.setObjectName("btnAc")
        self.lblDosya = QtWidgets.QLabel(Dialog)
        self.lblDosya.setGeometry(QtCore.QRect(10, 140, 311, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDosya.sizePolicy().hasHeightForWidth())
        self.lblDosya.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblDosya.setFont(font)
        self.lblDosya.setObjectName("lblDosya")
        self.btnKayit = QtWidgets.QPushButton(Dialog)
        self.btnKayit.setGeometry(QtCore.QRect(170, 21, 151, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnKayit.sizePolicy().hasHeightForWidth())
        self.btnKayit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnKayit.setFont(font)
        self.btnKayit.setObjectName("btnKayit")
        self.lineEditSon = QtWidgets.QLineEdit(Dialog)
        self.lineEditSon.setGeometry(QtCore.QRect(330, 80, 151, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSon.sizePolicy().hasHeightForWidth())
        self.lineEditSon.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditSon.setFont(font)
        self.lineEditSon.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEditSon.setInputMask("")
        self.lineEditSon.setObjectName("lineEditSon")
        self.btnSil = QtWidgets.QPushButton(Dialog)
        self.btnSil.setGeometry(QtCore.QRect(650, 80, 151, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSil.sizePolicy().hasHeightForWidth())
        self.btnSil.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnSil.setFont(font)
        self.btnSil.setObjectName("btnSil")
        self.btnEkle = QtWidgets.QPushButton(Dialog)
        self.btnEkle.setGeometry(QtCore.QRect(490, 80, 151, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnEkle.sizePolicy().hasHeightForWidth())
        self.btnEkle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnEkle.setFont(font)
        self.btnEkle.setObjectName("btnEkle")
        self.lineEditBas = QtWidgets.QLineEdit(Dialog)
        self.lineEditBas.setGeometry(QtCore.QRect(170, 80, 151, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditBas.sizePolicy().hasHeightForWidth())
        self.lineEditBas.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditBas.setFont(font)
        self.lineEditBas.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineEditBas.setObjectName("lineEditBas")
        self.grpBoxColor = QtWidgets.QGroupBox(Dialog)
        self.grpBoxColor.setGeometry(QtCore.QRect(330, 150, 491, 89))
        self.grpBoxColor.setObjectName("grpBoxColor")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.grpBoxColor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnRenk_1 = QtWidgets.QPushButton(self.grpBoxColor)
        self.btnRenk_1.setFlat(True)
        self.btnRenk_1.setObjectName("btnRenk_1")
        self.horizontalLayout.addWidget(self.btnRenk_1)
        self.btnRenk_2 = QtWidgets.QPushButton(self.grpBoxColor)
        self.btnRenk_2.setFlat(True)
        self.btnRenk_2.setObjectName("btnRenk_2")
        self.horizontalLayout.addWidget(self.btnRenk_2)
        self.btnRenk_3 = QtWidgets.QPushButton(self.grpBoxColor)
        self.btnRenk_3.setFlat(True)
        self.btnRenk_3.setObjectName("btnRenk_3")
        self.horizontalLayout.addWidget(self.btnRenk_3)
        self.btnRenk_4 = QtWidgets.QPushButton(self.grpBoxColor)
        self.btnRenk_4.setFlat(True)
        self.btnRenk_4.setObjectName("btnRenk_4")
        self.horizontalLayout.addWidget(self.btnRenk_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnRenk_5 = QtWidgets.QPushButton(self.grpBoxColor)
        self.btnRenk_5.setFlat(True)
        self.btnRenk_5.setObjectName("btnRenk_5")
        self.horizontalLayout_2.addWidget(self.btnRenk_5)
        self.btnRenk_6 = QtWidgets.QPushButton(self.grpBoxColor)
        self.btnRenk_6.setFlat(True)
        self.btnRenk_6.setObjectName("btnRenk_6")
        self.horizontalLayout_2.addWidget(self.btnRenk_6)
        self.btnRenk_7 = QtWidgets.QPushButton(self.grpBoxColor)
        self.btnRenk_7.setFlat(True)
        self.btnRenk_7.setObjectName("btnRenk_7")
        self.horizontalLayout_2.addWidget(self.btnRenk_7)
        self.btnRenk_8 = QtWidgets.QPushButton(self.grpBoxColor)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.btnRenk_8.setFont(font)
        self.btnRenk_8.setFlat(True)
        self.btnRenk_8.setObjectName("btnRenk_8")
        self.horizontalLayout_2.addWidget(self.btnRenk_8)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.frameColor = QtWidgets.QFrame(Dialog)
        self.frameColor.setGeometry(QtCore.QRect(330, 240, 491, 80))
        self.frameColor.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frameColor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameColor.setObjectName("frameColor")
        self.lblMaksBaskiUz = QtWidgets.QLabel(Dialog)
        self.lblMaksBaskiUz.setGeometry(QtCore.QRect(510, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.lblMaksBaskiUz.setFont(font)
        self.lblMaksBaskiUz.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblMaksBaskiUz.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lblMaksBaskiUz.setLineWidth(2)
        self.lblMaksBaskiUz.setTextFormat(QtCore.Qt.RichText)
        self.lblMaksBaskiUz.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMaksBaskiUz.setWordWrap(False)
        self.lblMaksBaskiUz.setIndent(5)
        self.lblMaksBaskiUz.setObjectName("lblMaksBaskiUz")
        self.lineEditCalismaHiz = QtWidgets.QLineEdit(Dialog)
        self.lineEditCalismaHiz.setGeometry(QtCore.QRect(650, 20, 151, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditCalismaHiz.sizePolicy().hasHeightForWidth())
        self.lineEditCalismaHiz.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditCalismaHiz.setFont(font)
        self.lineEditCalismaHiz.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEditCalismaHiz.setInputMask("")
        self.lineEditCalismaHiz.setObjectName("lineEditCalismaHiz")
        self.tBtnRecipeSend = QtWidgets.QToolButton(Dialog)
        self.tBtnRecipeSend.setGeometry(QtCore.QRect(330, 340, 61, 31))
        self.tBtnRecipeSend.setObjectName("tBtnRecipeSend")
        self.prgBarRec = QtWidgets.QProgressBar(Dialog)
        self.prgBarRec.setGeometry(QtCore.QRect(330, 390, 491, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.prgBarRec.setFont(font)
        self.prgBarRec.setProperty("value", 0)
        self.prgBarRec.setObjectName("prgBarRec")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEditBas, self.lineEditSon)
        Dialog.setTabOrder(self.lineEditSon, self.btnEkle)
        Dialog.setTabOrder(self.btnEkle, self.btnSil)
        Dialog.setTabOrder(self.btnSil, self.btnKayit)
        Dialog.setTabOrder(self.btnKayit, self.list1)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Reçete"))
        self.btnYeniRecete.setText(_translate("Dialog", "Yeni Reçete"))
        self.comboBox.setItemText(0, _translate("Dialog", "renk 1"))
        self.comboBox.setItemText(1, _translate("Dialog", "renk 2"))
        self.comboBox.setItemText(2, _translate("Dialog", "renk 3"))
        self.comboBox.setItemText(3, _translate("Dialog", "renk 4"))
        self.comboBox.setItemText(4, _translate("Dialog", "renk 5"))
        self.comboBox.setItemText(5, _translate("Dialog", "renk 6"))
        self.comboBox.setItemText(6, _translate("Dialog", "renk 7"))
        self.comboBox.setItemText(7, _translate("Dialog", "renk 8"))
        self.btnAc.setText(_translate("Dialog", "Aç"))
        self.lblDosya.setText(_translate("Dialog", "TextLabel"))
        self.btnKayit.setText(_translate("Dialog", "Kayıt"))
        self.lineEditSon.setPlaceholderText(_translate("Dialog", "bitiş (m olarak)"))
        self.btnSil.setText(_translate("Dialog", "sil"))
        self.btnEkle.setText(_translate("Dialog", "ekle"))
        self.lineEditBas.setPlaceholderText(_translate("Dialog", "başlangıç (m olarak)"))
        self.grpBoxColor.setTitle(_translate("Dialog", "Renk Seçim"))
        self.btnRenk_1.setText(_translate("Dialog", "renk 1"))
        self.btnRenk_2.setText(_translate("Dialog", "renk 2"))
        self.btnRenk_3.setText(_translate("Dialog", "renk 3"))
        self.btnRenk_4.setText(_translate("Dialog", "renk 4"))
        self.btnRenk_5.setText(_translate("Dialog", "renk 5"))
        self.btnRenk_6.setText(_translate("Dialog", "renk 6"))
        self.btnRenk_7.setText(_translate("Dialog", "renk 7"))
        self.btnRenk_8.setText(_translate("Dialog", "renk 8"))
        self.lblMaksBaskiUz.setText(_translate("Dialog", "TextLabel"))
        self.lineEditCalismaHiz.setPlaceholderText(_translate("Dialog", "çalışma hızı m/dk"))
        self.tBtnRecipeSend.setText(_translate("Dialog", "..."))


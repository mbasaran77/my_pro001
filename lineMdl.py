

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QBrush, QPen,QColor
from PyQt5.QtCore import Qt


class LineWidget(QWidget):
    def __init__(self, parent=None):
        super(LineWidget, self).__init__(parent)
        self.resize(600, 400)
        self.color=Qt.black
        self.colorDemet=(Qt.green,Qt.red)
        self.x0=20
        self.y0=40
        self.x1=250
        self.y1=40
        self.demet=[]
        self.i=0
    def setLine(self,demet):
        self.demet = demet


    def setColor(self,color):
        self.color=color
    def paintEvent(self,e):
        painter = QPainter(self)
        #painter.setRenderHint(QPainter.Antialiasing, True)
        #painter.setPen(QPen(self.color, 6, Qt.SolidLine))
        #painter.setBrush(QBrush(Qt.green, Qt.SolidPattern))
        self.i+=1
        #print(self.i)
        for a in self.demet:
            c, self.x0,self.y0,self.x1,self.y1=a
            a0,a1,a2,a3=c
            color=QColor.fromHsv(a0,a1,a2,a3)
            painter.setPen(QPen(color, 5, Qt.SolidLine))
            painter.drawLine(self.x0,self.y0,self.x1,self.y1) #20, 40, 250, 40
            #print(self.x0,self.x1)
class Dialog(QDialog):
    global _demet, sozluk,color,coord
    color ={'renk 1':Qt.darkRed,'renk 2':Qt.black,'renk 3':Qt.blue,'renk 4':Qt.yellow,'renk 5':Qt.cyan,'renk 6':Qt.green,
            'renk 7':Qt.gray,'renk 8':Qt.magenta}
    _demet=((Qt.red,20, 40, 250, 40),(Qt.green,245,50, 300, 50))
    sozluk={0: ['renk 1', '0', '150'], 1: ['renk 2', '150', '200'], 2: ['renk 3', '200', '250'], 3: ['renk 4', '250', '450'],
            4: ['renk 5', '450', '670'], 5: ['renk 6', '670', '870'], 6: ['renk 7', '870', '960']}
    coord={'renk 1':5,'renk 2':15,'renk 3':25,'renk 4':35,'renk 5':45,'renk 6':55,'renk 7':65,'renk 8':75}

    def __init__(self):
        super(Dialog, self).__init__()
        self.btn=QPushButton("deneme")
        self.btn_1=QPushButton("deneme_1")
        self.wid=LineWidget()
        self.btn.clicked.connect(self.ciz)
        self.btn_1.clicked.connect(self.dene)

        self.lbl=QLabel("deneme")
        self.frame=QFrame()
        self.frame.setFrameShape(QFrame.StyledPanel)
        frameLay=QVBoxLayout(self.frame)
        frameLay.addWidget(self.wid)


        self.resize(600,400)
        layout=QGridLayout()
        layout.addWidget(self.btn,0,0)
        layout.addWidget(self.btn_1,0,2)
        layout.addWidget(self.lbl,0,1)

        layout_1=QVBoxLayout()
        layout_1.addLayout(layout)
        layout_1.addWidget(self.frame)

        self.setLayout(layout_1)


    def dene(self):
        f_w=self.frame.width()-50
        maxX=self.findMaxX()
        skala=f_w/maxX
        return self.desenListeYap(skala)

    def findMaxX(self):
        maxL=0.0
        for a in sozluk:
            liste=sozluk[a]
            x=float(liste[2])
            if x>=maxL:
                maxL=x
        return maxL
    def desenListeYap(self, xSkala):
        liste,altListe,gecList=[],[],[]
        offset=10
        for a in sozluk:
            gecList=sozluk[a]
            for renk in coord:
                if renk==gecList[0]:
                    altListe.append(color[renk])
                    altListe.append(round(xSkala*float(gecList[1]))+offset)
                    altListe.append(coord[renk])
                    altListe.append(round(xSkala*float(gecList[2]))+offset)
                    altListe.append(coord[renk])
                    liste.append(altListe)
                    altListe=[]
        print(liste)
        return liste
    def ciz(self):
        self.wid.setLine(self.dene())
        #self.wid.setColor(Qt.red)
        self.wid.repaint()
        self.lbl.setText("ciz çağrıldı")
        print("ciz")






def main():
    import sys
    app = QApplication(sys.argv)
    window = Dialog()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
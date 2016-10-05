



from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
myDict={'renk 4': (327, 136, 255, 255), 'renk 1': (64, 71, 255, 255), 'renk 3': (338, 127, 255, 255), 'renk 8': (240, 255, 127, 255), 'renk 7': (200, 255, 255, 255), 'renk 2': (28, 126, 255, 255), 'renk 5': (323, 250, 255, 255), 'renk 6': (139, 118, 255, 255)}
#myDict={'renk 2': <PyQt5.QtGui.QColor object at 0x030D2AF0>, 'renk 3': <PyQt5.QtGui.QColor object at 0x030D22F0>, 'renk 5': <PyQt5.QtGui.QColor object at 0x0310E730>, 'renk 7': <PyQt5.QtGui.QColor object at 0x0310E830>, 'renk 4': <PyQt5.QtGui.QColor object at 0x0310E6F0>, 'renk 8': <PyQt5.QtGui.QColor object at 0x0310E7F0>, 'renk 1': <PyQt5.QtGui.QColor object at 0x00F873B0>, 'renk 6': <PyQt5.QtGui.QColor object at 0x0310E770>}
class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.setWindowTitle("color dialog")
        self.setGeometry(300,200,600,400)

        btn=QPushButton("color select",self)
        btn.move(200,100)
        palet=QPalette()
        role=QPalette.Button

        color=QColor.fromHsv(327, 136, 255, 255)
        brush=QBrush(color,Qt.SolidPattern)
        palet.setBrush(role,brush)
        btn.setPalette(palet)
        btn.setFlat(True)
        btn.setAutoFillBackground(True)





        self.lbl=QLabel("renk",self)
        self.lbl.move(200,150)
        self.color=Qt.green
        btn.clicked.connect(self.colorDialog)

    def paintEvent(self,e):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(QPen(self.color, 6, Qt.SolidLine))
        painter.setBrush(QBrush(self.color, Qt.SolidPattern))
        line=QLineF(20.00,40.05,250.05,40.00)
        painter.drawLine(line) #20, 40, 250, 40
        rect=QRect(20,70,40,60)
        painter.drawRect(rect)


    def colorDialog(self):
        cDial=QColorDialog.getColor()
        print(type(cDial))
        print(QColor.getHsv(cDial))
        self.color=QColor(cDial)
        self.repaint()





if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=Form()
    form.show()
    sys.exit(app.exec_())



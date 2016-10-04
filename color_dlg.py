



from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.setWindowTitle("color dialog")
        self.setGeometry(300,200,600,400)

        btn=QPushButton("color select",self)
        btn.move(200,100)
        palet=QPalette()
        roll=10
        palet.setColor(roll,Qt.red)
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
        self.color=QColor(cDial)
        self.repaint()





if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=Form()
    form.show()
    sys.exit(app.exec_())



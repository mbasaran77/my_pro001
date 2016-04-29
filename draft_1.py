mydict={0: ['renk1', 0, 50], 1: ['renk2', 50, 80], 2: ['renk3', 80, 120], 3: ['renk4', 120, 180], 4: ['renk5', 180, 220], 5: ['renk6', 220, 350]}

from PyQt5.QtWidgets import *
import sys
class my_list(QListWidget):
    def __init__(self,list_data):
        super(my_list, self).__init__()
        self.resize(300,120)
        self._listdata=list_data
        self.itemClicked.connect(self.sil)
        self.ekle()
    def ekle(self):
        self.clear()
        for n in range(len(self._listdata)):
            a=str(self._listdata[n])
            self.addItem(a)
            print(a)
    def sil(self):
        pass

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=my_list(mydict)
    ex.show()

    sys.exit(app.exec_())
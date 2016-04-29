import pickle

class color_list(object):
    def __init__(self):
        self.my_dict={}
        self._id=0
        self._bas=0
        self._bit=0
        self._color="renk1"
        self.my_dict_r={}
    def setDict(self,sdict):
        self.my_dict=sdict
        self._id=len(self.my_dict)

    def ekle(self,color,bas,bit):
        self.my_dict[self._id]=[color,bas,bit]
        self._id+=1


    def kaldir(self, id):
        if len(self.my_dict)>=1:
            self._id -= 1
        self.my_dict.pop(id)

        a=0
        i=0
        c=len(self.my_dict)
        for i in range(len(self.my_dict)+1):
            try:
                self.my_dict_r[a]=self.my_dict[i]
                a+=1
            except KeyError:
                pass
        i=0
        a=0
        self.my_dict.clear()
        for i in range(len(self.my_dict_r)+1):
           try:
               self.my_dict[a]=self.my_dict_r[i]
               a+=1
           except KeyError:
                pass
        print("my_dic_r ",self.my_dict_r)
        self.my_dict_r.clear()


    def yazdir(self):
        print("maydict  ",self.my_dict)

    def recete(self):
        return self.my_dict



class dosyakayit(object):
    # def __init__(self,mydict):
    #     self.mydict=mydict

    def kayit(self,mydict,dosya):
        _mydict=mydict
        _dosya=str(dosya)+".txt"
        with open(_dosya,'wb') as fh:
            pickle.dump(_mydict, fh)

    def oku(self,dosya):
        _dosya=dosya
        with open(_dosya,'rb') as fh:
            oku_dict=pickle.load(fh)
            return oku_dict


# my_recipe=color_list()
# my_recipe.ekle("renk1",0,50)
# my_recipe.ekle("renk2",50,80)
# my_recipe.ekle("renk3",80,120)
# my_recipe.ekle("renk4",120,180)
# my_recipe.ekle("renk5",180,220)
# my_recipe.ekle("renk6",220,350)
# print("my_recipe")
# my_recipe.yazdir()
#
# #dosya kayıt
# my_dict=my_recipe.recete()
# fSave=dosyakayit(my_dict)
# #fSave.kayit()
# oku_dict=fSave.oku()
# print("dosyadan okunan")
# print("o_mydict",oku_dict)
#
if __name__ == '__main__':
    pass
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


mydict = {0: ['renk1', 0, 500], 1: ['renk2', 50, 80], 2: ['renk3', 80, 120], 3: ['renk4', 120, 180],
          4: ['renk5', 180, 220], 5: ['renk6', 220, 350],
          6: ['renk1', 500, 900], 7: ['renk2', 90, 110], 8: ['renk3', 134, 560], 9: ['renk4', 455, 567],
          10: ['renk5', 230, 420], 11: ['renk6', 304, 405], 11: ['renk1', 1000, 1200]}


class plc_recete(object):
    def __init__(self):
        self.x =0
        self.renk1 = []
        self.renk2 = []
        self.renk3 = []
        self.renk4 = []
        self.renk5 = []
        self.renk6 = []
        self.renk7 = []
        self.renk8 = []
        self.a = []
    def hazirla(self,mydict):
        self.x=len(mydict)
        for i in range(self.x):
            self.a = mydict[i]
            if 'renk1' in self.a:
                self.renk1.append(str(self.a[1]))
                self.renk1.append(str(self.a[2]))

            elif 'renk2' in self.a:
                self.renk2.append(str(self.a[1]))
                self.renk2.append(str(self.a[2]))
            elif 'renk3' in self.a:
                self.renk3.append(str(self.a[1]))
                self.renk3.append(str(self.a[2]))
            elif 'renk4' in self.a:
                self.renk4.append(str(self.a[1]))
                self.renk4.append(str(self.a[2]))
            elif 'renk5' in self.a:
                self.renk5.append(str(self.a[1]))
                self.renk5.append(str(self.a[2]))
            elif 'renk6' in self.a:
                self.renk6.append(str(self.a[1]))
                self.renk6.append(str(self.a[2]))
            elif 'renk7' in self.a:
                self.renk7.append(str(self.a[1]))
                self.renk7.append(str(self.a[2]))
            elif 'renk8' in self.a:
                self.renk8.append(str(self.a[1]))
                self.renk8.append(str(self.a[2]))
            del self.a
    def yaz(self):
        print("renk1", self.renk1)
        print("renk2", self.renk2)
        print("renk3", self.renk3)
        print("renk4", self.renk4)
        print("renk5", self.renk5)
        print("renk6", self.renk6)
        print("renk7", self.renk7)
        print("renk8", self.renk8)
    def get_arr(self):
        return self.renk1

renk1=['0','500','500','900','1000','1200']
class plc_data_w_hazirla(object):
    def __init__(self,arr, str_adres):
        self._arr=arr
        self.len_arr=0
        self._wdata="%01#WD"
        self._end_adres=0
        self.data_string=""
        self._str_adres=str_adres

    def set_dizi(self,s_dizi):
        s_dizi_len=len(s_dizi)
        s_dizi=s_dizi
        c_dizi=[]
        c_dizi.append(s_dizi_len)
        for i in range(s_dizi_len):
            c_dizi.append(s_dizi[i])
        print(c_dizi)
        return c_dizi

    def hex_convert(self,str_arr):
        a=''
        dizi=str_arr
        len_dizi=len(str_arr)
        for i in range(len_dizi):
            b,c_1,c_2='','',''
            b=((hex(int(dizi[i])))[2:]).upper()
            b=b.zfill(4)
            c_1=b[2:]
            c_2=b[:2]
            a=a+(c_1+c_2)
        return a

    def hazirla(self):
        a=int(self._str_adres[1:6])
        end=a+ self.len_arr
        self._end_adres="D"+(str(end)).zfill((6-len(str(end))))
        self._wdata=self._wdata+self._str_adres+self._end_adres+self.hex_convert(self.set_dizi(self._arr))
        return (self._wdata+self.bcc_calc(self._wdata)+chr(13)).encode()

    def bcc_calc(self,d_str):
        e = 0
        _d_str = d_str.encode()
        for i in _d_str:
            d = i
            e = d ^ e

        print("e:", e, " ", hex(e))
        #return (d_str + (hex(e)[2:]).upper() + chr(13)).encode()
        return ((hex(e)[2:]).upper())

class plc_data_r_hazirla(object):
    pass

my_plc_recete=plc_recete()
my_plc_recete.hazirla(mydict)
my_plc_recete.yaz()

data_w=plc_data_w_hazirla(my_plc_recete.get_arr(),"D00001")
print(data_w.hazirla())



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
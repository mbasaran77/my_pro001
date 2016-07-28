

renk1=['0','500','500','900','1000','1200','1200','1200','1200','1200','1200','1200','1200','1200','1200','1200','1200','1200','1200','1200','1200','1200','1200','1200','1200','1200','1200','1200','1200']
renk2=[1280,1813,9]

class w_plc_data_hazirla(object):
    def __init__(self,arr, str_adres):
        self._arr=arr
        self.len_arr=0
        self._wdata="%01#WD"
        self.data_string=""
        self._str_adres=str_adres

    def set_dizi(self, dizi):
        s_dizi = dizi
        s_dizi_len=len(s_dizi)
        c_dizi=[]
        c_dizi.append(s_dizi_len)
        for i in range(s_dizi_len):
            c_dizi.append(s_dizi[i])
        print(c_dizi)
        self.len_arr=len(c_dizi)
        return c_dizi
    def end_addres(self,str_adres,dizi_len):
        a = int(self._str_adres[1:6])
        end = a +(dizi_len-1)
        end_adres = str(end).zfill(5)
        return end_adres


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

    def hazirla(self,recipe=False):
        #recete gönderilirken recipe=true yapılacak bu da dizinin başına kaç r
        #olduğunu ekler  !!!!
        if recipe==True:
            a=self.set_dizi(self._arr)
        else:
            a=self._arr
        print(a,"aaa", len(a))
        self._wdata=self._wdata+self._str_adres+self.end_addres(self._str_adres,len(a))+self.hex_convert(a)
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

class r_plc_data_hazirla(w_plc_data_hazirla):
    def __init__(self,str_add,data_l):
        self._wdata="%01#RD"
        self._str_adres=str_add
        self._data_l=data_l
    def hazirla(self,recipe=False):
        self._wdata=self._wdata+self._str_adres+self.end_addres(self._str_adres,self._data_l)
        return (self._wdata+self.bcc_calc(self._wdata)+chr(13)).encode()


class read_data_from_byte:
    dict_hex = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                "9": 9, "A": 10, "B": 11, "c": 12, "D": 13, "E": 14, "F": 15}
    s = "0123456789ABCDEF"
    def __init__(self,arr):
        self.arr=arr

    def check_r_w(self):
        if self.arr[3]==36 and self.arr[4]==82:
            print("okuma başarılı")
            self.convertRead()
        if self.arr[3]==36 and self.arr[4]==87:
            print("yazma başarılı")


    def convertRead(self):
        a=len(self.arr)-3
        x=1
        deger=[]
        for i in range(6,a,4):
            c=chr(self.arr[i])
            if chr(self.arr[i]) in self.s:
                b_1 = self.dict_hex[chr(self.arr[i])]
                b_0 = self.dict_hex[chr(self.arr[i+1])]
                b_3 = self.dict_hex[chr(self.arr[i+2])]
                b_2 = self.dict_hex[chr(self.arr[i+3])]
                deger.append(b_0*pow(16,0)+b_1*pow(16,1)+b_2*pow(16,2)+b_3*pow(16,3))
                x+=1
        print("deger :", x, " ", deger)
        return deger
# r_p_data=r_plc_data_hazirla("D00001",20)
# print("okuma",r_p_data.hazirla(False))
#
#
# w_p_data=w_plc_data_hazirla(renk1,"D00001")
# print(w_p_data.hazirla(True))

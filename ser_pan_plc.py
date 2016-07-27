




import serial
import time



def ser_init(a):
    seri_port=serial.Serial()
    seri_port.BAUDRATES=9600
    seri_port.port='COM4'
    seri_port.BYTESIZES=8
    seri_port.parity='O'
    seri_port.stopbits=1
    seri_port.open()
    seri_port.is_open
    seri_port.write(a)
    time.sleep(1)
    out=""
    while seri_port.inWaiting() > 0:
        out += seri_port.read(1)

    print(out)
    seri_port.close()


mydict={0: ['renk1', 0, 50], 1: ['renk2', 50, 80], 2: ['renk3', 80, 120], 3: ['renk4', 120, 180], 4: ['renk5', 180, 220], 5: ['renk6', 220, 350],
        6: ['renk1', 500, 900],7: ['renk2', 90, 110], 8: ['renk3', 134, 560], 9: ['renk4', 455, 567], 10: ['renk5', 230, 420], 11: ['renk6', 304, 405]}

def hazirla(mydict):
    x=len(mydict)
    print(x)
    renk1=  []
    renk2 = []
    renk3 = []
    renk4 = []
    renk5 = []
    renk6 = []
    renk7 = []
    renk8 = []
    a=[]
    for i in range(x):
        a=mydict[i]
        if 'renk1' in a:
            renk1.append(str(a[1]))
            renk1.append(str(a[2]))

        elif 'renk2' in a:
            renk2.append(str(a[1]))
            renk2.append(str(a[2]))
        elif 'renk3' in a:
            renk3.append(str(a[1]))
            renk3.append(str(a[2]))
        elif 'renk4' in a:
            renk4.append(str(a[1]))
            renk4.append(str(a[2]))
        elif 'renk5' in a:
            renk5.append(str(a[1]))
            renk5.append(str(a[2]))
        elif 'renk6' in a:
            renk6.append(str(a[1]))
            renk6.append(str(a[2]))
        elif 'renk7' in a:
            renk7.append(str(a[1]))
            renk7.append(str(a[2]))
        elif 'renk8' in a:
            renk8.append(str(a[1]))
            renk8.append(str(a[2]))
        del a
    print("renk1", renk1)
    print("renk2", renk2)
    print("renk3", renk3)
    print("renk4", renk4)
    print("renk5", renk5)
    print("renk6", renk6)
    print("renk7", renk7)
    print("renk8", renk8)

oku_str="%01#RDD0010000107**\r"
oku_str_1="%01#RDD0020000002"
oku_str_2="%01#RDD0010000107"


def bcc_calc(d_str):
    e = 0
    _d_str=d_str.encode()
    for i in _d_str:
        d=i
        e=d^e
    print(chr(e))

    return ("%01#RDD0020000002"+str(e)+"\r").encode()
a=bcc_calc(oku_str_1)
print(a)
print(bcc_calc(oku_str_2))

ser_init(a)




#hazirla(mydict)
# my_decoded_str = str.decode(bytes)
# type(my_decoded_str) # insures its string





#hazirla(mydict)
# dizi=[1,10,400]
# a=str(dizi[1])
# d=str(dizi[2])
# b=repr(dizi[1])
# print(type(a))
# print(type(b))
# c=bytes(a,'utf-8')+bytes(d,'utf-8')
# print(c)




# mystring ="@00RD0000010057*"
#
# b = bytes(mystring, 'utf-8')
#
# print(b)


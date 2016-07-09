

from draft_3 import w_plc_data_hazirla
from draft_3 import r_plc_data_hazirla
import serial
import time





oku_str_1="%01#RDD0020000202"
oku_str_2="%01#RDD0000100020"


renk1=['0','500','500','900','1000','1200']
w_p_data = w_plc_data_hazirla(renk1, "D00001")
yazilacak=w_p_data.hazirla(True)
print("mdl :",yazilacak)

r_p_data=r_plc_data_hazirla("D00001",20)
okunacak=r_p_data.hazirla()

print("mdl :",okunacak)

def bcc_calc(d_str):
    e = 0
    _d_str=d_str.encode()
    for i in _d_str:
        d=i
        e=d^e

    print("e:",e," ", hex(e))

    return (d_str+(hex(e)[2:]).upper()+chr(13)).encode()
a=bcc_calc(oku_str_2)
# a=okunacak
a=yazilacak
print(a)


ser = serial.Serial(
    port='COM4',
    baudrate=115200,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)
print("seri port açık mı?",ser.isOpen())
ser.write(a)
print("gönderilen :",a)

time.sleep(0.05)
line = ser.readline()
print("alınan :",line)
ser.close()
x=0
for i in line:
    print(x," :",i)
    x+=1

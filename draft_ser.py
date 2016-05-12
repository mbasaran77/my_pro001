


import serial
import time





oku_str_1="%01#RDD0020000202"
oku_str_2="%01#RDD0362103640"


def bcc_calc(d_str):
    e = 0
    _d_str=d_str.encode()
    for i in _d_str:
        d=i
        e=d^e

    print("e:",e," ", hex(e))

    return (d_str+hex(e)[2:]+chr(13)).encode()
a=bcc_calc(oku_str_2)
print(a)


ser = serial.Serial(
    port='COM4',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
print("seri port açık mı?",ser.isOpen())
ser.write(a)
print("gönderilen :",a)

time.sleep(0.2)
line = ser.readline()
print("alınan :",line)
ser.close()



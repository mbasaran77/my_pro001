import serial


def ser_init():
    seri_port=serial.Serial()
    seri_port.BAUDRATES=19200
    seri_port.port='COM1'
    seri_port.BYTESIZES=8
    seri_port.parity='N'
    seri_port.stopbits=1
    seri_port.open()
    seri_port.is_open

mydict={0: ['renk1', 0, 50], 1: ['renk2', 50, 80], 2: ['renk3', 80, 120], 3: ['renk4', 120, 180], 4: ['renk5', 180, 220], 5: ['renk6', 220, 350],
        6: ['renk1', 500, 900]}

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
            renk1.append(a[1])
            renk1.append(a[2])

            mystr=str(a[1])
            print(mystr)

            b=bytes(mystr,'utf-8')
            print("renk1",renk1)

            #del a
        elif 'renk2' in a:
            renk2.append(a[1])
            renk2.append(a[2])
            print("renk2", renk2)

#hazirla(mydict)
dizi=[1,10,400]
a=str(dizi[1])
d=str(dizi[2])
b=repr(dizi[1])
print(type(a))
print(type(b))
c=bytes(a,'utf-8')+bytes(d,'utf-8')
print(c)

mystring ="@00RD0000010057*"

b = bytes(mystring, 'utf-8')

print(b)


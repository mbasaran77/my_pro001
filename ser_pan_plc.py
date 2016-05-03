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


mystring ="@00RD0000010057*"

b = bytes(mystring, 'utf-8')

print(b)


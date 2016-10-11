
from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils
import time

client_host = "192.168.250.2"
client_port = 502

c = ModbusClient()

c.host(client_host)
c.port(client_port)

if not c.is_open():
    if not c.open():
        print("unable to connect to " + client_host + ":" + str(client_port))


def int32_to_int8(n):
    mask = (1 << 16) - 1
    return [(n >> k) & mask for k in range(0, 32, 16)]


var_int = utils.encode_ieee(7.5)
print(var_int)
sonuc=int32_to_int8(var_int)
print(sonuc)
if c.is_open():
    # read 10 registers at address 0, store result in regs list
    print(var_int)
    c.write_single_register(0,5)
    c.write_multiple_registers(1,sonuc)

    regs = c.read_holding_registers(0,100)
    # if success display registers
    if regs:
        print("reg ad #0 to 9: " , regs)

    bits = c.read_discrete_inputs(0, 16)
    # if success display registers
    if bits:
        print("bit ad #0 to 9: " + str(bits))

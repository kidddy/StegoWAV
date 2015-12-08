#!/usr/bin/python3
from os.path import getsize


def toBits(bytestr):
    result = []
    for byte in bytestr:
        bits = bin(byte)[2:]
        for _ in range(8 - len(bits)):
            result.append(0)
        for bit in bits:
            result.append(int(bit))
    return result

def toBytes(bits):
    b = []
    i = len(bits)
    while i % 8 != 0:
        i += 1
        b.append(0)
    for e in bits:
        b.append(e)
    count = 8
    byte = 0
    result = []
    for bit in b:
        byte = byte * 2 + bit
        count -= 1
        if count == 0:
            result.append(byte)
            byte = 0
            count = 8
    return bytes(result)

def hideBit(byte, hbit, position=8):
    if (position < 1 and position > 8):
        raise Exception("Bad argument position. It should be in [1..8].")
    result = 0
    step = 1
    for bit in toBits(byte):
        if (step == position):
            result = result * 2 + hbit
            step += 1
            continue
        result = result * 2 + bit
        step += 1
    return bytes([result])

def bytesToInt(bytestr):
    result = 0
    for bit in toBits(bytestr):
        result = result * 2 + bit
    return result

def bytesToIntLE(bytestr):
    return bytesToInt(reversed(bytestr))

def intToBytes(num, count=0):
    n = bin(num)[2:]
    b = []
    for e in n:
        b.append(int(e))
    result = toBytes(b)
    if count == 0: return result
    if len(result) > count:
        raise Exception("Can't write {} in {} bytes.".format(num, count))
    while len(result) != count:
        result = b'\x00' + result
    return result

def intToBytesLE(num, count=0):
    return bytes(reversed(list(intToBytes(num, count))))



def main():
    pass

if __name__ == '__main__':
    main()

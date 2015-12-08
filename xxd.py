#!/usr/bin/python3


import sys
import byte_tools
from os.path import getsize


def xxd(bytestr):
    step = 0
    line = ''
    endian = ''
    for byte in bytestr:
        if byte in [_ for _ in range(32, 127)]:
            endian += chr(byte)
        else:
            endian += '.'
        byte = hex(byte)[2:]
        if len(byte) < 2:
            byte = '0' + byte
        line += byte + " "
        step += 1
        if step % 4 == 0:
            line += " "
    while len(line) < 52:
        line += ' '
    return line + "  " + endian

def getnum(num, size):
    shift = size // 16 + 1
    result = hex(num)[2:]
    while len(result) != len(str(shift)):
        result = "0" + result
    return result

def main():
    filename = sys.argv[1]
    num = 0
    size = getsize(filename)
    with open(filename, 'rb') as f:
        while size - f.tell() != 0:
            print('{}:     {}'.format(getnum(num, size), xxd(f.read(16))))
            num += 1


if __name__ == '__main__':
    main()

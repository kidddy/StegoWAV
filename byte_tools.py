#!/usr/bin/python3


def to_bits(byte_str):
    result = []
    for byte in byte_str:
        bits = bin(byte)[2:]
        for _ in range(8 - len(bits)):
            result.append(0)
        for bit in bits:
            result.append(int(bit))
    return result


def to_bytes(bits):
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


def invert(x, bin_num_length=None):
    bin_x = []
    while x != 0:
        bin_x.append(x % 2)
        x //= 2
    while not (bin_num_length is None or bin_num_length <= len(bin_x)):
        bin_x.append(0)
    res = 0
    for e in reversed(bin_x):
        res = res*2 + int(not e)
    return res


def hide_data(byte, data, bin_data_size=None):
    if bin_data_size is None:
        bin_data_size = len(bin(data)[2:])
    bin_byte_size = len(bin(byte)[2:])
    ones = invert(0, bin_data_size)
    byte |= ones
    ones = invert(0, bin_byte_size) - invert(0, bin_data_size)
    data |= ones

    return byte & data


def main():
    pass

if __name__ == '__main__':
    main()

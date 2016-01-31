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


def hide_bit(byte, hbit, position=8):
    if not (0 < position < 9):
        raise Exception("Bad argument position. It should be in [1..8].")
    result = 0
    step = 1
    for bit in to_bits(byte):
        if step == position:
            result = result * 2 + hbit
            step += 1
            continue
        result = result * 2 + bit
        step += 1
    return result


def bytes_to_int(byte_str):
    result = 0
    for bit in to_bits(byte_str):
        result = result * 2 + bit
    return result


def bytes_to_int_le(byte_str):
    return bytes_to_int(reversed(byte_str))


def int_to_bytes(num, count=0):
    n = bin(num)[2:]
    b = []
    for e in n:
        b.append(int(e))
    result = to_bytes(b)
    if count == 0: return result
    if len(result) > count:
        raise Exception("Can't write {} in {} bytes.".format(num, count))
    while len(result) != count:
        result = b'\x00' + result
    return result


def int_to_bytes_le(num, count=0):
    return bytes(reversed(list(int_to_bytes(num, count))))


def main():
    pass

if __name__ == '__main__':
    main()

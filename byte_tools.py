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


def hide_bit(byte, hide_bit, position=1):
    number_of_byte = 0
    for i in range(len(byte)):
        number_of_byte += byte[i] * 256**i

    if hide_bit == 1:
        number_of_byte |= 2**(position - 1)
    elif hide_bit == 0:
        number_of_byte &= 2**(len(byte)*8 + 1) - 1 - 2**(position-1)
    else:
        Exception("Bad hide_bit argument.")

    result = list()
    while number_of_byte != 0:
        result.append(number_of_byte % 256)
        number_of_byte //= 256
    return bytes(result).ljust(len(byte), b'\x00')


def main():
    pass

if __name__ == '__main__':
    main()

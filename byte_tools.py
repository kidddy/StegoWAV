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


def bytes_to_int(byte_line):
    result = 0
    for byte in reversed(byte_line):
        result = result*256 + byte
    return result


def int_to_bytes(num, bytes_len):
    result = []
    while num != 0:
        result.append(num % 256)
        num //= 256
    return bytes(reversed(bytes(reversed(result)).rjust(bytes_len, b'\00')))


def hide_data(byte, data_to_hide, bad_bits_num=None):
    if bad_bits_num is None:
        bad_bits_num = len(bin(data_to_hide)[2:])
    byte = bin(byte)[2:].rjust(8, '0')[:-bad_bits_num]
    data_to_hide = bin(data_to_hide)[2:].rjust(bad_bits_num, '0')
    return int(byte + data_to_hide, 2)


def reveal_data(byte, number_of_bad_bits):
    ones = invert(0, number_of_bad_bits)
    return byte & ones


def main():
    pass

if __name__ == '__main__':
    main()

#!/usr/bin/python3

import unittest
import byte_tools

class byte_tools_Test(unittest.TestCase):
    def test_toBits(self):
        b = b'\xff\x01'
        res = 0
        for bit in byte_tools.to_bits(b):
            res = res * 10 + bit
        self.assertEqual(1111111100000001, res)

    def test_toBytes(self):
        first = b'\xff\x01'
        b = bytes(byte_tools.to_bytes(byte_tools.to_bits(first)))
        self.assertEqual(first, b)

    def test_hideBit1(self):
        b = byte_tools.hideBit(b'\x00', 1)
        self.assertEqual(1, b)

    def test_hideBit2(self):
        b = byte_tools.hideBit(b'\x00', 0)
        self.assertEqual(0, b)

    def test_hideBit3(self):
        b = byte_tools.hideBit(b'\xfa', 1)
        self.assertEqual(251, b)

    def test_bytesToInt(self):
        self.assertEqual(511, byte_tools.bytes_to_int(b'\x01\xff'))

    def test_bytestoIntLE(self):
        self.assertEqual(511, byte_tools.bytes_to_int_le(b'\xff\x01'))

    def test_intToBytes1(self):
        b = byte_tools.int_to_bytes(20)
        self.assertEqual(b'\x14', b)

    def test_intToBytes2(self):
        b = byte_tools.int_to_bytes(256)
        self.assertEqual(b'\x01\x00', b)

    def test_intToBytes3(self):
        b = byte_tools.int_to_bytes(256, 3)
        self.assertEqual(b'\x00\x01\x00', b)

    def test_intToBytesLE(self):
        b = byte_tools.int_to_bytes_le(256, 3)
        self.assertEqual(b'\x00\x01\x00', b)



def main():
    unittest.main()


if __name__ == "__main__":
    main()

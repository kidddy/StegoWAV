#!/usr/bin/python3

import unittest
from bitIterator import BitIter

class BitIter_Test(unittest.TestCase):
    def test_toBits(self):
        b = b'\xff\x01'
        res = 0
        for bit in BitIter.toBits(b):
            res = res * 10 + bit
        self.assertEqual(1111111100000001, res)

    def test_toBytes(self):
        first = b'\xff\x01'
        b = bytes(BitIter.toBytes(BitIter.toBits(first)))
        self.assertEqual(first, b)

    def test_hideBit1(self):
        b = BitIter.hideBit(b'\x00', 1)
        self.assertEqual(b'\x01', b)

    def test_hideBit2(self):
        b = BitIter.hideBit(b'\x00', 0)
        self.assertEqual(b'\x00', b)

    def test_hideBit3(self):
        b = BitIter.hideBit(b'\xfa', 1)
        self.assertEqual(b'\xfb', b)

    def test_bytesToInt(self):
        self.assertEqual(511, BitIter.bytesToInt(b'\x01\xff'))

    def test_bytestoIntLE(self):
        self.assertEqual(511, BitIter.bytesToIntLE(b'\xff\x01'))

    def test_intToBytes1(self):
        b = BitIter.intToBytes(20)
        self.assertEqual(b'\x14', b)

    def test_intToBytes2(self):
        b = BitIter.intToBytes(256)
        self.assertEqual(b'\x01\x00', b)

    def test_intToBytes3(self):
        b = BitIter.intToBytes(256, 3)
        self.assertEqual(b'\x00\x01\x00', b)

    def test_intToBytesLE(self):
        b = BitIter.intToBytesLE(256, 3)
        self.assertEqual(b'\x00\x01\x00', b)



def main():
    unittest.main()


if __name__ == "__main__":
    main()

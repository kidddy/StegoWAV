#!/usr/bin/python3

import unittest
import byte_tools


class ByteToolsTest(unittest.TestCase):
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
        b = byte_tools.hide_bit(b'\x00', 1)
        self.assertEqual(b'\x01', b)

    def test_hideBit2(self):
        b = byte_tools.hide_bit(b'\x00', 0)
        self.assertEqual(b'\x00', b)

    def test_hideBit3(self):
        b = byte_tools.hide_bit(b'\xfa', 1)
        self.assertEqual(b'\xfb', b)


def main():
    unittest.main()


if __name__ == "__main__":
    main()

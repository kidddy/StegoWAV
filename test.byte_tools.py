#!/usr/bin/python3

import unittest
import byte_tools


class ByteToolsTest(unittest.TestCase):
    def test_to_bits(self):
        b = b'\xff\x01'
        res = 0
        for bit in byte_tools.to_bits(b):
            res = res * 10 + bit
        self.assertEqual(1111111100000001, res)

    def test_to_bytes(self):
        first = b'\xff\x01'
        b = bytes(byte_tools.to_bytes(byte_tools.to_bits(first)))
        self.assertEqual(first, b)

    def test_invert1(self):
        self.assertEqual(0, byte_tools.invert(1))

    def test_invert2(self):
        self.assertEqual(21, byte_tools.invert(42))

    def test_invert3(self):
        self.assertEqual(213, byte_tools.invert(42, 8))

    def test_hideBit1(self):
        b = byte_tools.hide_data(0, 1)
        self.assertEqual(1, b)

    def test_hideBit2(self):
        b = byte_tools.hide_data(0, 0)
        self.assertEqual(0, b)

    def test_hideBit3(self):
        b = byte_tools.hide_data(250, 1)
        self.assertEqual(251, b)

    def test_hideBit4(self):
        b = byte_tools.hide_data(567, 5)
        self.assertEqual(565, b)

    def test_hideBit5(self):
        b = byte_tools.hide_data(42, 2, 4)
        self.assertEqual(34, b)

    def test_reveal(self):
        byte = 234213
        hidden_data = 9
        number_of_bad_bits = 15
        bad_byte = byte_tools.hide_data(byte, hidden_data, number_of_bad_bits)
        released_data = byte_tools.reveal_data(bad_byte, number_of_bad_bits)
        self.assertEqual(hidden_data, released_data)

    def test_byte_to_int_and_back(self):
        b = b'abcd'
        n = byte_tools.bytes_to_int(b)
        self.assertEqual(b, byte_tools.int_to_bytes(n))


def main():
    unittest.main()


if __name__ == "__main__":
    main()

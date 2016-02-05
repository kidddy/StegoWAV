#!/usr/bin/python3

import unittest
from enumerator import Enumerator


a = [i for i in range(20)]
f = Enumerator(a)
b = b'\x00\x01\x02\xff'
fb = Enumerator(b)


class Enumerator_test(unittest.TestCase):
    def test_list1(self):
        self.assertEqual([0,1,2], f.read(3))
        self.assertEqual(3, f.tell())

    def test_list2(self):
        self.assertEqual([3, 4, 5], f.read(3))

    def test_list3(self):
        f.seek(2)
        self.assertEqual([2, 3, 4], f.read(3))

    def test_list4(self):
        self.assertEqual(20, f.get_size())

    def test_bytes(self):
        self.assertEqual(b, bytes(fb.read()))




def main():
    unittest.main()


if __name__ == "__main__":
    main()

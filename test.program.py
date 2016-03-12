#!/usr/bin/python3

import unittest
from program import Program
from wav_tools.wav_container import WavContainer
from wav_tools.wav_file import BadFileException


class ProgramTest(unittest.TestCase):
    def test_correct_container(self):
        p = Program('container_1.txt')
        p.hide("data.txt", 'output.wav', 2, 1)
        w = WavContainer('output.wav')
        self.assertTrue(True)

    def test_simple_work(self):
        p = WavContainer('container_1.wav')
        with open('data.txt', mode='rb') as f:
            data = f.read()
        p.hide(data)
        self.assertEqual(data, bytes(p.reveal()))

    def test_example_work(self):
        p = WavContainer('container_1.wav')
        with open('data.txt', mode='rb') as f:
            data = f.read()
        p.hide(data, 2, 4)
        self.assertEqual(data, bytes(p.reveal(2, 4)))

    def test_not_existed_file(self):
        with self.assertRaises(FileNotFoundError):
            p = Program('some_name')

    def test_not_wav(self):
        with self.assertRaises(BadFileException):
            p = Program('data.txt')


if __name__ == '__main__':
    unittest.main()

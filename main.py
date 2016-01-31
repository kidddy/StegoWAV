#!/usr/bin/python3

from program import Program
from WavContainer.wav_file import WavFile
import sys


def main():
    # p = Program(sys.argv[1:])
    # p.work()
    wav = WavFile(sys.argv[1])
    print(wav.get_info_text())


if __name__ == "__main__":
    main()

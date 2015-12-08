#!/usr/bin/python3

from WavContainer.wavEditor import WavFile
import sys


def main():
    w = WavFile(sys.argv[1])
    w.print_info()
    # s = []
    # for e in w.samples():
    #     s.append(e)
    # data = b''
    # for sample in reversed(s):
    #     for b in sample:
    #         data += bytes(b)
    # w.set_data(data)
    w.saveToDisk('output.wav')



if __name__ == "__main__":
    main()

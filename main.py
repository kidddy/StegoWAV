#!/usr/bin/python3

from WavContainer.wavFile import WavFile
from WavContainer.wavContainer import WavContainer
import sys


def main():
    w = WavContainer(sys.argv[1])
    w.print_info()
    # w.saveToDisk('output.wav')
    print(w.container_space())



if __name__ == "__main__":
    main()

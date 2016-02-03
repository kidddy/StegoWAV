#!/usr/bin/python3

from program import Program
from WavContainer.wav_file import WavFile
import sys


def main():
    # p = Program(sys.argv[1:])
    # p.work()
    wav = WavFile(sys.argv[1])
    print(wav.get_info_text())
    if len(sys.argv) >= 3:
        wav.save_to_disk(sys.argv[2])


if __name__ == "__main__":
    main()

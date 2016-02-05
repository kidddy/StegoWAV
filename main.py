#!/usr/bin/python3

from program import Program
from WavContainer.wav_container import WavContainer
import sys


def go(container, file_name):
    with open(file_name, mode="rb") as f:
        container.hide(f.read())


def main():
    # p = Program(sys.argv[1:])
    # p.work()
    wav = WavContainer(sys.argv[1])
    print(wav.get_info_text())
    print(wav.container_space())
    if len(sys.argv) == 3:
        wav.save_to_disk(sys.argv[2])
    elif len(sys.argv) == 4:
        go(wav, sys.argv[2])
        wav.save_to_disk(sys.argv[3])


if __name__ == "__main__":
    main()

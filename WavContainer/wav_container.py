#!/usr/bin/python3


from abstracts import AbstractContainer
from .wav_file import WavFile
import byte_tools
from struct import pack, unpack


class WavContainer(AbstractContainer, WavFile):
    def __init__(self, file_name):
        WavFile.__init__(self, file_name)

    def container_space(self, number_of_bad_bits=1):
        if not 0 < number_of_bad_bits < 9:
            raise Exception("Bad number of bad bits")
        return (
            self.chunks['data'].get_size() //
            self.chunks['fmt '].bits_per_sample //
            8 * number_of_bad_bits
        )

    def hide(self, bytes_data, number_of_bad_bits=1):
        if len(bytes_data) > self.container_space(number_of_bad_bits):
            raise Exception("Too much data to hide. {}: but max={}".format(
                len(bytes_data), self.container_space())
            )
        bytes_data = pack(">I", len(bytes_data)) + bytes_data
        sample_num = 0
        pos = 0
        data = 0
        for bit in byte_tools.to_bits(bytes_data):
            data = data * 2 + bit
            pos += 1
            if pos == number_of_bad_bits:
                self[sample_num] = bytes(byte_tools.hide_data(self[sample_num], data, pos))
                pos = 0
                sample_num += 1

    def _iter_hidden_bits(self, number_of_bad_bits=1):
        sample_num = 0
        while sample_num != self.container_space() // number_of_bad_bits:
            bits = byte_tools.to_bits(self[sample_num])
            for i in range(number_of_bad_bits):
                yield bits[-(i + 1)]

    def reveal(self, number_of_bad_bits=1):
        size = list()
        sample_num = 0
        while True:
            bits = byte_tools.to_bits(self[sample_num])
            for i in range(number_of_bad_bits):
                size.append(bits[-(i + 1)])
                if len(size) == 24:
                    break
            sample_num += 1
        size = unpack(">I", byte_tools.to_bytes(size))
        result = list()
        while len(result) != size:
            # TODO =)
        return byte_tools.to_bytes(result)


def main():
    pass

if __name__ == '__main__':
    main()

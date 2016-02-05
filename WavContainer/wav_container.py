#!/usr/bin/python3


from abstracts import AbstractContainer
from .wav_file import WavFile
import byte_tools


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
        pos = 0
        for bit in byte_tools.to_bits(bytes_data):
            self[pos] = bytes(byte_tools.hide_bit(self[pos], bit, position=1))
            pos += 1
            # TODO: number_of_bad_bits and reveal

    def reveal(self, num):
        result = []
        step = self.chunks['fmt '].bitsPerSample // 8
        pos = -2
        for i in range(num * 8):
            pos += step
            result.append(
                byte_tools.to_bits(self._byte_at_pos(pos))[7]
            )
        return byte_tools.to_bytes(result)


def main():
    pass

if __name__ == '__main__':
    main()

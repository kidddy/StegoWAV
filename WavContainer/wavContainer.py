#!/usr/bin/python3


from abstracts import AbstractContainer
from .wavFile import WavFile
import byte_tools


class WavContainer(AbstractContainer, WavFile):
    def __init__(self, file_name):
        WavFile.__init__(self, file_name)

    def container_space(self):
        return (
            self.chunks['data'].get_size() //
            self.chunks['fmt '].blockAlign //
            8
        )

    def _byte_at_pos(self, pos):
        return bytes([self.chunks['data'].data[pos]])

    def _set_byte_at_pos(self, byte, pos):
        self.chunks['data'].data[pos] = byte

    def hide(self, bytes_data):
        if len(bytes_data) > self.container_space():
            raise Exception("Too much data to hide.")
        step = self.chunks['fmt '].bitsPerSample // 8
        pos = -2
        for bit in byte_tools.to_bits(bytes_data):
            pos += step
            self._set_byte_at_pos(
                byte_tools.hide_bit(self._byte_at_pos(pos), bit, 8),
                pos
            )

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

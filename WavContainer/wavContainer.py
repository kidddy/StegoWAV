#!/usr/bin/python3


from abstracts import AbstractContainer
from .wavFile import WavFile
import byte_tools



class WavContainer(AbstractContainer, WavFile):
    def __init__(self, filename):
        WavFile.__init__(self, filename)

    def container_space(self):
        return (
            self.chunks['data'].get_size() //
            self.chunks['fmt '].blockAlign //
            8
        )

    def _byte_at_pos(self, pos):
        return(bytes([self.chunks['data'].data[pos]]))

    def _set_byte_at_pos(self, byte, pos):
        self.chunks['data'].data[pos] = byte


    def hide(self, bytes_data):
        step = self.chunks['fmt '].bitsPerSample // 8
        pos = -1
        for bit in byte_tools.toBits(bytes_data):
            pos += step
            self._set_byte_at_pos(
                byte_tools.hideBit(self._byte_at_pos(pos), bit),
                pos
            )

    def reveal(self, num):
        result = []
        step = self.chunks['fmt '].bitsPerSample // 8
        pos = -1
        for i in range(num):
            pos += step
            result.append(
                byte_tools.toBits(self._set_byte_at_pos(pos))[7]
            )
        return byte_tools.toBytes(result)



def main():
    pass

if __name__ == '__main__':
    main()

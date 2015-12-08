#!/usr/bin/python3

import byte_tools
from enumerator import Enumerator

def toInt(b):
    return byte_tools.bytesToIntLE(bytes(b))

toBytes = byte_tools.intToBytesLE


class AbstractChunk:
    def __init__(self, data):
        raise NotImplementedError("Need to rewrite method")

    def get_size(self):
        raise NotImplementedError("Need to rewrite method")

    def print_info(self):
        raise NotImplementedError("Need to rewrite method")

    def toBytes(self):
        raise NotImplementedError("Need to rewrite method")


class ChunkFMT(AbstractChunk):
    def __init__(self, data):
        f = Enumerator(data)
        self.format = toInt(f.read(2))
        self.numChannels = toInt(f.read(2))
        self.sampleRate = toInt(f.read(4))
        self.byteRate = toInt(f.read(4))
        self.blockAlign = toInt(f.read(2))
        self.bitsPerSample = toInt(f.read(2))
        self._hasExtra = False
        self.extraData = b''
        if f.get_size() > 16:
            extraBytesNum = toInt(f.read(2))
            if extraBytesNum > 0:
                self.extraData = f.read(extraBytesNum)

    def get_size(self):
        size = 16
        if self._hasExtra:
            size += len(self._extraData)
        return size

    def print_info(self):
        print('Chunk ID: "fmt "')
        print('Size: {}'.format(self.get_size()))
        print('    Compression code: {}'.format(self.format))
        print('    Number of channels: {}'.format(self.numChannels))
        print('    Sample rate: {}'.format(self.sampleRate))
        print('    Byte rate: {}'.format(self.byteRate))
        print('    Block align: {}'.format(self.blockAlign))
        print('    Significant bits per sample: {}'.format(self.bitsPerSample))
        if self._hasExtra:
            print('    Extra data: {}'.format(self.extraData))

    def toBytes(self):
        result = b''
        result += b'fmt '
        result += toBytes(self.get_size(), 4)
        result += toBytes(self.format, 2)
        result += toBytes(self.numChannels, 2)
        result += toBytes(self.sampleRate, 4)
        result += toBytes(self.byteRate, 4)
        result += toBytes(self.blockAlign, 2)
        result += toBytes(self.bitsPerSample, 2)
        return result
        #TODO Extra data doesn't write

    def __eq__(self, other):
        if not isinstance(other, ChunkFMT):
            return False
        return (
            self.format == other.format and
            self.numChannels == other.numChannels and
            self.sampleRate == other.sampleRate and
            self.byteRate == other.byteRate and
            self.blockAlign == other.blockAlign and
            self.bitsPerSample == other.bitsPerSample and
            self.extraData == other.extraData
        )


class ChunkDATA(AbstractChunk):
    def __init__(self, data):
        self.data = bytearray(data)

    def get_size(self):
        return len(self.data)

    def print_info(self):
        print('Chunk ID: "data"')
        print('Size: {}'.format(self.get_size()))

    def toBytes(self):
        result = b''
        result += b'data'
        result += toBytes(self.get_size(), 4)
        result += bytes(self.data)
        return result




class ChunkFACT(AbstractChunk):
    def __init__(self, data):
        self._data = data

    def get_size(self):
        return len(self._data)

    def print_info(self):
        print('Chunk ID: "fact"')
        print('Size: {}'.format(self.get_size()))

    def toBytes(self):
        result = b''
        result += b'fact'
        result += toBytes(self.get_size(), 4)
        result += self._data
        return result



CHUNK_HANDLERS = {}
CHUNK_HANDLERS['fmt '] = ChunkFMT
CHUNK_HANDLERS['data'] = ChunkDATA
CHUNK_HANDLERS['fact'] = ChunkFACT


def main():
    pass


if __name__ == "__main__":
    main()

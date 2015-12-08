#!/usr/bin/python3

from bitIterator import BitIter

def toInt(b):
    return BitIter.bytesToIntLE(bytes(b))

toBytes = BitIter.intToBytesLE


class Enumerator:
    def __init__(self, sequence):
        self._body = sequence
        self._iter = iter(self._body)
        self._pos = 0

    def seek(self, position):
        self._pos = position
        self._iter = iter(self._body)
        step = 0
        while step != self._pos:
            next(self._iter)
            step += 1

    def get_size(self):
        return len(self._body)

    def tell(self):
        return self._pos

    def read(self, num=-1):
        if num == -1:
            num = self.get_size() - self._pos
        step = 0
        result = []
        while step != num:
            result.append(next(self._iter))
            step += 1
        self._pos += num
        return result



class ChunkFMT:
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


class ChunkDATA:
    def __init__(self, data):
        self.data = Enumerator(data)

    def get_size(self):
        return self.data.get_size()

    def print_info(self):
        print('Chunk ID: "data"')
        print('Size: {}'.format(self.get_size()))

    def toBytes(self):
        result = b''
        result += b'data'
        result += toBytes(self.get_size(), 4)
        result += bytes(self.data.read())
        return result




class ChunkFACT:
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

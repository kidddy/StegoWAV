#!\usr\bin\python3

from bitIterator import BitIter
from .chunkHandlers import CHUNK_HANDLERS


class WavFile:
    def __init__(self, filename):
        self._name = filename
        self.chunks = {}
        self.undecodedData = {}
        self.undecodedData['Data'] = 'no undecodedData'
        self.undecodedData['Size'] = 0
        with open(self._name, mode='rb') as f:
            if f.read(4).decode('utf-8') != 'RIFF':
                raise Exception("Bad file: not RIFF")
            size = BitIter.bytesToIntLE(f.read(4))
            if f.read(4).decode('utf-8') != 'WAVE':
                raise Exception("Bad file: not WAVE")
            self._read_chunks(f, size - 4)

    def _read_chunks(self, f, size):
        pos = 0
        while pos != size:
            chunkName = f.read(4).decode('utf-8')
            chunkSize = BitIter.bytesToIntLE(f.read(4))
            if (chunkName not in CHUNK_HANDLERS) or (chunkSize == 0):
                self.undecodedData['Size'] = size - pos
                self.undecodedData['Data'] = f.read(size - pos)
                pos += self.undecodedData['Size']
                continue
            self.chunks[chunkName] = CHUNK_HANDLERS[chunkName](f.read(chunkSize))
            pos += chunkSize + 8

    def get_size(self):
        size = 12
        for chunk in self.chunks:
            size += self.chunks[chunk].get_size() + 8
        return size

    def print_info(self):
        print("File: " + self._name)
        print("Size: {}".format(self.get_size()))
        for chunk in self.chunks:
            self.chunks[chunk].print_info()

    def print_unknown(self):
        print(self.undecodedData['Data'])

    def saveToDisk(self, name):
        with open(name, 'wb') as f:
            f.write(b'RIFF')
            f.write(BitIter.intToBytesLE(self.get_size() - 8, 4))
            f.write(b'WAVE')
            f.write(self.chunks['fmt '].toBytes())
            f.write(self.chunks['fact'].toBytes())
            f.write(self.chunks['data'].toBytes())

    def samples(self):
        size = self.chunks['data'].get_size()
        pos = 0
        blockAlign = self.chunks['fmt '].blockAlign
        numChannels = self.chunks['fmt '].numChannels
        bytePerSample = self.chunks['fmt '].bitsPerSample // 8
        while pos != size:
            result = []
            for _ in range(numChannels):
                result.append(bytes(self.chunks['data'].data.read(bytePerSample)))
            yield result
            pos += blockAlign

    def set_data(self, data):
        self.chunks['data'] = CHUNK_HANDLERS['data'](data)

    def container_space(self):
        return (
            self.chunks['data'].get_size() //
            self.chunks['fmt '].blockAlign *
            self.chunks['fmt '].numChannels // 8
            )   

def main():
    pass


if __name__ == '__main__':
    main()

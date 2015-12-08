#!\usr\bin\python3

import byte_tools
from .chunkHandlers import CHUNK_HANDLERS
from abstracts import AbstractFile


class WavFile(AbstractFile):
    def __init__(self, filename):
        self._name = filename
        self.chunks = {}
        self.undecodedData = {}
        self.undecodedData['Data'] = 'no undecodedData'
        self.undecodedData['Size'] = 0
        with open(self._name, mode='rb') as f:
            if f.read(4).decode('utf-8') != 'RIFF':
                raise Exception("Bad file: not RIFF")
            size = byte_tools.bytesToIntLE(f.read(4))
            if f.read(4).decode('utf-8') != 'WAVE':
                raise Exception("Bad file: not WAVE")
            self._read_chunks(f, size - 4)

    def _read_chunks(self, f, size):
        pos = 0
        while pos != size:
            chunkName = f.read(4).decode('utf-8')
            chunkSize = byte_tools.bytesToIntLE(f.read(4))
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
            f.write(byte_tools.intToBytesLE(self.get_size() - 8, 4))
            f.write(b'WAVE')
            f.write(self.chunks['fmt '].toBytes())
            f.write(self.chunks['fact'].toBytes())
            f.write(self.chunks['data'].toBytes())


def main():
    pass


if __name__ == '__main__':
    main()

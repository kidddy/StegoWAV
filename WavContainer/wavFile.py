#!\usr\bin\python3

import byte_tools
from .chunkHandlers import CHUNK_HANDLERS
from abstracts import AbstractFile


class WavFile(AbstractFile):
    def __init__(self, file_name):
        self._name = file_name
        self.chunks = {}
        self.undecoded_data = dict()
        self.undecoded_data['Data'] = 'no undecoded data'
        self.undecoded_data['Size'] = 0
        with open(self._name, mode='rb') as f:
            if f.read(4).decode('utf-8') != 'RIFF':
                raise Exception("Bad file: not RIFF")
            size = byte_tools.bytes_to_int_le(f.read(4))
            if f.read(4).decode('utf-8') != 'WAVE':
                raise Exception("Bad file: not WAVE")
            self._read_chunks(f, size - 4)

    def _read_chunks(self, f, size):
        pos = 0
        while pos != size:
            chunk_name = f.read(4).decode('utf-8')
            chunk_size = byte_tools.bytes_to_int_le(f.read(4))
            if (chunk_name not in CHUNK_HANDLERS) or (chunk_size == 0):
                self.undecoded_data['Size'] = size - pos
                self.undecoded_data['Data'] = f.read(size - pos)
                pos += self.undecoded_data['Size']
                continue
            self.chunks[chunk_name] = CHUNK_HANDLERS[chunk_name](f.read(chunk_size))
            pos += chunk_size + 8

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
        print(self.undecoded_data['Data'])

    def save_to_disk(self, name):
        with open(name, 'wb') as f:
            f.write(b'RIFF')
            f.write(byte_tools.int_to_bytes_le(self.get_size() - 8, 4))
            f.write(b'WAVE')
            f.write(self.chunks['fmt '].toBytes())
            f.write(self.chunks['fact'].toBytes())
            f.write(self.chunks['data'].toBytes())


def main():
    pass


if __name__ == '__main__':
    main()

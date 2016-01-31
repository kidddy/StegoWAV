#!\usr\bin\python3

from .chunk_handlers import CHUNK_HANDLERS
from abstracts import AbstractFile
from collections import OrderedDict
from struct import pack, unpack


class WavFile(AbstractFile):
    def __init__(self, file_name):
        self._name = file_name
        self.chunks = OrderedDict()
        with open(self._name, mode='rb') as f:
            if f.read(4).decode('utf-8') != 'RIFF':
                raise Exception("Bad file: not RIFF")
            size = unpack("<I", f.read(4))[0]
            if f.read(4).decode('utf-8') != 'WAVE':
                raise Exception("Bad file: not WAVE")
            self._read_chunks(f, size - 4)

    def _read_chunks(self, f, size):
        pos = 0
        while pos != size:
            chunk_name = f.read(4).decode('utf-8')
            chunk_size = unpack("<I", f.read(4))[0]
            if chunk_size == 0:
                raise Exception('Null chunk')
            if chunk_name not in CHUNK_HANDLERS:
                self.chunks[chunk_name] = CHUNK_HANDLERS["def "](f, chunk_size, chunk_name)
                pos += chunk_size + 8
                continue
            self.chunks[chunk_name] = CHUNK_HANDLERS[chunk_name](f, chunk_size)
            pos += chunk_size + 8

    def get_size(self):
        size = 12
        for chunk in self.chunks:
            size += self.chunks[chunk].get_size() + 8
        return size

    def get_info_text(self):
        info = ("File: " + self._name + "\n" +
                "Size: {}".format(self.get_size()))
        for chunk_name in self.chunks:
            info += "\n" + self.chunks[chunk_name].get_info_text()
        return info

    def save_to_disk(self, name):
        with open(name, 'wb') as f:
            f.write(b'RIFF')
            f.write(pack("<I", self.get_size() - 8))
            f.write(b'WAVE')
            for chunk_name in self.chunks:
                f.write(self.chunks[chunk_name].to_bytes())


def main():
    pass


if __name__ == '__main__':
    main()

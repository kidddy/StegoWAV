#!/usr/bin/python3

from abc import ABCMeta, abstractmethod
from struct import pack, unpack


class AbstractChunk(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, f, size):
        raise NotImplementedError("Need to rewrite method")

    @abstractmethod
    def get_size(self):
        raise NotImplementedError("Need to rewrite method")

    @abstractmethod
    def get_info_text(self):
        raise NotImplementedError("Need to rewrite method")

    @abstractmethod
    def to_bytes(self):
        raise NotImplementedError("Need to rewrite method")


class ChunkFMT(AbstractChunk):
    def __init__(self, f, size):
        (
            self.format,
            self.num_channels,
            self.sample_rate,
            self.byte_rate,
            self.block_align,
            self.bits_per_sample
        ) = unpack("<HHIIHH", f.read(16))
        self._has_extra = False
        self.extra_data = b''
        if size > 16:
            extra_bytes_num = unpack("<H", f.read(2))
            if extra_bytes_num > 0:
                self.extra_data = f.read(extra_bytes_num)

    def get_size(self):
        size = 16
        if self._has_extra:
            size += len(self.extra_data)
        return size

    def get_info_text(self):
        info = (
            'Chunk ID: "fmt "\n' +
            'Size: {}\n'.format(self.get_size()) +
            '    Compression code: {}\n'.format(self.format) +
            '    Number of channels: {}\n'.format(self.num_channels) +
            '    Sample rate: {}\n'.format(self.sample_rate) +
            '    Byte rate: {}\n'.format(self.byte_rate) +
            '    Block align: {}\n'.format(self.block_align) +
            '    Significant bits per sample: {}'.format(self.bits_per_sample)
        )
        if self._has_extra:
            info += '\n    Extra data: {}'.format(self.extra_data)
        return info

    def to_bytes(self):
        result = b'fmt '
        result += pack("<IHHIIHH",
                       self.get_size(),
                       self.format,
                       self.num_channels,
                       self.sample_rate,
                       self.byte_rate,
                       self.block_align,
                       self.bits_per_sample)
        if self._has_extra:
            result += pack("<H", len(self.extra_data))
            result += self.extra_data
        return result

    def __eq__(self, other):
        if not isinstance(other, ChunkFMT):
            return False
        return (
            self.format == other.format and
            self.num_channels == other.num_channels and
            self.sample_rate == other.sample_rate and
            self.byte_rate == other.byte_rate and
            self.block_align == other.block_align and
            self.bits_per_sample == other.bits_per_sample and
            self.extra_data == other.extra_data
        )


class ChunkDATA(AbstractChunk):
    def __init__(self, f, size):
        self._data = bytearray(f.read(size))

    def get_size(self):
        return len(self._data)

    def get_info_text(self):
        result = ('Chunk ID: data\n' +
                  'Size: {}'.format(self.get_size()))
        return result

    def to_bytes(self):
        result = b'data'
        result += pack("<I", self.get_size())
        result += self._data
        return result


class DefaultChunk(AbstractChunk):
    def __init__(self, f, size, name="def "):
        self._name = name
        self._data = f.read(size)

    def get_size(self):
        return len(self._data)

    def get_info_text(self):
        return ('Chunk ID: {}\n'.format(self._name) +
                'Size: {}'.format(self.get_size()))

    def to_bytes(self):
        result = bytes(self._name, "utf-8")
        result += pack("<I", self.get_size())
        result += self._data
        return result


CHUNK_HANDLERS = dict()
CHUNK_HANDLERS['fmt '] = ChunkFMT
CHUNK_HANDLERS['data'] = ChunkDATA
CHUNK_HANDLERS['def '] = DefaultChunk


def main():
    pass


if __name__ == "__main__":
    main()

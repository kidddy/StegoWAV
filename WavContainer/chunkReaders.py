#!/usr/bin/python3

from bitIterator import BitIter
toInt = BitIter.bytesToIntLE


def fmt(f, size):
    chunkData = {}
    chunkData['Chunk ID'] = 'fmt '
    chunkData['Chunk Size'] = size
    chunkData['Compression code'] = toInt(f.read(2))
    chunkData['Number of channels'] = toInt(f.read(2))
    chunkData['Sample rate'] = toInt(f.read(4))
    chunkData['Byte rate'] = toInt(f.read(4))
    chunkData['Block align'] = toInt(f.read(2))
    chunkData['Significant bits per sample'] = toInt(f.read(2))
    if size > 16:
        chunkData['Extra format bytes'] = toInt(f.read(2))
        chunkData['Extra data'] = f.read(chunkData['Extra format bytes'])
        return chunkData
    chunkData['Extra format bytes'] = 0
    chunkData['Extra data'] = b''
    return chunkData


def data(f, size):
    chunkData = {}
    chunkData['Chunk Size'] = size
    chunkData['Sample data'] = f.read(size)
    return chunkData


def fact(f, size):
    chunkData = {}
    chunkData['Chunk Size'] = size
    chunkData['Format Dependant Data'] = f.read(size)
    return chunkData

def default(f, size):
    chunkData = {}
    chunkData['Chunk Size'] = size
    chunkData['Chunk Data'] = f.read(size)



CHUNK_READERS = {}
CHUNK_READERS['default'] = default
CHUNK_READERS['fmt '] = fmt
CHUNK_READERS['data'] = data
CHUNK_READERS['fact'] = fact



def main():
    pass


if __name__ == '__main__':
    main()

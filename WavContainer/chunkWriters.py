#!/usr/bin/python3

from bitIterator import BitIter


def fmt(f, chunk):
    f.write(b'fmt ')
    f.write(BitIter.intToBytesLE(chunk['Chunk Size'], 4))
    f.write(BitIter.intToBytesLE(chunk['Compression code'], 2))
    f.write(BitIter.intToBytesLE(chunk['Number of channels'], 2))
    f.write(BitIter.intToBytesLE(chunk['Sample rate'], 4))
    f.write(BitIter.intToBytesLE(chunk['Byte rate'], 4))
    f.write(BitIter.intToBytesLE(chunk['Block align'], 2))
    f.write(BitIter.intToBytesLE(chunk['Significant bits per sample'], 2))
    if chunk['Extra format bytes'] != 0:
        f.write(BitIter.intToBytesLE(chunk['Extra format bytes'], 2))
        f.write(chunk['Extra data'])
        
def data(f, chunk):
    f.write(b'data')
    f.write(BitIter.intToBytesLE(chunk['Chunk Size'], 4))
    f.write(chunk['Sample data'])
    
    
CHUNK_WRITERS = {}
CHUNK_WRITERS['fmt '] = fmt
CHUNK_WRITERS['data'] = data




def main():
    pass


if __name__ == '__main__':
    main()

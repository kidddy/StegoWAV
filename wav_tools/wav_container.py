from abstracts import AbstractContainer
from .wav_file import WavFile
import byte_tools
from struct import pack, unpack
from orders import ORDER_INSPECTORS


class WavContainer(AbstractContainer, WavFile):
    def __init__(self, file_name):
        WavFile.__init__(self, file_name)

    def container_space(self, number_of_bad_bits=1):
        if not 0 < number_of_bad_bits < 9:
            raise ValueError("Bad number of bad bits")
        return (
            self.chunks['data'].get_size() //
            self.chunks['fmt '].bits_per_sample //
            8 * number_of_bad_bits
        )

    def hide(self, bin_data, order_num=0, bad_bits_num=1):
        bin_data = pack(">L", len(bin_data)) + bin_data
        if len(bin_data) > self.container_space(bad_bits_num):
            raise ContainerException("Too much data to hide. {}: but max={}".format(
                len(bin_data), self.container_space())
            )
        order_inspector = ORDER_INSPECTORS[order_num](self.container_space())
        sample_id = 0
        pos = 0
        hidden_data_byte = 0
        bits_data = byte_tools.to_bits(bin_data)
        for i in range(len(bits_data)):
            hidden_data_byte = hidden_data_byte * 2 + bits_data[i]
            pos += 1
            if (pos == bad_bits_num) or (i + 1 == len(bits_data)):
                if i + 1 == len(bits_data) and not (pos == bad_bits_num):
                    while pos != bad_bits_num:
                        hidden_data_byte *= 2
                        pos += 1
                self[sample_id] = byte_tools.hide_data(self[sample_id], hidden_data_byte, bad_bits_num)
                pos = 0
                hidden_data_byte = 0
                sample_id = order_inspector.next()

    def _iter_hidden_bits(self, order_num, number_of_bad_bits=1):
        sample_num = 0
        sample_id = 0
        order_inspector = ORDER_INSPECTORS[order_num](self.container_space())
        while sample_num != self.container_space():
            bits = byte_tools.reveal_data(self[sample_id], number_of_bad_bits)
            for pos in bin(bits)[2:].rjust(number_of_bad_bits, '0'):
                yield int(pos)
            sample_num += 1
            sample_id = order_inspector.next()

    def reveal(self, order_num=0, bad_bits_num=1):
        size = list()
        bits_iterator = iter(self._iter_hidden_bits(order_num, bad_bits_num))
        for bit in bits_iterator:
            size.append(bit)
            if len(size) == 32:
                break
        size = unpack(">L", byte_tools.to_bytes(size))[0] * 8
        current_pos = 0
        result = list()
        for bit in bits_iterator:
            result.append(bit)
            current_pos += 1
            if len(result) == 8:
                yield byte_tools.to_bytes(result)[0]
                result.clear()
            if current_pos == size:
                break
        if result:
            yield byte_tools.to_bytes(result)[0]


class ContainerException(Exception):
    def __init__(self, *args, **kwargs):
        pass


def main():
    pass

if __name__ == '__main__':
    main()

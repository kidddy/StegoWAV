#!/usr/bin/python3


from wav_tools.wav_container import WavContainer
from argparse import ArgumentParser
from xxd import Dumper
from sys import argv, exit


def init_argparser():
    parser = ArgumentParser(prog="python3 program.py", epilog="by kidddy!")
    sub_parsers = parser.add_subparsers(help="modes of program")

    hide_parser = sub_parsers.add_parser('hide', help="Hides datafile in the file-container")
    hide_parser.add_argument('file-container', action="store", help="This is file-container name")
    hide_parser.add_argument('data_file', action='store', help="This is datafile name")
    hide_parser.add_argument('output_file', action='store', help="Name of a output file.")

    reveal_parser = sub_parsers.add_parser('reveal', help="Reveals hidden data from the file-container")
    reveal_parser.add_argument('file-container', action="store", help="This is file-container name")
    reveal_parser.add_argument('output_file', action='store', help="Name of a output file.")

    check_parser = sub_parsers.add_parser('check', help="Steganalysis")
    check_parser.add_argument('file-container', action="store", help="This is file-container name")
    check_parser.add_argument('--hex_table', action="store_true", help="Prints hex table of hidden data.")

    parser.add_argument(
        '-b', '--bad_bits_number',
        action="store",
        default=1,
        type=int,
        help="Number of how many bits in every byte will be replaced")
    parser.add_argument(
        '-o', '--ordering_type',
        action="store",
        default=0,
        type=int,
        help="Thing which will be used for ordering bytes")
    return parser


class Program:
    def __init__(self, source_filename):
        self._container = WavContainer(source_filename)

    def hide(self, data, output_file, bad_bits_num=1, order_num=0):
        with open(data, mode='rb') as f:
            bin_data = f.read()
        self._container.hide(bin_data, order_num, bad_bits_num)
        self._container.save_to_disk(output_file)

    def reveal(self, output_file, bad_bits_num=1, order_num=0):
        with open(output_file, mode="wb") as f:
            f.write(bytes(self._container.reveal(order_num, bad_bits_num)))

    def dump_hidden_data(self, bad_bits_num=1, order_num=0):
        try:
            dumper = Dumper()
            for line in dumper(self._container.reveal(order_num, bad_bits_num)):
                print(line)
        except BrokenPipeError:
            pass


def main():
    parser = init_argparser()
    args = vars(parser.parse_args(argv[1:]))
    program = Program(args['file-container'])
    if 'data_file' in args:  # HIDE
        program.hide(
            args['data_file'],
            args['output_file'],
            args['bad_bits_number'],
            args['ordering_type']
        )
    elif 'output_file' in args:  # REVEAL
        program.reveal(
            args['output_file'],
            args['bad_bits_number'],
            args['ordering_type']
        )
    else:  # CHECK
        if args['hex_table']:
            program.dump_hidden_data(
                args['bad_bits_number'],
                args['ordering_type']
            )
        else:
            print(program._container.get_info_text())

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)

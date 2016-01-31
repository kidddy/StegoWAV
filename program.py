#!/usr/bin/python3


from WavContainer.wavContainer import WavContainer


class Program:

    mode = dict()
    mode['default'] = 0
    mode['--hide'] = 1
    mode['--reveal'] = 2
    mode['--help'] = 3

    def __init__(self, args):
        self._mode = Program.mode['default']
        if args[0] not in Program.mode:
            print('Arguments error: bad mode.')
        self._mode = Program.mode[args[0]]
        self._args = args[1:]

    def work(self):
        if self._mode == Program.mode['--hide']:
            self._hide()
        elif self._mode == Program.mode['--reveal']:
            self._reveal()
        elif self._mode == Program.mode['--help']:
            self.print_help()
        elif self._mode == Program.mode['default']:
            pass
        else:
            raise Exception("Unknown mode.")

    def _hide(self):
        if len(self._args) < 3:
            print("Arguments error.")
        (input_file, hide_data, output_file) = self._args
        with open(hide_data, 'rb') as f:
            data = f.read()
        w = WavContainer(input_file)
        w.hide(data)
        w.save_to_disk(output_file)
        print("Done!")

    def _reveal(self):
        if len(self._args) < 3:
            print("Arguments error.")
        (container, num_bytes, output_file) = self._args
        w = WavContainer(container)
        data = w.reveal(int(num_bytes))
        with open(output_file, 'wb') as f:
            f.write(data)
        print("Done")

    @staticmethod
    def print_help():
        print("HELP INFO.")


def main():
    pass


if __name__ == '__main__':
    main()

#!/usr/bin/python3


from WavContainer.wavContainer import WavContainer



class Program:

    mode = {}
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
        (inputfile, hidedata, outputfile) = self._args
        with open(hidedata, 'rb') as f:
            data = f.read()
        w = WavContainer(inputfile)
        w.hide(data)
        w.saveToDisk(outputfile)
        print("Done!")

    def _reveal(self):
        if len(self._args) < 3:
            print("Arguments error.")
        (container, numBytes, outputfile) = self._args
        w = WavContainer(container)
        data = w.reveal(int(numBytes))
        with open(outputfile, 'wb') as f:
            f.write(data)
        print("Done")

    def print_help(self):
        print("HELP INFO.")



def main():
    pass


if __name__ == '__main__':
    main()

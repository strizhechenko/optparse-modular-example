from optparse import Option, OptionConflictError, OptionParser


class BaseTop:
    options = None

    def __init__(self):
        self.specific_options = [
            Option('-f', '--file', dest='file', help='file to monitor'),
            Option('-i', '--interval', dest='interval', help='interval between file readings in seconds'),
        ]
        # This places seems perfect for call parse_options, but in specifics Top1 /
        # Top2 it should be called AFTER extending by own specific options, not in
        # BaseTop.__init__(self) call. So, little duplicity will be in every subclass.

    def parse_options(self):
        parser = OptionParser()
        for opt in self.specific_options:
            try:
                parser.add_option(opt)
            except OptionConflictError:
                pass  # I don't know how to make a set of options
        self.options, args = parser.parse_args()

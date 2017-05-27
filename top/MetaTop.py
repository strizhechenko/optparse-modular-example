from BaseTop import BaseTop
from optparse import OptionParser, OptionConflictError
from Top1 import Top1
from Top2 import Top2


class MetaTop(BaseTop):
    def __init__(self):
        BaseTop.__init__(self)
        self.tops = [
            Top1(),
            Top2(),
            self,
        ]
        self.parse_options()

    def parse_options(self):
        parser = OptionParser()
        for top in self.tops:
            for opt in top.specific_options:
                try:
                    parser.add_option(opt)
                except OptionConflictError:
                    pass  # I don't know how to make a set of options
        self.options, args = parser.parse_args()

from optparse import Option
from BaseTop import BaseTop


class Top1(BaseTop):
    def __init__(self):
        BaseTop.__init__(self)
        specific_options = [
            Option('-t', '--top1-specific1', dest='top1_specific1', help='Top1 specific option #1'),
            Option('-s', '--top1-specific2', dest='top1_specific2', help='Top1 specific option #2'),
        ]
        self.specific_options.extend(specific_options)

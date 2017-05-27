from optparse import Option
from BaseTop import BaseTop


class Top2(BaseTop):
    def __init__(self):
        BaseTop.__init__(self)
        specific_options = [
            Option('-u', '--top2-specific1', dest='top2_specific1', help='Top2 specific option #1'),
            Option('-w', '--top2-specific2', dest='top2_specific2', help='Top2 specific option #2'),
        ]
        self.specific_options.extend(specific_options)

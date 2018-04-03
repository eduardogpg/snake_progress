class ProgressBar(object):
        
    def __init__(self, fill='█', empty=' ', prefix='Progress', auto_size_bar=True, custome_size_bar=100, show_percentage=True, show_balance=True, precision=2):
        
        self.fill = fill
        self.empty = empty
        self.prefix = prefix

        self.auto_size_bar = auto_size_bar
        self.custome_size_bar = custome_size_bar
        self.show_percentage = show_percentage
        self.show_balance = show_balance
        self.precision = '.{}f'.format(precision)

        self.set_variables()

    def set_variables(self, current=0, buffer=1, skip=False, completed=False):
        self.current = current
        self.buffer = buffer
        self.skip = skip
        self.completed = completed

    def percentage_completed(self):
        percentage = (self.current * 100) / self.buffer
        return float(format(percentage, self.precision))

    def size_bar(self):
        if self.auto_size_bar:
           full_progress_bar_size = self.terminal_size() - len(self.right_text())
           return int((full_progress_bar_size * 80) / 100) #Print in only the 80 percentage of the window
        else:
            return self.custome_size_bar

    def terminal_size(self):
        import os
        
        _, columns = os.popen('stty size', 'r').read().split()
        return int(columns)

    def percentage_format(self):
        return "{}%".format(self.percentage_completed()) if self.show_percentage else ''

    def balance_format(self):
        return "({}/{})".format(self.current, self.buffer) if self.show_balance else ''

    def skip_format(self):
        return "\n" if self.completed or self.skip else ""

    def right_text(self):
        return "{} {} {}".format(self.percentage_format(), self.balance_format(), self.skip_format())

    def progress_bar(self):
        size_bar = self.size_bar()
        progress = (self.percentage_completed() * size_bar) / 100
        
        empty = self.empty * int(size_bar - progress)
        progress = self.fill * int(progress)

        return "{}{}".format(progress, empty)

    def full_progress_bar(self):
        return "{} |{}| {}".format(self.prefix, self.progress_bar(), self.right_text())

    def show_full_progress_bar(self):
        import sys

        sys.stdout.write(self.full_progress_bar())
        sys.stdout.flush()

    def update(self, current, buffer, skip=False):
        self.set_variables(current, buffer, skip)

        self.show_full_progress_bar()

    def complete(self):
        pass


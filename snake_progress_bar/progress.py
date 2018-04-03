class ProgressBar(object):
        
    def __init__(self, fill='█', empty=' ', prefix='Progress', auto_bar_size=True, custome_bar_size=100, show_percentage=True, show_balance=True, precision=2):
        
        self.fill = fill
        self.empty = empty
        self.prefix = prefix

        self.auto_bar_size = auto_bar_size
        self.custome_bar_size = custome_bar_size
        self.show_percentage = show_percentage
        self.show_balance = show_balance
        self.precision = '.{}f'.format(precision)

        self.set_variables()
        self.terminal_size = self.terminal_size()
        

    def set_variables(self, current=0, buffer=1, skip=False, completed=False):
        self.current = current
        self.buffer = buffer
        self.skip = skip
        self.completed = completed

    def percentage_completed(self):
        percentage = (self.current * 100) / self.buffer
        return float(format(percentage, self.precision))

    def bar_size(self):
        if self.auto_bar_size:
           return self.bar_size_suggestion()
        else:
            return self.custome_bar_size

    def bar_size_suggestion(self):
        percentage_text = int( len(self.full_text()) * 100 ) / self.terminal_size
        percentage_bar = int(100 - percentage_text)

        return int((percentage_bar * self.terminal_size) / 100)
            
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
        bar_size = self.bar_size()
        progress = (self.percentage_completed() * bar_size) / 100
        
        empty = self.empty * int(bar_size - progress)
        progress = self.fill * int(progress)

        return "{}{}".format(progress, empty)

    def full_text(self):
        return "{} {}".format(self.prefix, self.right_text())

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


class ProgressBar(object):
        
    def __init__(self, fill='█', empty=' ', prefix='Progress', auto_length=True, custome_length=100, show_percentage=True, show_balance=True, precision=2):
        
        self.fill = fill
        self.empty = empty
        self.prefix = prefix

        self.auto_length = auto_length
        self.custome_length = custome_length
        self.show_percentage = show_percentage
        self.show_balance = show_balance
        self.precision = '.{}f'.format(precision)

        self.set_variables()
        self.percentage_completed = 0.0

    def set_variables(self, current=0, buffer=0, skip=False, completed=False):
        self.current = current
        self.buffer = buffer
        self.skip = skip
        self.completed = completed

    def percentage_format(self):
        return "{}%".format(self.percentage_completed) if self.show_percentage else ''

    def balance_format(self):
        return "({}/{})".format(self.current, self.buffer) if self.show_balance else ''

    def skip_format(self):
        return "\n" if self.completed or self.skip else ""

    def right_text(self):
        return "{} {} {}".format(self.percentage_format(), self.balance_format(), self.skip_format())

    def progress_bar(self):
        return "███████████████           "

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


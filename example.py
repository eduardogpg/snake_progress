from snake_progress_bar import ProgressBar
from time import sleep

#First example
#output
print("First Example")

progress_bar = ProgressBar(prefix='Progress completed')
progress_bar.update(50, 100, True)

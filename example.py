from snake_progress_bar import ProgressBar
from time import sleep

#First example
#output
#progress |██████████████████████████████████████████████████| 100.0% (100/100)

print("First Example")
progress_bar = ProgressBar(size=50, show_balance=True)

items = list(range(0, 100))
for i, item in enumerate(items):
     sleep(0.1)
     progress_bar.update_progress(i, len(items))

progress_bar.complete()

#Second example
#output
#Progress completed |🦖🦖🦕🦕🦕🦕🦕🦕🦕🦕🦕🦕🦕🦕🦕🦕🦕🦕🦕🦕|
print("\n")
print("Second Example")
progress_bar = ProgressBar(size=20, fill='🦖', empty='🦕', prefix='Progress completed', show_percentage=False, show_balance=False)
progress_bar.update_progress(10, 100, True)

#Third example
#output
#progress |███████████         | 55.5% (55.5/100)
print("\n")
print("Third Example")
progress_bar = ProgressBar(size=20)
progress_bar.update_progress(55.5, 100, True)
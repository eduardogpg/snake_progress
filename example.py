from snake_progress_bar import ProgressBar
from time import sleep

progress_bar = ProgressBar()
items = list(range(0, 100))

for i, item in enumerate(items):
     sleep(0.1)
     progress_bar.update(i * 100, len(items) * 100)

progress_bar.complete()


"""
#First example
#output
#Progress |██████████████████                                                      | 25.0% (25/100)
print("\n>First Example")

progress_bar = ProgressBar() #Default Values
progress_bar.update(25, 100, True) #Current 25, total 100, skip line True



#Second example
#output
#Progress completed |///////                                                                   |   
print("\n>Second Example")

progress_bar = ProgressBar(fill='/', prefix='Progress completed', show_percentage=False, show_balance=False)
progress_bar.update(10, 100, True)

#Third example
#output
#Progress |******------------------------------------------------------| 10.0% (10/100
print("\n>Third Example")

progress_bar = ProgressBar(fill='*', empty='-', auto_bar_size=False, custome_bar_size=60)
progress_bar.update(10, 100, True)


#Fourth example
#output
#Progress |███████████████████████████████████████████████████████████████████████████████| 100.0%
print("\n>Fourth Example")

progress_bar = ProgressBar()
progress_bar.complete()

"""
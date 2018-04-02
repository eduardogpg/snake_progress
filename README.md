### Snake Progress bar

ProgressBar is a class that allows to show a progress bar in console.
The progress bar is very felixble, you can modifie the size, prefix, bar fill character (any chacarater, and yes, you can use emojis) you can show the percentage or the balance if you need them.

#### Install

For the correct use, you musts to have Python 3 or above version.

```
pip install snake_progress_bar
```

#### Usage

For use it, you needs to import the class ``` from snake_progress import Progress Bar ```
Once you imports the class, is necessary create a new object,

```
progress_bar = ProgressBar()
````

Optional params

    fill                - Optional  : Bar fill character, default █ (Str)
    empty               - Optional  : Bar empty character, default blank space (Str)
    size                - Optional  : Bar size (Int)
    prefix              - Optional  : Prefix string (Str)
    current             - Optional  : Initial position (Int)
    buffer              - Optional  : Buffer size (Int)
    show_percentage     - Optional  : If True, the percentage is shown at the end
    show_balance        - Optional  : If True, the balance is shown at the end
    precision           - Optional  : Float precision (Int)

With the object, you can use the methods ```update_progress``` or ```complete```.

__update_progress__ method updates the progress bar. Required params _current_ and _buffer_. Optional param _skip_.

__complete__ method complete the progress bar. The _current_ attribute will be equals to _buffer_ attribute.

#### Examples

```
from snake_progress import ProgressBar
from time import sleep

progress_bar = ProgressBar(size=50, show_balance=True)

items = list(range(0, 100))
for i, item in enumerate(items):
     sleep(0.1)
     progress_bar.update_progress(i, len(items))

progress_bar.complete()

progress_bar = ProgressBar(size=20, fill='🦖', empty='🦕', prefix='Progress completed', show_percentage=False, show_balance=False)
progress_bar.update_progress(10, 100, True)

progress_bar = ProgressBar(size=20)
progress_bar.update_progress(55.5, 100, True)
```

### Developer
@eduardo_gpg

License
----

MIT

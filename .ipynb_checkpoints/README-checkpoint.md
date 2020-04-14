# KlondBar \m/_(>_<)_\m/
*coded by dAriush* 

## what is klondbar?
klondbar is a simple progress bar with lots of customizations!
here are some of this customizable features:
* adding header to progress bar
* changing bar width
* changing progress steps
* adding a footnote
* changing the color of progress bar

*Beside these fun customizations, KlondBar also reacts with some funny ASCII emojis like this: \\(^-^)/ Pass your expected time as an argument and if calculations take longer than that, KlondBar will show it's angry face to you!*

## how to install klondbar?
use pip like any other package:

    pip install klondbar

    or: python3 -m pip install klondbar
    

## How to use:

    progress_bar = KlondBar(*args, **kwargs)
    
args:
 * iterable_object

kwargs:
* task_name=''
* bar_width=80
* steps_number=80
* footnote=''
* expected_time = 20
* color='grey'

*this is a sample code:*

    from klondbar.klondbar_module import KlondBar
    
    # First construct an iterable_object for using in "for loop"
    iterable_object = range(500000)

    # KlondBar object construction
    # test_bar is an instance of KlondBar class
    test_bar = KlondBar(iterable_object, task_name='task title',
                        bar_width = 80, footnote='footnote',
                        steps_number = 80, color='cyan')

    print('before start')

    # Place start method before "for loop"; don't pass any argument to it
    test_bar.start()
    for i in iterable_object:
        # Place midle method after "for loop" definition,
        # pass "for loop" iterator to midle method. like this:
        test_bar.midle(i)

        # place your calculations here
        i**200
    
    # Place end method after "for loop" block, don't pass any argument to it
    test_bar.end()

    print('after end')

Here's the output:

![Output Screenshot][logo]

[logo]: https://gitlab.com/dariush-bahrami/klondbar_project/-/raw/master/output%20example.png?inline=false

## More information

* code repository: https://gitlab.com/dariush-bahrami/klondbar_project.git
* PyPI page: https://pypi.org/project/klondbar/
* dAriush email address: dariush.bahrami@ut.ac.ir
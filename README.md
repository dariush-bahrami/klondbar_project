# KlondBar \m/_(>_<)_\m/
*coded by dAriush*

## what is klondbar?
klondbar is a simple progress bar with lots of customizations!
here is some of this customizable features:
*adding header to progress bar
*changing bar width
*changing progress steps
*adding a footnote
*changing the color of progress bar
beside this fun customizations, KlondBar react to you by some funy ASCII emojies like this: \(^-^)/
pass your expected time as an argument and see. if calculations take longer then KlondBar show you it's angry face.

## how to install klondbar?
use pip like any other pakcage:
pip install klondbar

## How to use:
progress_bar = KlondBar(*args, **kwargs)
args:
iteration_list 
kwargs:
task_name=''
bar_width=80
steps_number=80
footnote=''
expected_time = 20
color='grey'

*this is a sample code:*
    from klondbar.klondbar_module import KlondBar
    
    end_of_range = int(1000)

    # KlondBar object construction; test_bar is an instance of KlondBar class
    test_bar = KlondBar(range(end_of_range), task_name='lostham',
                        bar_width = 80, footnote='fandogh',
                        steps_number = 80, color='cyan')

    print('before start method')
    
    test_bar.start()
    for i in range(end_of_range):
        test_bar.midle(i)
        
        # place your calculations here
        
    test_bar.end()
    
    print('after end method')

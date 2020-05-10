''' Klond Bar is python module which can be used to create fun progress bar
    objects by using only ASCII characters; coded by dAriush
'''


class ColoredMegaBar:
    ''' dAriush progress bar class
    '''

    # Except iterable_object, all arguments are optional
    def __init__(self,
                 iterable_object,
                 task_name='',
                 bar_width=80,
                 steps_number=80,
                 footnote='',
                 expected_time=20,
                 color='grey'):
        '''__init__ KlondBar class constructor

        Parameters
        ----------
        iterable_object : like list, tuple, strings
            this is same iterable object that will be used in for loop
        task_name : str, optional
            progress title, by default ''
        bar_width : int, optional
            width of the bar, by default 80
        steps_number : int, optional
            total progress steps, by default 80
        footnote : str, optional
            text at the bottom of progress bar, by default ''
        expected_time : int, optional
            your prediction of process time, by default 20
        color : str, optional
            valid entries: grey, red, green, yellow, blue, magenta, cyan,
            white, by default 'grey'
        '''

        # Preparing requirements
        #
        # Checking steps_number validity; steps_number should divide bar_width
        assert bar_width % steps_number == 0, 'invalid entry, steps_number should divide bar_width'
        # Importing a function which returns random emoji arts for
        # header of progress bar
        import os        
        self.colors = {
            'BLACK': '\033[30m',
            'RED': '\033[31m',
            'GREEN': '\033[32m',
            'YELLOW': '\033[33m',
            'BLUE': '\033[34m',
            'MAGENTA': '\033[35m',
            'CYAN': '\033[36m',
            'WHITE': '\033[37m',
            'UNDERLINE': '\033[4m',
            'RESET': '\033[0m'
        }
        self.emojis = [
            '\m/_(>_<)_\m/',
            '\m/ (>.<) \m/',
            '\,,/(^_^)\,,/',
            '\(^-^)/',
            '( 0 _ 0 )',
            'd[-_-]b',
            '<(^_^)>',
            '¯\(°_o)/¯',
            '[¬º-°]¬',
            '(V) (°,,,,°) (V)]',
        ]

        # Assigning basic attributes
        self.color = color.upper()
        os.system("")  # allows you to print ANSI codes in the Terminal
        print(self.colors[self.color])
        self.iterable_object = iterable_object
        self.iterations_number = len(iterable_object)
        self.task_name = task_name
        self.bar_width = bar_width
        self.steps_number = steps_number
        self.step = int(self.bar_width / self.steps_number)  # progress step

        # progress data calculation
        #
        # KlondBar need a list of desired values in iterable_object to
        # excute a progress step; this list defined as progress_points

        self.progress_points = [
            j * (1 / self.steps_number) * int(len(iterable_object))
            for j in range(1, self.steps_number)
        ]

        # The elapsed_steps attribute is a counter for passed steps
        self.elapsed_steps = 0

        # Time consumption calculation
        #
        # Wasted time per iteration is a experimental gues of how much
        # time consumes just for KlondBar

        self.expected_time = expected_time
        self.WASTED_TIME_PER_ITERATION = 623.2e-9
        self.total_wasted_time = (self.WASTED_TIME_PER_ITERATION *
                                  self.iterations_number)

        # Header and footer Construction
        #
        # Header of the KlondBar splited into two part, emoji and title
        # by default 0.4 of bar width allocated to emoji and remained
        # 0.6 of bar width allocated to title which is formated version
        # of task_name
        emoji_width = int(self.bar_width * 0.4) - 1  # -1 for opening character
        title_width = int(self.bar_width * 0.6) - 1  # -1 for ending character
        emoji = f'{self.get_random_emoji(): ^{emoji_width}s}'
        title = f'{task_name: ^{title_width}s}'
        top_box = '▄' * self.bar_width + '\n'
        self.header = f'{top_box}▌{emoji}{title}▐'
        self.footnote = footnote + '\n'

    def get_random_emoji(self):
        '''returning random emoji from emoji collection "klond_art_emojis.txt"'''
        from random import randint

        random_emoji = self.emojis[randint(0, len(self.emojis) - 1)]

        return random_emoji

    def start(self):
        '''start This method should be placed just before for block
        '''

        from timeit import default_timer as timer

        self.start_time = timer()
        print(f'\n{self.header}', flush=True)
        print('▌', end="", flush=True)

    def midle(self, i):
        '''midle This method should be placed at first line of for block

        Parameters
        ----------
        i : same as for block iterator
        '''

        # in folowing if block program determines when to pass one step
        if i in self.progress_points:
            print('▓' * (self.step),
                  end="",
                  flush=True)
            # whenever a progress step is passed, elapsed_steps counter
            # sholud be ubdated by adding 1 to it
            self.elapsed_steps += 1

    def end(self):
        '''end This method should be placed just after for block
        '''

        from timeit import default_timer as timer

        self.stop_time = timer()
        self.elapsed_time = self.stop_time - self.start_time

        # It is possible that elapsed steps do not reach desired steps
        # number this is mostly because of integer conversion of
        # progress points
        #This problem can be solved by using elapsed_steps counter,
        # at the end of progress remaining characters will have calculated
        # and printed
        #
        # in remained_character, -2 appears for opening and ending characters

        remained_character = self.bar_width - self.elapsed_steps * self.step - 2
        print('▓' * remained_character + '▐',
              flush=True)

        self.remained_steps = self.steps_number - self.elapsed_steps

        # Printing progress bar status
        #
        # If consumed time by KlondBar be more than 10% of total process
        # time, a sad status appears

        if ((self.total_wasted_time) / (self.elapsed_time) * 100) > 10:
            print(f'    (ಥ﹏ಥ) progress completed in ' +
                  f'{self.elapsed_time:.3f}s',
                  flush=True)
            print(self.footnote, flush=True)

        # If total process time be greater than expected time, an angry
        # status appears
        elif self.elapsed_time > self.expected_time:
            print('    (╯°□°）╯︵ ┻━┻ Progress completed in {0:.3f}s'.format(
                self.elapsed_time) + ' it was boring' +
                  self.colors[self.color],
                  flush=True)
            print(self.footnote, flush=True)

        # In any other condition a heroic status will shows up
        else:
            print(f'    ─=≡Σ((( つ◕ل͜◕)つ Progress completed in ' +
                  f'{self.elapsed_time:.3f}s\n',
                  flush=True)
            print(self.footnote, flush=True)
        print(self.colors['RESET'], end='', flush=True)


## Debug section
if __name__ == '__main__':
    import time
    # First construct an iterable_object for using in "for loop"
    iterable_object = range(50)

    # KlondBar object construction
    # test_bar is an instance of KlondBar class
    test_bar = ColoredMegaBar(iterable_object,
                              task_name='task title',
                              bar_width=80,
                              footnote='footnote',
                              steps_number=80,
                              color='cyan')

    print('before start', flush=True)

    # Place start method before "for loop"; don't pass any argument to it
    test_bar.start()
    for i in iterable_object:
        # Place midle method after "for loop" definition,
        # pass "for loop" iterator to midle method. like this:
        test_bar.midle(i)

        # place your calculations here
        time.sleep(0.1)  # any calculation you need

    # Place end method after "for loop" block, don't pass any argument to it
    test_bar.end()

    print('after end', flush=True)
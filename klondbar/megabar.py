''' Klond Bar is python module which can be used to create fun progress bar
    objects by using only ASCII characters; coded by dAriush
'''


class MegaBar:
    ''' dAriush progress bar class
    '''

    # Except iterable_object, all arguments are optional
    def __init__(self,
                 iterable_object,
                 task_name='',
                 bar_width=80,
                 expected_time=20,
                 colored_bar=False):
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
        # assert bar_width % steps_number == 0, 'invalid entry, steps_number should divide bar_width'
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
        ]

        self.colored_bar = colored_bar
        if self.colored_bar:
            self._color = 'WHITE'
            os.system("")  # allows you to print ANSI codes in the Terminal
            print(self.colors[self.color], end="", flush=True)

        # Assigning basic attributes

        self.iterable_object = iterable_object
        self.iterations_number = len(iterable_object)
        self.task_name = task_name
        self.bar_width = bar_width
        self.step = int(self.bar_width / self.steps_number)  # progress step
        # self.maximum_steps = self.step *

        # progress data calculation
        #
        # KlondBar need a list of desired values in iterable_object to
        # excute a progress step; this list defined as progress_points

        self.progress_points = [
            int(j * (self.iterations_number / self.steps_number))
            for j in range(0, self.steps_number)
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

    @property
    def steps_number(self):
        return self.bar_width - 2

    def get_random_emoji(self):
        '''returning random emoji from emoji collection "klond_art_emojis.txt"'''
        from random import randint

        random_emoji = self.emojis[randint(0, len(self.emojis) - 1)]

        return random_emoji

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, user_color_choice):
        import os
        if self.colored_bar:
            self._color = user_color_choice.upper()
            print(self.colors[self.color], end="", flush=True)
        else:
            print('For printing colored megabars pass "colored_bar=True" argument in constructor')

    def start(self):
        '''start This method should be placed just before for block
        '''

        import time

        self.start_time = time.perf_counter()
        print(f'{self.header}', flush=True)
        print('▌', end="", flush=True)

    def midle(self, i):
        '''midle This method should be placed at first line of for block

        Parameters
        ----------
        i : same as for block iterator
        '''

        # in folowing if block program determines when to pass one step
        if i in self.progress_points:
            print('▓' * (self.step), end="", flush=True)
            # whenever a progress step is passed, elapsed_steps counter
            # sholud be ubdated by adding 1 to it
            self.elapsed_steps += 1

    def end(self):
        '''end This method should be placed just after for block
        '''

        import time

        stop_time = time.perf_counter()
        elapsed_time = stop_time - self.start_time
        formated_elapsed_time = time.strftime("%M:%S",
                                              time.gmtime(elapsed_time))
        elapsed_time_string = f'Elapsed time: {formated_elapsed_time}'
        footer_time = f'▌{elapsed_time_string: ^{self.bar_width-2}s}▐' 
        bottom_box = '▀' * self.bar_width
        footer = footer_time + '\n' + bottom_box
        # It is possible that elapsed steps do not reach desired steps
        # number this is mostly because of integer conversion of
        # progress points
        #This problem can be solved by using elapsed_steps counter,
        # at the end of progress remaining characters will have calculated
        # and printed
        #
        # in remained_character, -2 appears for opening and ending characters

        remained_character = self.bar_width - self.elapsed_steps * self.step - 2
        print('▓' * remained_character + '▐', flush=True)

        # Printing elapsed time status
        print(footer, flush=True)

        if self.colored_bar:
            print(self.colors['RESET'], end='', flush=True)

    def run(self):
        self.start()

        for counter, item in enumerate(iterable_object):
            yield item
            self.midle(counter)

        self.end()


## Debug section
if __name__ == '__main__':
    import time
    # First construct an iterable_object for using in "for loop"
    iterable_object = range(20)

    # KlondBar object construction
    # test_bar is an instance of KlondBar class
    print('colorless bar test:')
    test_bar = MegaBar(iterable_object, task_name='task title', bar_width=80)
    test_bar.color = 'blue'

    for i in test_bar.run():
        # place your calculations here
        time.sleep(0.1)  # any calculation you need

    print('colored bar test:')
    colored_test_bar = MegaBar(iterable_object,
                               task_name='task title',
                               bar_width=40,
                               colored_bar=True)
    colored_test_bar.color = 'cyan'

    for i in colored_test_bar.run():
        # place your calculations here
        time.sleep(0.1)  # any calculation you need

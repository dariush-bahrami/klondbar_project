def progressbar(iterable_object, title="", bar_length=40):
    import time
    import sys

    start_time = time.perf_counter()
    file = sys.stdout
    iterations = len(iterable_object)

    def update_bar(current_step):
        progressed_steps = int(current_step * (bar_length / iterations))
        progress_character = '#'
        progressed_steps_string = progress_character * progressed_steps

        remained_steps = bar_length - progressed_steps
        remained_character = "."
        remained_steps_string = remained_character * remained_steps

        step_time = time.perf_counter()
        elapsed_time = step_time - start_time
        elapsed_time_string = time.strftime("%M:%S", time.gmtime(elapsed_time))

        bar_string = '{0}[{1}{2}] {3}/{4} elapsed time: {5}'.format(
            title, progressed_steps_string, remained_steps_string,
            current_step, iterations, elapsed_time_string)

        # uncomment following line to use backspace for clearing line
        # file.write('\b' * len(bar_string))
        file.write('\r')
        file.write(bar_string)
        file.flush()

    update_bar(0)  # Initializing Progress Bar

    for counter, item in enumerate(iterable_object):
        yield item
        update_bar(counter + 1)

    file.write("\n")
    file.flush()


def colored_progressbar(iterable_object, title="", bar_length=40,
                        color='magenta'):
    import time
    import sys
    import os

    start_time = time.perf_counter()
    file = sys.stdout
    iterations = len(iterable_object)

    os.system("")  # allows you to print ANSI codes in the Terminal
    colors = {
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

    def update_bar(current_step):
        progressed_steps = int(current_step * (bar_length / iterations))
        progress_character = '#'
        progressed_steps_string = progress_character * progressed_steps

        remained_steps = bar_length - progressed_steps
        remained_character = "."
        remained_steps_string = remained_character * remained_steps

        step_time = time.perf_counter()
        elapsed_time = step_time - start_time
        elapsed_time_string = time.strftime("%M:%S", time.gmtime(elapsed_time))

        bar_string = '{0}[{1}{2}] {3}/{4} elapsed time: {5}'.format(
            title, progressed_steps_string, remained_steps_string,
            current_step, iterations, elapsed_time_string)

        # uncomment following line to use backspace for clearing line
        # file.write('\b' * len(bar_string))
        file.write('\r')
        file.write(bar_string + colors[color.upper()])
        file.flush()

    update_bar(0)  # Initializing Progress Bar

    for counter, item in enumerate(iterable_object):
        yield item
        update_bar(counter + 1)

    file.write("\n")
    file.write(colors['RESET'])
    file.flush()


# Test Section
if __name__ == '__main__':
    import time
    print('Minimal progressbar:')
    for i in progressbar(range(10)):
        time.sleep(0.1)  # any calculation you need

    print('Colored progressbar:')
    for i in colored_progressbar(range(10)):
        time.sleep(0.1)  # any calculation you need

    for i in colored_progressbar(range(10)):
        time.sleep(0.1)  # any calculation you need
    for i in colored_progressbar(range(10)):
        time.sleep(0.1)  # any calculation you need

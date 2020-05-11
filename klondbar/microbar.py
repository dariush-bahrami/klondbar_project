def micro_bar(iterable_object, title="", bar_length=40):
    """just wrap for loop sequence with micro_bar

    Parameters
    ----------
    iterable_object : any iterable object
        this is what you want to pass to the for loop
    title : str, optional
        bar prefix, by default ""
    bar_length : int, optional
        by default 40

    Yields
    -------
    items in iterable_objects
    """
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

        bar_string = '{0}[{1}{2}] {3}/{4} Elapsed time: {5}'.format(
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



# Debug Section
if __name__ == '__main__':
    import time
    print('Minimal microbar:')
    for i in micro_bar(range(10)):
        time.sleep(0.1)  # any calculation you need

    print('Customized microbar:')
    for i in micro_bar(range(10), title='title:', bar_length=20):
        time.sleep(0.1)  # any calculation you need
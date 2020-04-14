'''Klond Art Module; Coded by dAriush'''

emojis = [
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

def klond_random_emoji():
    '''returning random emoji from emoji collection "klond_art_emojis.txt"'''
    from random import randint

    random_emoji = emojis[randint(0, len(emojis) - 1)]

    return random_emoji


def klond_pretty_line(text, line_width=80, alignment='^', filler_symbol='',
                      first_letters='', last_letters=''):
    '''this function returns a formated text with lots of customizations'''

    text_width = line_width - len(first_letters) - len(last_letters) - 2
    return '{0} {1:{2}{3}{4}s} {5}\n'.format(first_letters, text, filler_symbol,
                                             alignment, text_width,
                                             last_letters)


def klond_text_box(*args, **user_defined_properties):
    # Defining default properties
    default_properties = {'width': 80, 'margin_symbol': '▓',
                          'filler_symbol': '', 'margin_y_thickness': 1,
                          'margin_x_thickness': 2,
                          'lines_alignment': ['^' for i in args]}
    # Unpacking properties dictionary and combining that with default properties
    #
    # By mentioning user defined properties after default ones in
    # properties dictionary, user's entries override default properties
    properties = {**default_properties, **user_defined_properties}

    # Extracting properties from properties dictionary by using the keys:
    width = properties['width']
    margin_symbol = properties['margin_symbol']
    filler_symbol = properties['filler_symbol']
    # Some useful symbols for customization: • ◘ ○ ♪ º ░ ▒ ▓ ┼ ╓ ╥ ╖ ╙ ╨ ╜ █ ≡ ■
    margin_y_thickness = properties['margin_y_thickness']
    margin_x_thickness = properties['margin_x_thickness']
    lines_alignment = properties['lines_alignment']

    # Text box construction:
    horizontal_margin = (f'{margin_symbol}'*width + '\n') * margin_y_thickness
    margin_symbols = margin_symbol*margin_x_thickness
    vertical_space = klond_pretty_line(text='', line_width=width,
                                       first_letters=margin_symbols,
                                       last_letters=margin_symbols,
                                       filler_symbol=filler_symbol)
    context = horizontal_margin + vertical_space

    counter = 0
    for line in args:
        context += klond_pretty_line(text=line,
                                     alignment=lines_alignment[counter],
                                     line_width=width,
                                     first_letters=margin_symbols,
                                     last_letters=margin_symbols,
                                     filler_symbol=filler_symbol)
        counter += 1

    context += vertical_space + horizontal_margin
    return context
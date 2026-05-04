"""Module provides an easy way to find out a resistor's band colors and code."""
def color_code(color):
    return colors().index(color)


def colors():
    return [
        'black',
        'brown',
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'violet',
        'grey',
        'white'
    ]

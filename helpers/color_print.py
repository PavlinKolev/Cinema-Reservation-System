import sys
from termcolor import colored, cprint


def print(string):
    cprint(string, 'green')


def input_(string):
    text = colored(string, 'green')
    return input(text)

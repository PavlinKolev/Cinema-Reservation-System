import os
from user_interface.interface import Interface
from helpers.color_print import input_


def run_program():
    name = input_("Enter the cinema name:> ")
    cinema = Interface(name)
    cinema.run()

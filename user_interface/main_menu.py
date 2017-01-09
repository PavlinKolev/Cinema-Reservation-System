import os
from user_interface.interface import Interface


def run_program():
    name = input("Enter the cinema name:> ")
    cinema = Interface(name)
    cinema.run()

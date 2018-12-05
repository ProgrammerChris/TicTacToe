#setup.py
import sys, os
from cx_Freeze import setup, Executable

__version__ = "1.1.0"

excludes = ["tkinter"]
packages = ["os", "pygame"]

setup(
    name = "TicTacToe",
    description='Simple Tic tac toe game made in python with pygame',
    version=__version__,
    options = {"build_exe": {
    'packages': packages,
    'excludes': excludes,
    'include_msvcr': True,
}},
executables = [Executable("tictactoe.py",base="Win32GUI")]
)
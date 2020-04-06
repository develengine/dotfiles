#!/usr/bin/env python3

from os import popen
from os import system
from sys import argv
from time import sleep
import json

def main():

    def update_bar():
        date = popen('date +%D').read().strip()
        time = popen('date +%T').read().strip()
        
        delim = ' | '
    
        system('xsetroot -name " ' + date + delim + time + ' "')

    if "loop" in argv:
        while True:
            update_bar()
            sleep(5)

    update_bar()

main()

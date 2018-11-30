#!/usr/bin/env python3

"""SIGINT_Ctrl+C.py
Author: Joseph Lin
Email : joseph.lin@aliyun.com

Social:
  https://github.com/RDpWTeHM
  https://blog.csdn.net/qq_29757283

Note:
  Ctrl+C <==> SIGINT

"""

# import sys
# import os
# import atexit
import signal
from time import sleep


# Signal handler for termination (required)
def sigint_handler(signo, frame):
    ''' show catch Ctrl+C information!'''
    print("\nGoodbay Cruel World.....\n")
    raise SystemExit(1)


def prog_init():
    signal.signal(signal.SIGINT, sigint_handler)


def main():
    prog_init()

    counter = 0
    while True:
        print("Guess what am I running....{}s".format(counter), end="")
        sleep(1)
        counter += 1
        print("\r", end="")


if __name__ == '__main__':
    main()

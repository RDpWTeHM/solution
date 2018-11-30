#!/usr/bin/env python3

"""SIGALRM_calculate-game.py
Author: Joseph Lin
Email : joseph.lin@aliyun.com

Social:
  https://github.com/RDpWTeHM
  https://blog.csdn.net/qq_29757283

Note:
  signal.alarm(integer) ==> SIGALRM

"""

import sys
import os
# import atexit
import signal
# from time import sleep
from random import randint


score = 0
prog_pid = os.getpid()
if __debug__:
    print("[Debug] prog_pid <- os.getpid(): {}".format(prog_pid))


def sigalrm_handler(signo, frame):
    ''' game time up'''
    global prog_pid
    print("\nOooooops game time up!")
    os.kill(prog_pid, signal.SIGINT)


def sigint_handler(signo, frame):
    ''' end game'''
    global score
    print("\nFinal score: {}\n".format(score))
    raise SystemExit(0)


def prog_init():
    signal.signal(signal.SIGALRM, sigalrm_handler)
    signal.signal(signal.SIGINT, sigint_handler)


def main():
    global score
    global prog_pid

    prog_init()

    print("!!!!!game start!!!!!")

    while True:
        a = randint(0, 10)
        b = randint(0, 10)

        signal.alarm(5)  # set game time
        print("Calculate {} x {} = ?: ".format(a, b), end='')
        try:
            user_input = int(input())
        except ValueError:
            print("Error input! Expect numbers.", file=sys.stderr)
            os.kill(prog_pid, signal.SIGINT)

        if a * b == user_input:
            print("Right!\n")
            score += 1
        else:
            os.kill(prog_pid, signal.SIGINT)


if __name__ == '__main__':
    main()

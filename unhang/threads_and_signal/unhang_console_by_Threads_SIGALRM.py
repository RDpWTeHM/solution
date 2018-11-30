#!/usr/bin/env python3

"""unhang_console_by_Threads_SIGALRM.py
Author: Joseph Lin
Email : joseph.lin@aliyun.com

Social:
  https://github.com/RDpWTeHM
  https://blog.csdn.net/qq_29757283

Note:
  signal.alarm(integer) ==> SIGALRM
  alarm may can't not work well with sleep in some python version.
"""

# import sys
import os
# import atexit
import signal
# from random import randint
from time import sleep


prog_pid = os.getpid()
if __debug__:
    print("[Debug] prog_pid <- os.getpid(): {}".format(prog_pid))


def sigalrm_handler(signo, frame):
    ''' time up'''
    global prog_pid
    print("\nOooooops time up!")
    os.kill(prog_pid, signal.SIGINT)


def sigint_handler(signo, frame):
    ''' end program'''
    print("")
    raise SystemExit(0)


def prog_init():
    signal.signal(signal.SIGALRM, sigalrm_handler)
    signal.signal(signal.SIGINT, sigint_handler)


def main():
    global prog_pid

    prog_init()

    signal.alarm(5)
    i = 0
    circle = ('|', '/', '-', '\\')
    while True:
        sleep(0.2)
        print("\rprocessing... {}".format(circle[i]), end='')
        i = 0 if i == 3 else i + 1


if __name__ == '__main__':
    main()

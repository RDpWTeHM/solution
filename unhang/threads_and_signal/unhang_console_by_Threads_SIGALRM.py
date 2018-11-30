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
import threading


request_pages_result = {}
prog_pid = os.getpid()
if __debug__:
    print("[Debug] prog_pid <- os.getpid(): {}".format(prog_pid))


def sigalrm_handler(signo, frame):
    ''' time up'''
    global request_pages_result
    global prog_pid
    print("\nOooooops time up!")
    print("[sigalrm_handler] request pages result: \n", request_pages_result)
    os.kill(prog_pid, signal.SIGINT)


def sigint_handler(signo, frame):
    ''' end program'''
    global request_pages_result
    print("\nGoodbay Cruel World.....")
    print("[sigint_handler] before exit program, show you the result:\n", request_pages_result)
    raise SystemExit(0)


def prog_init():
    signal.signal(signal.SIGALRM, sigalrm_handler)
    signal.signal(signal.SIGINT, sigint_handler)


def request_pages():
    global request_pages_result
    sites = ("https://www.baidu.com",
             "https://www.bing.com",
             "https://www.yahoo.com",
             "http://www.so.com")

    import requests
    try:
        for site in sites:
            r = requests.get(site)
            if r.status_code != 200:
                request_pages_result[site] = False
            else:
                request_pages_result[site] = True
    except Exception as e:
        print("[Error] request_pages(): ", e, file=sys.stderr)


def main():
    global request_pages_result
    global prog_pid

    prog_init()

    t = threading.Thread(target=request_pages)
    t.setDaemon(True)
    t.start()
    print("request pages result: \n", request_pages_result)
    print("start the function which will cost lots of time.")

    # 5 second later, run the register function which will show the result.
    signal.alarm(5)

    # main thread keep doing things
    i = 0
    circle = ('|', '/', '-', '\\')
    while True:
        sleep(0.2)
        print("\rmain thread processing... {}".format(circle[i]), end='')
        i = 0 if i == 3 else i + 1


if __name__ == '__main__':
    main()

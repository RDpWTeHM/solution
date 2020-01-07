#!/usr/bin/env python3

import traceback
import threading
from time import sleep


class foo(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.err_msg = None

    def run(self):
        sleep(1)
        try:
            ret = 3 / 0
        except Exception as err:
            err_msg = traceback.format_exc()
        self.err_msg = err_msg

    def get_err_msg(self):
        return self.err_msg


class bar(threading.Thread):
    def __int__(self):
        threading.Thread.__init__(self)
        self.err_msg = None

    def run(self):
        sleep(2)
        try:
            l = [1, 2, 3]
            i = l[3]
        except Exception as err:
            err_msg = traceback.format_exc()
        self.err_msg = err_msg

    def get_err_msg(self):
        return self.err_msg


def main():
    div_thr = foo()
    idx_thr = bar()

    div_thr.start()
    idx_thr.start()

    div_thr.join()
    idx_thr.join()

    print("==== error message ====")
    print("foo thread error message:\n", div_thr.get_err_msg())
    print("bar thread error message:\n", idx_thr.get_err_msg())

    print("==== end ====")


if __name__ == "__main__":
    main()

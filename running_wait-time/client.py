#!/usr/bin/env python3

"""
Author: Joseph Lin
E-mail: joseph.lin@aliyun.com

Social: https://github.com/RDpWTeHM
        https://me.csdn.net/qq_29757283
"""
import sys
# import os
from multiprocessing.connection import Client
# import time
from time import ctime
from time import sleep


def main():
    missions = [#"localhost", "google.com", "myrpiserver.com", "bing.com",
                #"www.csdn.net",
                "yahoo.com", "google.com", "www.jd.com", "www.baidu.com",
                "www.amazon.com", "www.gitee.com",
    ]

    def timeoutsleep():
        _totimes = 0

        def runningsleep(IsTimeout):
            nonlocal _totimes  # fluent python - & 7.6 nonlocal
            if IsTimeout is False:
                _totimes = 0
            elif IsTimeout is True:
                _totimes += 1
                if __debug__: sleep(_totimes * 2)
                else:         sleep(_totimes * 5)
            else:
                raise Exception("<timeoutsleep> Error parameter gived!")
        return runningsleep

    tosleep = timeoutsleep()

    cconn = Client(("localhost", 15337), authkey=b"running_wait-time")

    try:
        for mission in missions:
            cconn.send("http://" + mission)
            page_source = cconn.recv()

            if "timeout" == page_source.lower():
                print("[{}] timeout in {}!".format(ctime(), mission))
                tosleep(True)
            else:
                print("[{}] get {} suucess!".format(ctime(), mission))
                tosleep(False)
    except EOFError:
        print("Server closed the IPC connection!", file=sys.stderr)
        raise SystemExit("Mission Interrupt due to server closed connection!")
    else:
        cconn.close()


if __name__ == "__main__":
    main()

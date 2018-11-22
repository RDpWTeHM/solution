#!/usr/bin/env python3

"""
Author: Joseph Lin
E-mail: joseph.lin@aliyun.com

Social: https://github.com/RDpWTeHM
        https://me.csdn.net/qq_29757283
"""
import os
import sys
# import time
from time import ctime
# from time import sleep
import signal

from multiprocessing.connection import Listener

from selenium import webdriver
from selenium.common.exceptions import TimeoutException

PATH = os.environ.get("PATH", None)
os.environ['PATH'] = "/usr/lib/chromium-browser:" + PATH


browser = webdriver.Chrome()
browser_bkup = browser  # just in case lost browser banding.

browser.implicitly_wait(20)
browser.set_script_timeout(20)    # lower timeout can be easy to
browser.set_page_load_timeout(20)


def handler_client(conn):
    while True:  # handle client until client close the connection
        try:
            recv = conn.recv()
        except EOFError:
            print("Connection closed at {}".format(ctime()))
            break
        except Exception as e:  # 如何在测试中跑到这个 condition？？？
            print("[Error] Unexcept Exception: ", e, file=sys.stderr)
            print("\tclose connection but not exit program!", file=sys.stderr)
            conn.close()
            break
        else:
            try:
                print("[{}][INFO] request {}".format(ctime(), recv))
                safe_get_tab = browser.window_handles[0]

                excute_script_str = "window.open('{}','handler_tab');".format("about:blank")
                browser.execute_script(excute_script_str)
                browser.switch_to.window('handler_tab')

                browser.get(recv)
            except TimeoutException as e:
                print("[{}][WARNING] get '{}' page source timeout!".format(ctime(), recv))
                print("\t", "=" * 15, "TimeoutException: ", "=" * 15, "\n", e)
                # browser.execute_script("window.stop();")
                page_source = "timeout"
            else:
                print("[{}][INFO] finish get '{}' page source".format(ctime(), recv))
                page_source = browser.page_source
            finally:
                browser.close()
                browser.switch_to.window(safe_get_tab)

                conn.send(page_source)


def server_handler(address, authkey):
    serv = Listener(address, authkey=authkey)
    while True:  # server act like daemon
        try:
            client_conn = serv.accept()

            handler_client(client_conn)
        except Exception:
            import traceback; traceback.print_exc()


def handler_everything():
    server_handler(("", 15337), authkey=b"running_wait-time")


def main():
    def sigterm_handler(signo, frame):
        # close the connection - use global queue!!!!
        browser_bkup.quit()
        raise SystemExit("\nreceive 'Ctrl+C'/'kill -15'/SIGTERM, program stop!")
    signal.signal(signal.SIGINT, sigterm_handler)
    signal.signal(signal.SIGTERM, sigterm_handler)

    try:
        handler_everything()
    except Exception as e:  # 报告一切错误
        print("[Error] Exception: ", e, file=sys.stderr)


if __name__ == "__main__":
    main()

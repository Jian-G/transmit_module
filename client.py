import subprocess
import sys
import threading
from threading import Thread
import time
import logging

flag=0
stdout = sys.stdout()


def client():
    global flag
    PID=0
    with subprocess.Popen(["iperf3", "-c", "172.24.178.109"], stdout=subprocess.PIPE, universal_newlines=True) as process:
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                pass

                print(output.strip())


        rc = process.poll()
        time.sleep(2)
        flag = 1
        if flag ==1:
            print("client has shut")
            with subprocess.Popen(["netstat", "-ano|findstr","12000"], stdout=subprocess.PIPE, shell=True,universal_newlines=True) as process:
                        while True:
                            output = process.stdout.readline()
                            if output == '' and process.poll() is not None:
                                break
                            if output:
                                PID = output[-5:]
                                print(output[-5:])
            with subprocess.Popen("taskkill  /F /pid "+str(PID), stdout=subprocess.PIPE, shell=True,universal_newlines=True) as process:
                        while True:
                            output = process.stdout.readline()
                            if output == '' and process.poll() is not None:
                                break
                            if output:
                                print(output.strip())

            


if __name__ == "__main__":
    thread_client = Thread(target=client)
    thread_client.start()


import subprocess
import sys
import threading
from threading import Thread
import time
import logging

flag=0
stdout = sys.stdout


def client():
    global flag
    PID=0
    with subprocess.Popen(["iperf3", "-c", 
                            "172.24.178.109",
                            "-p", "5200",
                            "-F", "mix_weights.pt",
                            "-fM"], stdout=subprocess.PIPE, universal_newlines=True) as process:
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                pass

                print(output.strip())

if __name__ == "__main__":
    thread_client = Thread(target=client)
    thread_client.start()


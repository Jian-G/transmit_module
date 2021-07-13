import subprocess
import os,signal
import sys
from threading import Thread
import time
import core

model_list = []
param_list = []
tensor_list = []

stdout = sys.stdout
def server(save_path, port, interval="0"):
    with subprocess.Popen( ["iperf3", "-s", 
                            # "-F", save_path,
                            "-fM",
                            "-i", interval,
                            "--verbose",
                            "--logfile", save_path + ".log",
                            "-p", port],
                            stdout=subprocess.PIPE, universal_newlines=True) as process:
        print(process.pid)
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                print("server exit")
                break
            if output:
                with open(save_path + '/out.txt', 'w+') as file:
                    sys.stdout = file             
                    print(output.strip())

        # os.kill(process.pid, signal.SIGTERM)

def receive_check_loop(type):
    print(type)
    if type == "cloud":
        save_path = "data/receive/tensor/" + "receive.txt"
        thread_server = Thread(target=server, args=(save_path, core.EDGE_SENDTO_CLOUD, ))
        thread_server.start()
    elif type == "edge":
        save_path = "data/receive/model/" + "receive.pt"
        thread_server = Thread(target=server, args=(save_path, core.CLOUD_SENTTO_EDGE, ))
        thread_server.start()

if __name__ == "__main__":
        save_path = "data/receive/tensor/" + "receive.txt"
        thread_server = Thread(target=server, args=(save_path, core.EDGE_SENDTO_CLOUD, ))
        thread_server.start()

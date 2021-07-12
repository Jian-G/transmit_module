import subprocess
from threading import Thread
import time
import core

def server(save_path, port, interval="0"):
    with subprocess.Popen( ["iperf3","-s", 
                            "-F", save_path,
                            "-i", interval,
                            "--verbose",
                            "--logfile",save_path + '.log',
                            "-p", port],
                            stdout=subprocess.PIPE, universal_newlines=True) as process:
        while True:
            print("doing")
            time.sleep(1)
            output = process.stdout.readline()

            if output == '' and process.poll() is not None:
                break
            if output:
                pass


        rc = process.poll()

def receive_check_loop(type):
    if type == "cloud":
        save_path = "data/receive/tensor/" + "receive.txt"
        thread_server = Thread(target=server, args=(save_path, core.EDGE_SENDTO_CLOUD, ))
        thread_server.start()
    elif type == "edge":
        save_path = "data/receive/model/" + "receive.pt"
        thread_server = Thread(target=server, args=(save_path, core.CLOUD_SENTTO_EDGE, ))
        thread_server.start()


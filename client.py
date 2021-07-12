import subprocess
import sys
import glob
from threading import Thread
import core

model_dict = {}
param_dict = {}
tensor_dict = {}

stdout = sys.stdout



def client(filename, host, port, interval="0"):
    with subprocess.Popen( ["iperf3", "-c", host, 
                            "-F", filename,
                            "-i", interval,
                            "--verbose",
                            "--logfile", filename + ".log",
                            "-p", port],
                            stdout=subprocess.PIPE, universal_newlines=True) as process:
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                pass

                print(output.strip())

def send_check_loop(type):
    while(True):
        if type == "cloud":
            for filename in glob.glob(r'data/send/model/*.pt'):
                if(filename not in model_dict.keys()):
                    model_dict[filename] = 0
            for filename, status in model_dict.items():
                if status == 0:
                    print(filename)
                    file_path = filename
                    thread_client = Thread(target=client, args=(file_path, core.EDGE_HOST, core.CLOUD_SENTTO_EDGE, ))
                    thread_client.start()
                    model_dict[filename] = 1
        elif type == "edge":
            for filename in glob.glob(r'data/send/tensor/*.txt'):
                if(filename not in tensor_dict.keys()):
                    tensor_dict[filename] = 0
            for filename, status in tensor_dict.items():
                if status == 0:
                    print(filename)
                    file_path = filename
                    thread_client = Thread(target=client, args=(file_path, core.CLOUD_HOST, core.EDGE_SENDTO_CLOUD, ))
                    thread_client.start()
                    tensor_dict[filename] = 1


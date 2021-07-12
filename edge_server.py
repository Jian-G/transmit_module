import subprocess
from threading import Thread
import time
flag = 0
def server():
    global flag
    if flag == 1:
        return
    with subprocess.Popen(["iperf3","-s", "-F", "receive.pt"],stdout=subprocess.PIPE, universal_newlines=True) as process:
        while True:
            print("doing")
            time.sleep(1)
            output = process.stdout.readline()

            if output == '' and process.poll() is not None:
                break
            if output:
                pass


        rc = process.poll()

if __name__ == "__main__":
    thread_client = Thread(target=server)
    thread_client.start()

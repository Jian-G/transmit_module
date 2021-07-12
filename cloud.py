from threading import Thread
from client import send_check_loop
from server import receive_check_loop
import time

if __name__ == '__main__':
    cloud_server_thread = Thread(target=receive_check_loop, args=("cloud", ))
    cloud_client_thread = Thread(target=send_check_loop, args=("cloud", ))

    cloud_server_thread.start() 
    time.sleep(5)
    cloud_client_thread.start()

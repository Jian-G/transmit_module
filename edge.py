from threading import Thread
from client import send_check_loop
from server import receive_check_loop
import time

if __name__ == '__main__':
    edge_server_thread = Thread(target=receive_check_loop, args=("edge", ))
    edge_client_thread = Thread(target=send_check_loop, args=("edge", ))

    edge_server_thread.start() 
    time.sleep(5)
    edge_client_thread.start()

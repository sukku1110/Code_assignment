import platform
import sys
import time
import hashlib
from collections import defaultdict
import psutil
from threading import Thread
import pyshark


if platform.system() != 'Windows':
    print("This script can only be run on a Windows platform.")
    sys.exit(1)


hash_cache = defaultdict(lambda: {"timestamp": 0, "counter": 0})

def hash_executable(path):
    hasher = hashlib.sha256()
    try:
        with open(path, 'rb') as exe_file:
            buf = exe_file.read()
            hasher.update(buf)
    except FileNotFoundError:
        return None
    return hasher.hexdigest()

def capture_processes():
    while True:
        a = psutil.process_iter(['pid', 'name', 'exe'])
        for proc in psutil.process_iter(['pid', 'name', 'exe']):
            print(proc)

            try:
                path = proc.info['exe']
                if path:
                    hash_value = hash_executable(path)
                    if hash_value:
                        process_data = {
                            "name": proc.info['name'],
                            "path": path,
                            "hash": hash_value
                        }
                        handle_process(process_data)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        time.sleep(5)  

def handle_process(process_data):
    hash_value = process_data['hash']
    current_time = time.time()
    if hash_value in hash_cache:
        if current_time - hash_cache[hash_value]['timestamp'] < 60:
            hash_cache[hash_value]['counter'] += 1
            print(f"Duplicate process: {process_data['name']}, Count: {hash_cache[hash_value]['counter']}")
        else:
            hash_cache[hash_value]['timestamp'] = current_time
            hash_cache[hash_value]['counter'] = 1
            print(f"Process recaptured after 60 seconds: {process_data['name']}")
    else:
        hash_cache[hash_value]['timestamp'] = current_time
        hash_cache[hash_value]['counter'] = 1
        print(f"New process captured: {process_data['name']}")

def packet_handler(packet):
    print(f"Packet captured: {packet}")

def start_network_capture():
    capture = pyshark.LiveCapture(interface='your_network_interface')  # replace 'your_network_interface' with req network interface name
    capture.apply_on_packets(packet_handler, timeout=1000)


if __name__ == "__main__":
    process_thread = Thread(target=capture_processes)
    network_thread = Thread(target=start_network_capture)
    process_thread.start()
    network_thread.start()
    process_thread.join()
    network_thread.join()

import socket
import time
import random
import threading
import json

HOST = 'robins.ddns.net'
PORT = 53

def serverload(name):
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(3)
            try:
                print("information on leaederboard")
                s.connect((HOST, PORT))
                flag = b"pp,"
                s.sendall(flag)
                score = random.randint(1, 20)
                namescore = {'name': (name), 'score': (score)}
                namescore = json.dumps(namescore).encode("utf-8")
                s.sendall(namescore)
                print("sent better scores")
                leaderboardstats = s.recv(1024)
                print(leaderboardstats)
            except socket.timeout:
                TIMEDOUT = True
            time.sleep(0.5)

t1 = threading.Thread(target=serverload, args=("1234",))
t2 = threading.Thread(target=serverload, args=("12345",))
t3 = threading.Thread(target=serverload, args=("123456",))
t4 = threading.Thread(target=serverload, args=("1234567",))

t1.start()
t2.start()
t3.start()
t4.start()
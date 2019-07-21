from time import sleep
import requests
import socket
import sys

response = requests.get("http://proyectossbecorp.com/logs/access.log")
data = response.text

lines = data.split('\n')


host = "localhost"
port = 9998
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

while True:
    print("Started")
    conn, addr = s.accept()
    print('\nConnected by', addr)

    try:
        for i in range(len(lines)):
            conn.send(str(lines[i]+'\n').encode('utf-8'))

            sleep(5)
    except socket.error:
        print ('Error Occured.\n\nClient disconnected.\n')
        break
conn.close()
    
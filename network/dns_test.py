import socket
from typing import List


addr: str = "hankku.home.com"

try:
    result= socket.getaddrinfo(addr, 80)
    print(result)

except Exception as e:
    print("fail-getaddrifo:",e)
    try:
        result = socket.gethostbyname(addr)
    except Exception as e:
        print("fail gethostByname:",e)
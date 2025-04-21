import socket
from typing import List


addr: str = "cloud.internal.home"

try:
    result= socket.getaddrinfo(addr, 80)
    print("test:", result)

except Exception as e:
    print("fail-getaddrifo:",e)
    try:
        result = socket.gethostbyname(addr)
    except Exception as e:
        print("fail gethostByname:",e)
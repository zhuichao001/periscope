import socket

def hostip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except:
        ip = socket.inet_ntoa(fcntl.ioctl( s.fileno(), 0x8915, struct.pack('256s', 'eth0'))[20:24])
    finally:
        s.close()
    return ip

print(hostip())

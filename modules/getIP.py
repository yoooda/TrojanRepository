import socket
def run(**args):
    ip = socket.gethostbyname(socket.gethostname())
    if (ip != "127.0.0.1" and ip != None):
        print "[*] Obtained IP address %s" %ip
        return str(ip)
    return "UNABLE TO GET IP"
    
import socket
from IPy import IP

def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[------------ Scanning Target:  ' + str(target) +' ------------]')
    for port in range(1,100):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

def scan_port(ipAddress, port):
    try:
    # socket descriptor
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((ipAddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open Port '+str(port)+' | Banner: '+str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port ' + str(port))
    except:
        pass
# if is the main the program run this part of code
if __name__ == "__main__":
    targets = input('[+] Enter Target/s to scan (for multiple target with -->,<--): ')
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)
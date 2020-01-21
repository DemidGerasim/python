import subprocess

def check_ip_addresses(ip_address):
    ping_ok = []
    ping_not_ok = []

    for k in ip_address:
        reply = subprocess.run(['ping', '-n', '3', k],
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL)
        if reply.returncode == 0:
            ping_ok.append(k)
        elif reply.returncode == 1:
            ping_not_ok.append(k)
    return ping_ok, ping_not_ok

if __name__ == '__main__':
    ip = ['1.1.1.1', '8.8.8.8', '8.8.4.4', '8.8.7.1']
    result = check_ip_addresses(ip)
    print(f'Available IP: {result[0]} \nUnavailable IP: {result[1]}')
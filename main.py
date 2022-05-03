import time
import socket

line_banner = ("Cornell CYB 333 Project")
print(line_banner)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# This will ask for target's website or IP address to be scanned.
# Be responsible port scanning can be illegal if not used properly.
# Practice port scanning on hackthissite.org.
# Or practice scanning your local host: 127.0.0.1
target = input('Enter website or IP address to scan: ')

# This next line will display the initiation of the scan and the target IP address
target_ip = socket.gethostbyname(target)
print('Scanning target: ', target_ip)

# This line is the function for scanning the targeted port
def port_scan(port):
    try:
        s.connect((target_ip, port))
        return True
    except:
        return False


start = time.time()

# This line tells the code to scan: from port 0 to 7 & if they're open or closed
# Scanning 65,535 ports starting from 0, I'll be using 0-7 range
for port in range(7):
    if port_scan(port):
        print(f'port {port} is open')
    else:
        print(f'port {port} is closed')

end = time.time()
print(f'Time taken {end - start:.2f} seconds')

# This is a message for Prof. Scavotto from Morgan Cornell at the end 05/01/2022
line_banner1 = ("Thank you for all that you do!!:-)")
print(line_banner1)

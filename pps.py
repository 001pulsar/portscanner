import sys
import socket
from datetime import datetime

lengthCheck = len(sys.argv)
if (lengthCheck == 4):
    try:
        target = socket.gethostbyname(sys.argv[1])      # converts hostname to IP
        dots = target.count('.')
        if (dots == 3):     # cause 3 dots in an earthly ipv4
            exit
        else:
            print("\nInvalid IPv4 format received.\nExiting program.")
            sys.exit()
    except socket.gaierror:
        print("\nHost couldn't be resolved.")
else:
    print("\nInvalid arguments.\nSyntax: python3 pps.py <ip> <first_ip> <last_ip>\n")  # instructions for potatoes
    sys.exit()

# converting argv's by default string type items to integer to use with range()
first_port = int(sys.argv[2])
last_port = int(sys.argv[3]) + 1

print(f"\nStarting time: {datetime.now()}\n")

# had no plan to use "try" until planned to set custom commands for errors
try:        
    for port in range(first_port, last_port):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        connection_result = connection.connect_ex((target, port))
        if (connection_result == 0):
            print(f"{port} (status: open)")
        else:
            print(f"port {port}: CLOSED")
    
    print(f"\nEnding time: {datetime.now()}\n")

except KeyboardInterrupt:
    print("\nKeyboard interruption detected.\nExiting program.")

except socket.gaierror:
    print("\nHost couldn't be resolved.\nExiting program.")
    sys.exit()

except Exception as e:      # exception for all the rests of exceptions (just like war to end all wars)
    print(f"\nAn error occured: {str(e)}")
    sys.exit()

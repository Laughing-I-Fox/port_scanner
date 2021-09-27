import socket
import colorama


def scanner(ip, port):
    # TCP connect. AF_INET - protocols family, SOCK_STREAM - important for connection oriented protocols.
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # if connection filled:
    if client.connect_ex((ip, port)):
        pass
    # successful connection
    else:
        print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.RED + f"Port {port} is open!")


ip = socket.gethostbyname(input(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.GREEN +
                                "Please enter target domain name "))

# print target IP
print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.RED + "Target IP:", ip)

for i in range(int(input(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.GREEN +
                         "Please enter target port range "))):
    scanner(ip, i)

print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.RED + "Scan", ip, "finished!")

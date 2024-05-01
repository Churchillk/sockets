import socket, threading
from colorama import Fore, Style
from argparse import ArgumentParser

class server:
    def __init__(self, mac):
        self.mac = mac
        self.server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

    def __str__(self):
        return f"{self.mac}"
    
    def binding(self):
        try:
            self.server.bind((str(self.mac), 4)) #mac and chanell
            print(f"{Fore.GREEN}Bindinig was successful waiting for client")
            print("....")
            self.connection()

        except Exception as err:
            pass

    def connection(self):
        try:
            self.server.listen()
            self.client, self.address = self.server.accept()
            print(f"{Fore.GREEN} connection established at {self.address} {Style.RESET_ALL}")
        except Exception as err:
            print(Fore.RED, err, Style.RESET_ALL)

        sending_thread = threading.Thread(target=self.receive)
        receive_thread = threading.Thread(target=self.send)
        sending_thread.start()
        receive_thread.start()
    
    def receive(self):
        try:
            while True:
                self.data = self.client.recv(1024).decode("utf-8")
                if not self.data or self.data == "END":
                    self.client.close()
                    self.server.close()
                    break
                print(f"received >>{Fore.LIGHTYELLOW_EX} {self.data} {Style.RESET_ALL}")
        except Exception as err:
            print(Fore.RED, err, Style.RESET_ALL)

    def send(self):
        try:
            while True:
                print({Fore.CYAN})
                self.message = input(f"send >> ")
                self.client.sendall(self.message.encode("utf-8"))
                print(Style.RESET_ALL)
        except KeyboardInterrupt:
            self.client.close()
            self.server.close()

    
def main():
    parser = ArgumentParser()
    parser.add_argument("-m", "--mac", type=str, help="enter bluetooth address", required=True)
    return parser.parse_args()

if __name__ == "__main__":
    s = server(f"{main().mac}")
    s.binding()
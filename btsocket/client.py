import threading, socket
from colorama import Fore, Style
from argparse import ArgumentParser

class Client:
    def __init__(self, mac):
        self.mac = mac
        self.client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

    def __str__(self):
        return self.mac
    
    def connect(self):
        self.client.connect((str(self.mac), 4))
        print(f"{Fore.GREEN}Connected successfully {Style.RESET_ALL}")
        sending_thread = threading.Thread(target=self.receive)
        receive_thread = threading.Thread(target=self.send)
        sending_thread.start()
        receive_thread.start()

    def send(self):
        try:
            while True:
                print({Fore.CYAN})
                self.message = input(f"send >> ")
                self.client.sendall(self.message.encode("utf-8"))
                print(Style.RESET_ALL)
        except OSError:
            pass

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



def main():
    parser = ArgumentParser()
    parser.add_argument("-m", "--mac", type=str, help="enter bluetooth address", required=True)
    return parser.parse_args()

if __name__ == "__main__":
    Client(f"{main().mac}").connect()
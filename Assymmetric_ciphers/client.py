import pickle
import socket

from crypt_utils import Cryptographer, File_Cryptographer

HOST = '127.0.0.1'
PORT = 8089

def main():
    sock = socket.socket()
    sock.connect((HOST, PORT))

    p = 54
    g = 53
    a = 63

    diffie_hellman = Cryptographer(a=a, p=p, g=g)
    client_mixed_key = diffie_hellman.mixed_key
    private_key = diffie_hellman.generate_key(client_mixed_key)
    print(client_mixed_key)
    print(private_key)

    sock.send(pickle.dumps((p, g, client_mixed_key)))
    sock.close()

    sock = socket.socket()
    sock.connect((HOST, PORT))
    cryptographer = File_Cryptographer(private_key)
    result = cryptographer.encryption("test message")
    print(result)
    sock.send(pickle.dumps(result))

    result = cryptographer.encryption(result)
    print(result)

    sock.close()
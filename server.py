import pickle
import socket

from crypt_utils import Cryptographer, File_Cryptographer

HOST = '127.0.0.1'
PORT = 8089

'''Главная функция сервера'''
def main():
    sock = socket.socket()
    sock.bind((HOST, PORT))
    sock.listen(1)

    cryptographer = None
    while True:
        conn, addr = sock.accept()
        
        '''Получаем данные от клиента'''
        msg = conn.recv(4096)
        data = pickle.loads(msg)

        print("Data Type: ", type(data), " | Message = ", data)
        if type(data) == tuple:
            p, g, A = data

            diffie_hellman = Cryptographer(a=A, p=p, g=g)
            server_mixed_key = diffie_hellman.mixed_key
            private_key = diffie_hellman.generate_key(server_mixed_key)
            cryptographer = File_Cryptographer(private_key)
            print(server_mixed_key)
            print(private_key)

        elif type(data) == str:
            result = cryptographer.encryption(data)
            print("Decrypted message" + result)
        else:
            raise ValueError(f"Incorrect data type: {type(data)}")
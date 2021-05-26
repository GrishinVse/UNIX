# https://www.youtube.com/watch?v=vFjq9pID4-E&t=1s

    
'''
Данный класс позволяет шифровать файлы с помощью ключа (key)
:param message: исходное сообщение
:return: зашифрованное/расшифрованное сообщение
'''
class File_Cryptographer:
    def __init__(self, key: int):
        self.key = key

    def encryption(self, message: str) -> str:
        return "".join([chr(ord(message[i]) ^ self.key) for i in range(len(message))])

'''
Работает по алгоритму шифрования Диффи-Хеллмана
'''
class Cryptographer:

    def __init__(self, a: int, p: int, g: int):
        self._a = a
        self._p = p
        self._g = g

    '''Смешаный ключ'''
    def mixed_key(self):
        return self._g ** self._a % self._p
    
    '''Генератор приватного ключа'''
    def generate_key(self, mixed_key):
        return mixed_key ** self._a % self._p
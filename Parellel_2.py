#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing import Process, Queue, Pool
import math
import random

MTX1 = './files/mtx1.txt'
MTX2 = './files/mtx2.txt'
MTX_RES = './files/mtx_res.txt'

def element(index, A, B, queue):
    i, j = index

    res = 0
    
    # get a middle dimension
    N = len(A[0]) or len(B) 
    for k in range(N):
        res += A[i][k] * B[k][j]
    
    queue.put(res)  
    return res 

# Очищает строку от ненужных символов
def cleaner(string):
    return string.replace("[", "").replace("]", "").replace(" ", "").strip()

# Преобразует строку списка в список
def str_to_list(string):
    return [int(el.strip()) for el in cleaner(string).split(",")]

# Преобразует список в строку (матрицу)
def list_to_str(List):
    res = ""
    for el in List:
        res += str(el).strip() + "\n"
    
    return res

# Считывает матрицу из файла
def read_matrix(file_name):
    mtx_file = open(file_name, 'r')
    matrix = list()
    for el in [line.strip() for line in mtx_file]:
        matrix.append(str_to_list(el))

    mtx_file.close()

    print(matrix, type(matrix))

    n = math.ceil((math.sqrt(len(matrix))))
    print("Размер матрицы", n)

    return matrix

# Записывает матрицу в файл
def write_matrix(mtx, file_name = './files/mtx_res.txt'):
    mtx_file = open(file_name, 'w')
    mtx_file.write(list_to_str(mtx))

# Генерация матрицы
def matrix_gen(n, m):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(random.randint(1, 100))
    return matrix

# Генерация и запись матриц в файлы
def start_matrix():
    n = int(input("Введите кол-во строк в матрице : "))
    m = int(input("Введите кол-во столбцов в матрице : "))

    if (n > 1 and m > 1):
        matrix1 = matrix_gen(n ,m)
        matrix1 = matrix_gen(m ,n)

        write_matrix(matrix1, MTX1)
        write_matrix(matrix2, MTX2)

matrix1 = list()
matrix2 = list()

while True:
    command_input = input("****** МЕНЮ ******\n1. Загрузить матрицы из файла\n2. Создать новые данные матриц\n-> ")
    if (command_input.strip() == '1'):
        matrix1 = read_matrix(MTX1)
        print('/////////////////////////////')
        matrix2 = read_matrix(MTX2)
        break
    elif (command_input.strip() == '2'):
        start_matrix()

        matrix1 = read_matrix(MTX1)
        print('/////////////////////////////')
        matrix2 = read_matrix(MTX2)
    else:
        print("ERROR")

q = Queue()

D = len(matrix1[0]) or len(matrix2)
print("D = ", D)

res_matrix = list()

for i in range(0, D):
    loc = list()
    for j in range(0, D):
        p1 = Process(target=element, args=[(i, j), matrix1, matrix2, q])
        
        p1.start()
        p1.join()
        
        loc.append(q.get())        
        
        print("Res[ ",i , ", ", j, " ]= ", loc[len(loc)-1])
    res_matrix.append(loc)

print(res_matrix)
str_res = list_to_str(res_matrix)

print("********\n",str_res)

write_matrix(res_matrix, './files/mtx_res.txt')

#'./files/mtx2.txt'

q.close()
q.join_thread()





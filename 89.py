"""  # Opção 1
file = open('abc.txt', 'w+')  # w+ é ^L do arquivo
file.write('Row 1\n')
file.write('Row 2\n')
file.write('Row 3\n')

file.seek(0, 0)  # manda "cursor" para inicio do arquivo (1 é para onde esta e 2 para final, confirmar depois)
print('Lendo rows')
print(file.read())
print('###########')

file.seek(0, 0)
print(file.readline(), end='')  # end='' impede a quebra de linha automatica
print(file.readline(), end='')
print(file.readline(), end='')
print('###########')

file.seek(0, 0)
for row in file.readlines():
    print(row, end='')
print('###########')

file.seek(0, 0)
for letter in file.readline():
    print(letter)
print('###########')

file.seek(0, 0)
for row in file:
    print(row, end='')
print('###########')

file.close()
"""
"""  # opção com o Try
try:
    file = open('abc.txt', 'w+')
    file.write('Row')
    file.seek(0)
    print(file.read())
finally:
    file.close()
"""
""" open with with and r/a+
with open('abc.txt', 'w+') as file:  # file vai conter a função open
    file.write('Row 1\n')
    file.write('Row 2\n')
    file.write('Row 3\n')

    file.seek(0)
    print(file.read())

with open('abc.txt', 'r') as file:  # r abre o arquivo só pra ler
    print(file.read())

with open('abc.txt', 'a+') as file:  # a+ abre o arquivo de onde parou (não apaga)
    file.write('Outra linha\n')
    file.seek(0)
    print(file.read())
"""
"""
import os
os.remove('abc.txt')
"""

d1 = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': 25,
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 30,
    },
}

print(d1)  # dicionario normal (não sei oque é pq adiante essa aula pra ver utilização de arquivo)
import json
"""
d1 = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': 25,
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 30,
    },
}

d1_json = json.dumps(d1, indent=True)
with open ('abc.json', 'w+') as file:
    file.write(d1_json)
"""

with open('abc.json', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)  # transforma json em dicionário

for k, v in d1_json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)
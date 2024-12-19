'''
Elabore a função generatePassword(userName) que funciona como um gerador 
de passwords: a função deve receber um username, e em função desse nome 
deve gerar e devolver uma password que é constituída da seguinte forma: 

• Password consiste nos caracteres das posições pares do username, 
intercalados de um número aleatório entre 1 e 9 (inclusive). 
 
• A password termina com o nº de caracteres indicados no username 
 
Se  o  username  incluir  algum  espaço  a  função  deve  devolver  a  mensagem 
“username é inválido” em alternativa à password.
'''

import os
import random

# Limpa a consola
os.system("cls")

def generate_password(user_name):
    '''
    generatePassword(userName) que funciona como um gerador de passwords: a função deve receber um username
    '''
    nome_utilizador=""
    n=0
    if user_name.count(" ") != 0:
        print("Username inválido")
    else:
        for i in user_name:
            if n % 2 == 0:
                nome_utilizador+= f"{user_name[n]}{random.randint(1,9)}"
            n+=1
    return nome_utilizador

# Solicita o input do utilizador
user_name = input("Indique um username: ")
print(generate_password(user_name))
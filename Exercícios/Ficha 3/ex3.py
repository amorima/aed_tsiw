'''
Crie a função capicua(texto) que receba um texto como parâmetro de entrada 
e devolva True ou False, conforme o texto seja uma capicua ou não.  
 
Uma capicua consiste num texto que tanto pode ser lido da esquerda para 
a direita como da direita para a esquerda. 
 
 Exemplos de capicuas: osso, asa, ana, arara 
 
 Exemplos do uso da sua função capicua: 
capicua(‘osso’)  => devolve True 
capicua(‘roma’)  => devolve False 
 
 Conforme o valor devolvido pela função, deve depois indicar na consola 
se o texto inserido é uma capicua ou não.
'''

def capicua(texto):
    texto=texto.lower()
    inv=""
    caracteres=len(texto)
    for i in range(caracteres-1, -1, -1):
        inv+=texto[i]
    
    if texto==inv:
        return True
    else:
        return False

texto=str(input("Indique um texto: "))
if capicua(texto)==True:
    print(f"{texto} é capicua")
else:
    print(f"{texto} não é capicua")
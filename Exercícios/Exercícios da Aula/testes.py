try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

ValueError - Ocorre quando uma função recebe um argumento de tipo correto, mas com um valor inapropiado (exemplo: tentar converter uma string não numérica para inteiro).

TypeError - Ocorre quando uma operação é realizada em um tipo de dado inadequado (exemplo: tentar somar uma string e um número).

IndexError - Ocorre quando se tenta acessar um índice de uma lista ou sequência que não existe (exemplo: acessar um índice fora do intervalo da lista).

KeyError - Ocorre quando se tenta acessar uma chave que não existe em um dicionário.

FileNotFoundError - Ocorre quando se tenta abrir um arquivo que não existe no caminho especificado.

ZeroDivisionError - Ocorre quando se tenta dividir um número por zero.

AttributeError - Ocorre quando se tenta acessar ou chamar um método ou atributo em um objeto que não possui tal método ou atributo.

ImportError - Ocorre quando a importação de um módulo ou parte de um módulo falha (exemplo: o módulo não existe ou não pode ser encontrado).

NameError - Ocorre quando se tenta acessar uma variável ou nome que não foi definido.

TimeoutError - Ocorre quando uma operação ultrapassa o tempo limite estabelecido, geralmente em operações de rede ou I/O.
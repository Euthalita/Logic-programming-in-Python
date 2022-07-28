'''
produtos = []
produtos.append(('produto1',20))
produtos.append(('produto2',30))
lista = sum([x for y,x in produtos])

lista=[]
for x,y in produtos:
    lista.append(y)

print(sum(lista))
'''
lista=[1,4,6,8]

def multiplicasion(x,y=2):
    return x*y

def potension(x,y=3):
    return x**y

novo=[multiplicasion(i) for i in lista ]
novu =[potension(i) for i in lista]


num = [i if i != 6 else 600 for i in lista]

siglas = ['SP','RJ','GO']
estados = ['São Paulo','rio de janeiro', 'goias']

juncao = list(zip(siglas,estados))

def func(nome):
    return f'Oi {nome}'
def fun1(nome, saudacao='Bom dia'):
    return f'{nome} {saudacao}'

func('Alana')
var = fun1(func)
#print(var)

def funtotal(one):
    return f' Esse é o resultado: {one}'

alunos = [
{'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'}
]
def ordena(item):
  return item['nota']


alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)
print(alunos_agrupados)
for agrupamento, valores_agrupados in alunos_agrupados:
  valores = list(valores_agrupados)
  print(f'Agrupamento: {agrupamento}')
  for aluno in valores:
    print(f'\t{aluno}')
  quantidade = len(valores)
  print(f'\t{quantidade} alunos tiraram nota {agrupamento}')
#notas = groupby(alunos, ordenado)

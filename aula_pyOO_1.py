############
# Funcional e OO
# Prof. Neylson
# Gerson Vasconcelos Neto
# aula 1 - python
###########

5 + 5  # análogo ao R
5 - 6
5 * 2
5 / 2 
5 ** 2 # potencia
5 % 2 # resto da divisão
5 // 2 # quociente inteiro da divisão

######
# criando objetos e realizando operações
x = 6
print(x)

y = 8.5

x + y
x - y
x / y
x * y
x ** y 
x // y
x % y

x ** (1/2)

##########
# tipo de dados

type(x)
type(y)

nome = 'Neylson'
sobrenome = 'Crepalde'

print(nome)
print(sobrenome)

type(nome)

nome + sobrenome  # juntar
nome + ' ' + sobrenome # juntar com espaço

x == 5  # retorna booleanos
x < 5
x > 5

###########
### estruturas de dados no PY

# listas e dicionarios

nomes = ['Neylson', 'Gerson', 'Layla',
         'Bia']

type(nomes)

len(nomes)   # tamanho do objeto

nomes[0]  # indice comeca no 0, diferente do R que começa no 1

nomes.append('Adelvan')   # adiciona esse elemento ao FINAL da lista

nomes.pop(0)  # retira elemento da lista

nomes.insert(0, 'Edésio')  # adciona elemento no índice desejado

# nomes[2] = 'Edésio' iria sobrescrever o elemento 2
print(nomes)

## slice

nomes[:3]  # fatiou do começo ao 3   (intervalo aberto no fim)
nomes[1:] # fatiou do 2 até o final
nomes[1:-1] # fatiou do 2 até o penultimo

nomeCompleto = 'Neylson Crepalde'

nomeCompleto[:7]
nomeCompleto[8:]
nomeCompleto[8:-3]

idade = 31

nomeCompleto + ' tem ' + str(idade) + \
' anos.'   # quebra de linha no código usa \

print(nomeCompleto + ' tem\n ' + str(idade) + \
' anos.')  # quebra de linha no texto

## dicionarios
# {'key' : 'value'}

alunos = {'nome': 'Gerson',
          'idade': 27,
          'curso': 'CD',
          'natural': 'Recife'}

print(alunos)
alunos['nome']   #chama a key e retorna o value
alunos['natural']

alunos = {'nome': ['Gerson', 'Layla'],    # posso usar uma lista dentro
          'idade': [27, 23],
          'curso': ['CD', 'CD'],
          'natural': ['Recife', 'Maceio']}

alunos['idade'][0]   # idade do 1º aluno

alunos.keys()   # retorna as chaves do dct
alunos.values() # retorna os valores do dct

alunos['bomAluno'] = True

alunos['bomAluno']

## dct da turma

funcionalOO = {'alunos': ['Gerson','Layla',
                          'Bia', 'Adelvan', 
                          'Warley', 'Ester',
                          'Vanessa', 'Marcos',
                          'Juliany', 'Nelson',
                          'Edésio', 'Numiá'],
'professor': 'Neylson Crepalde',
'sala': 2204,
'quantidade de computadores': 25,
'cursos': ['CD', 'BioInfo'],
'IES': 'IMIH'}



# investigar o objeto
type(funcionalOO)
funcionalOO.keys()  # mostrou as chaves
funcionalOO['professor']
len(funcionalOO['alunos']) #quantidade de alunos

#---

listaAlunos = funcionalOO['alunos']
print(listaAlunos)

funcionalOO['alunos'] = {
        'nomes': listaAlunos,
        'id': list(range(1, 13)),
        'idades': [25,26,27,25,26,26,27,23,25,
                   30,21,22]}

funcionalOO.keys()

funcionalOO['alunos']['id']












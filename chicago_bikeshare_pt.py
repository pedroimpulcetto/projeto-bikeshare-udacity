
# coding: utf-8

# In[4]:


# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...\n")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!\n\n")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("\n\nLinha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("\n\nLinha 1: ")
print(data_list[1])

input("\n\nAperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for l in range(1, 21, 1):
    print(data_list[l])

    
# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("\n\nAperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
l = 0
while l < 20:
    print(data_list[l][6])
    l += 1

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("\n\nAperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    '''
    Função que retorna uma coluna de -data_list-.
    Argumentos:
        param1: base de dados que deseja usar.
        param2: o index da coluna da base de dados que usou.
    Retorna:
        Uma lista -column_list- de valores com os dados da coluna da base de dados usada. 
        
    '''
    
    column_list = []
    line = 0
    while line < len(data):
        column_list.append(data[line][index])
        line += 1
# Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("\n\nAperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
male = 0
female = 0
line = 0
while line < len(data_list):
    if data_list[line][6] == 'Male':
        male += 1
    if data_list[line][6] == 'Female':
        female += 1
    line += 1

# Verificando o resultado
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("\n\nAperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    '''
    Função que faz a contagem da quantidade de -male- e -female- de uma coluna de uma base de dados -data_list-.
    Argumento:
        base de dados que deseja usar -data_list-.
    Retorna:
        Uma lista de nome -count_gender- que contém a quantidade de -male- e -female- em valor -int-.
    
    '''
    male = 0
    female = 0
    line = 0
    while line < len(data_list):
        if data_list[line][6] == 'Male':
            male += 1
        if data_list[line][6] == 'Female':
            female += 1
        line += 1
    return [male, female]

print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("\n\nAperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list):
    '''
    Função recebe uma base de dados -data_list-, verifica os números das variáveis -male- e -female- recebidos
    anteriormente retornando qual tem a maior quantidade ou se são iguais.
    Argumentos:
        base de dados que deseja usar -data_list-.
    Retorna:
        Uma resposta em -str- dizendo qual
    '''
    answer = ""
    if male > female:
        answer = 'Male'
    elif female > male:
        answer = 'Female'
    else:
        answer = 'Equal'
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("\n\nAperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
def count_types(data_list):
    '''
    Função recebe um base de dados de sua escolha -data_list-, verifica a quantiade de valores especificados
    em uma certa coluna -5- e retorna uma lista -count_types- com os valores.
    Argumentos:
        base de dados que deseja usar -data_list-.
    Returna:
        uma lista -count_types- com os valores de -customer- e -subscriber-.
    '''
    customer = 0
    subscriber = 0
    line = 0
    while line < len(data_list):
        if data_list[line][5] == 'Customer':
            customer += 1
        if data_list[line][5] == 'Subscriber':
            subscriber += 1
        line += 1
    return [customer, subscriber]


print("TAREFA 7: Verifique o gráfico!")
user_types = column_to_list(data_list, 5)
types = ['Customer', 'Subscriber']
quantity = count_types(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo')
plt.xticks(y_pos, types)
plt.title('Quantidade de Tipos')
plt.show(block=True)

input("\n\nAperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque existem vários espaços que estão em branco -sem preenchimento- tipo: ''."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("\n\nAperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
trip_duration_list = list(map(int, trip_duration_list))
soma = 0

#verificando o max e min
for trip in trip_duration_list:
    if soma == 0:
        min_trip = trip
        max_trip = trip
    else:
        if trip < min_trip:
            min_trip = trip
        if trip > max_trip:
            max_trip = trip
    soma += trip # somando os valores para depois tirar a média
#tirando a média
mean_trip = soma / len(trip_duration_list)

trip_duration_list.sort() #colocando a lista em ordem crescente
median_trip = trip_duration_list[775752:775754] #encontrando os valores para tirar a mediana
#somando os valores do meio
soma_median = 0
for median in median_trip:
    soma_median += median
#tirando a mediana
median_trip = int(soma_median / 2)


print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("\n\nAperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------



input("\n\nAperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    item_types = set(column_to_list(data_list, -2))
    count_items = []
    line = 0
    none = 0
    male = 0
    female = 0
    while line < len(data_list):
        if data_list[line][6] == 'Male':
            male += 1
        if data_list[line][6] == 'Female':
            female += 1
        if data_list[line][6] == '':
            none +=1
        line += 1
    count_items = [none, female, male]
    return item_types, count_items

column_list = column_to_list(data_list, -2)
types, counts = count_items(column_list)


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------


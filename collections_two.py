users_data_sciencie = [15, 23, 43, 56]
users_machine_learm = [13, 23, 56, 43]

watching = users_data_sciencie.copy()
print(f"Lista copiada: {watching}")
watching.extend(users_machine_learm)
print(f"lista extendida {watching} e seu tamanho é {len(watching)}")
# remover elementos iguais usando conjunto
watching = set(watching)
print(f"lista em conjunto {watching} e o seu tamanho é {len(watching)}")


users_data_sciencie = {15, 23,  56}
users_machine_learm = {13, 23, 56, 43}

print(users_data_sciencie & users_machine_learm) # intercessão / subtração
print(users_data_sciencie | users_machine_learm) # soma/uniao

do_ds_not_do_ml = users_data_sciencie - users_machine_learm
print(do_ds_not_do_ml) # apenas o que forem diferente de data science
print(15 in do_ds_not_do_ml)

donot_ds_and_donot_lm = users_data_sciencie ^ users_machine_learm # ou exclusivo
print(donot_ds_and_donot_lm )


# trabalhando com mais conjuntos

users = {1, 5, 76, 34, 52, 13, 17}
print(len(users))
users.add(13)
print(len(users))
users.add(765)
print(len(users))
print(users)

users_immutable = frozenset(users)
print(users_immutable)
print(type(users_immutable))


my_text = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
my_text_breaked = set(my_text.split())
print(my_text_breaked)


# Usando dicionários

appearances = {
    "Guilherme": 1,
    "cachorro": 2,
    "nome": 2,
    "vindo": 1
}

print(type(appearances))

# obtendo o valor do dicinário pelo seu nome
print(appearances["Guilherme"])
print(appearances["cachorro"])
# print(appearances["XPTO"]) ocorre um erro ao tentar buscar esse dado
# para evitar

print(appearances.get("xpto", 0)) # caso não encontre a chave retorne a valor 0


# criando um dicinário de outra maneira

appearances = dict(Guilherme = 2, cachorro = 1)
print(appearances)


# adicionando novo elemento
appearances["Rodrigo"] = 2

# substituir o valor
appearances["Guilherme"] = 4

print(appearances)

# remover um elemento
del(appearances["Rodrigo"])

print(appearances)

print(f"Existe rodrigo no dicinário: {'Rodrigo' in appearances}")
print(f"Existe rodrigo no dicinário: {'Guilherme' in appearances}")


for element in appearances:
    print(element)


# somente a chaves
for element in appearances.keys():
    print(element)


# somente valores
for element in appearances.values():
    print(element)


# verificando se existe um valor no dicionário
print(1 in appearances.values())


# chave valor
for element in appearances.keys():
    print(element, appearances[element])

# ou

for element in appearances.items():
    print(element)

# ou separando
for key, value in appearances.items():
    print(key, "=", value)


# criando uma palavra\\

print(["Palavra {}".format(key) for key in appearances.keys()])

my_text = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
my_text = my_text.lower()

# contando palavras com um dicionário
appearances = {}
for word in my_text.split():
    yet = appearances.get(word, 0)
    appearances[word] = yet + 1

print(appearances)





users_data_sciencie = [15, 23, 43, 56]
users_machine_learm = [13, 23, 56, 43]

watching = users_data_sciencie.copy()
print(f"Lista copiada: {watching}")
watching.extend(users_machine_learm)
print(f"lista extendida {watching} e seu tamanho é {len(watching)}")
# remover elementos iguais usando conjunto
watching = set(watching)
print(f"lista em conjunto {watching} e o seu tamanho é {len(watching)}")


users_data_sciencie = {15, 23, 43, 56}
users_machine_learm = {13, 23, 56, 43}

print(users_data_sciencie & users_machine_learm) # intercessão / subtração
print(users_data_sciencie | users_machine_learm) # soma/uniao
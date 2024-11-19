tupla = ("Cácia", 34, 1.65, True, "viajar")

print(tupla)
print(type(tupla))

lista = list(tupla)

print(lista)
print(type(lista))

lista.append("Adora viajar")
print(lista)

lista.pop(0)
lista.pop()
print(lista)

print(lista[0])

if len(lista)>1:
    print(f"A quantidade de dados são: {len(lista)} e os dados são: {lista}")
else:
    print(f"A quantidade de dado está incorreta!")

dicionario = {
    'nome': 'Cácia',
    'idade': 34,
    'comida favorita': 'Doces'
}

for valor in dicionario.values():
    print(valor)

tupla = ("carro", "moto", "bicicleta", "skate", "bola")
print(tupla)
print(type(tupla))

lista = ["carro", "moto", "bicicleta", "skate", "bola"]
print(lista)
print(type(lista))


for brinquedos in lista:
    print (f"os elementos contidos na lista são: {brinquedos}")


def add_fruta(a, b):
    lista.append(a)
    lista.append(b)
    print(lista)

def del_fruta():
     lista.pop()
     print(lista)

     for x in lista:
          print(f"este brinquedo está na lista{x}")




     




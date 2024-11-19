lista = ['banana' , 'maça', 'uva']



def add_fruta(a, b):
    lista.append(a)
    lista.append(b)
    print(lista)

add_fruta("abacate","sorvete")

def del_fruta():
     lista.pop()
     print(lista)

     del_fruta()

     for x in lista:
          print(f"esta fruta está na lista{x}")



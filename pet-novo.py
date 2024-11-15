nomePet = str(input("Olá, caro cliente, qual é o nome do seu pet?"))
idadePet = int(input("Qual é a idade do seu cachorro? responda apenas com números reais:"))
portePet = int(input("Qual é o porte do seu pet? por favor digite 1 para grande, 2 para médio, 3 para pequeno:"))
qtdBanho = int(input("No último ano, quantas vezes ele tomou banho com a gente? responda apenas com números reais:"))

if portePet == 1: print(input(f"obrigado caro cliente, a idade humana do {nomePet} é igual a {idadePet*7} e nos últimos 12 meses ele nos visitou {qtdBanho} e o lucro foi de {qtdBanho*(75-20)}."))
elif portePet == 2: print(input(f"obrigado caro cliente, a idade humana do {nomePet} é igual a {idadePet*7}e nos últimos 12 meses ele nos visitou {qtdBanho} e o lucro foi de {qtdBanho*(60-15)}."))
elif portePet == 3: print(input(f"obrigado caro cliente, a idade humana do {nomePet} é igual a {idadePet*7} tigrao e nos últimos 12 meses ele nos visitou {qtdBanho} e o lucro foi de {qtdBanho*(50-5)}."))



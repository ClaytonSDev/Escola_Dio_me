nome = "Clayton"
idade = 44
profissao = "Programador"
Linguagem = "Python"
saldo = 45.435

dados = {"nome": "Clayton", "idade": 44, "Saldo": 45.435}

print("nome: %s idade: %d " % (nome, idade)) # essa forma nao se utiliza mais
print("nome: {} idade: {}" .format(nome, idade)) # essaforma nao se utiliza mais tambem
print("nome: {1} idade: {0}" .format(idade, nome))
print("nome: {1} idade: {0} nome: {1} {1}".format(idade, nome))
print("nome: {nome} idade: {idade}".format(nome=nome, idade=idade))
print("nome: {nome} idade: {idade}".format(**dados))
print(f"nome: {nome} idade: {idade}")
print(f"nome: {nome} idade: {idade} saldo: {saldo:10.2f}")
print(f"nome: {nome} idade: {idade} saldo: {saldo:.2f}")
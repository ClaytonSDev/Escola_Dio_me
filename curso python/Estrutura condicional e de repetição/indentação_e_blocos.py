saldo = 1500
dep = 2000

print(saldo + dep)

saldoatual = (saldo + dep)

print(saldoatual)


def sacar(saldoatual):
    saque = 500

    if saque >= saldoatual:
        print("valor sacado")
        print("retire o seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente")



def depositar(valor):
    saldo = 500
    saldo += valor


sacar(100)
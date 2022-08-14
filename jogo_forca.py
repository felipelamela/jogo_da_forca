from funcao import *

palavra_escolhida = palavra()
palavra_secreta = []
for letra in palavra_escolhida:
    palavra_secreta.append('_ ')

####################  Tentativas ######################
while True:
    print()
    tentativas = tentativa(input("""Escolha sua  dificudalde:

[1] -> Fácil
[2] -> Médio
[3] -> Difícil
[4] -> Impossível

Digite aqui: """))
    if type(tentativas) == int:
        break
    else:
        print()
        print('Você precisa digitar um numero valido!')
########################  Jogo ########################
while True:
    if '_ ' in palavra_secreta:
        print()
        print(palavra_secreta)
        print()
        print(f"Numero de Tentativas: {tentativas}")
        print()
        letra_digitada = input('Digite uma letra: ').upper()


        if tentativas > 0:
            if not letra_digitada.isnumeric():
                if letra_digitada in palavra_escolhida:
                    for i in range(len(palavra_escolhida)):
                        if letra_digitada == palavra_escolhida[i]:
                            palavra_secreta[i] = letra_digitada
                else:
                    print(f"Palavra secreta não possui a letra '{letra_digitada}")
                    tentativas -= 1
            else:
                print(f"você não pode digitar numeros!")
                tentativas -= 1
        else:
            print(f'Suas tentativas acabaram!')
            print(f"A palavra secreta era '{palavra_escolhida}'.")
            break

    else:
        print()
        print(f"""Parabens você descobriu a palavra secreta:
        {palavra_secreta} ! """)
        break
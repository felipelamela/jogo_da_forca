def palavra():
  from random import randint

  lista_de_palavra = ['Bola', 'Peixe', 'Basquete', 'Tesoura', 'Sapo', 'Colher', 'Martelo', 'Pinguim', 'Promotor', 'Dentro', 'Colar', 'Formigueiro', 'Morango', 'Cercado', 'Meses', 'Hipnotizar', 'Silicone', 'Ecologia', 'Galo', 'Funil', 'Bateria', 'Profissional']

  rand_num = randint(0,len(lista_de_palavra)-1)
  palavra_escolhida = lista_de_palavra[rand_num].upper()
  return palavra_escolhida


def tentativa(numero=2):
    tentativas = numero
    try:
        tentativas = int(tentativas)
        if 1 <= tentativas <= 4:
            if tentativas == 1:
                tentativas = 15
                return tentativas

            elif tentativas == 2:
                tentativas = 10
                return tentativas

            elif tentativas == 3:
                tentativas = 7
                return tentativas

            elif tentativas == 4:
                tentativas = 3
                return tentativas

    except ValueError:
        return 'Você precisa digitar um numero valido!'

if __name__ == '__main__':

    valor = tentativa(input("Digite uma tentativa: "))

    print(type(valor))
 
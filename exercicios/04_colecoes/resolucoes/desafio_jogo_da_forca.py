from random import randrange

import unidecode


def imprimir_boas_vindas():
  print('*' * 80)
  print('Boas-vindas ao jogo da forca!'.upper())
  print('*' * 80)


def selecionar_opcao():
  print('Digite uma das opções abaixo:')
  print('[1] Jogar')
  print('[2] Cadastrar palavra')
  print('[0] Encerrar o programa')
  escolha = int(input('>>> '))
  return escolha


def obter_banco_palavras():
  return list()


def gerar_palavra_secreta(lista_palavras: list) -> str:

  if len(lista_palavras) > 0:
    indice_randomico_palavra = randrange(start=0, stop=len(lista_palavras))
    return unidecode.unidecode(lista_palavras[indice_randomico_palavra])
  else:
    print('*' * 80)
    print("O banco de palavras está vazio!")
    print('*' * 80)


def mascarar_palavra_secreta(palavra_secreta):
  return ['_' for letra in palavra_secreta]  # compreensão de lista


def dar_palpite():
  palpite = input('Qual seu palpite?: ').strip().upper()
  return palpite


def verificar_palavra_completa(palpite, palavra_secreta):
  return palpite == palavra_secreta
  # TODO: implementar uma funcionalidade para, caso o usuário digite a palavra completa, dê como vitória


def verificar_vitoria(palavra_secreta_mascarada):
  return '_' not in palavra_secreta_mascarada


def verificar_derrota(numero_erros, palavra_secreta):
  return numero_erros == len(palavra_secreta)


def imprimir_mensagem_vitoria():
  print('*' * 80)
  print("Parabéns, você ganhou!".upper())
  print("       ___________      ")
  print("      '._==_==_=_.'     ")
  print("      .-\\:      /-.    ")
  print("     | (|:.     |) |    ")
  print("      '-|:.     |-'     ")
  print("        \\::.    /      ")
  print("         '::. .'        ")
  print("           ) (          ")
  print("         _.' '._        ")
  print("        '-------'       ")


def imprimir_mensagem_derrota(palavra_secreta):
  print('*' * 80)
  print("Você perdeu!".upper())
  print("A palavra era {}".format(palavra_secreta).upper())
  print("    _______________         ")
  print("   /               \       ")
  print("  /                 \      ")
  print("//                   \/\  ")
  print("\|   XXXX     XXXX   | /   ")
  print(" |   XXXX     XXXX   |/     ")
  print(" |   XXX       XXX   |      ")
  print(" |                   |      ")
  print(" \__      XXX      __/     ")
  print("   |\     XXX     /|       ")
  print("   | |           | |        ")
  print("   | I I I I I I I |        ")
  print("   |  I I I I I I  |        ")
  print("   \_             _/       ")
  print("     \_         _/         ")
  print("       \_______/           ")


def cadastrar_nova_palavra(lista_palavras):
  nova_palavra = input(
    'Digite uma nova palavra para cadastrar na base de dados: ').upper()
  lista_palavras.append(nova_palavra)


def encerrar_jogo():
  print('Programa encerrado!'.upper())
  exit(0)


imprimir_boas_vindas()


def jogar():
  lista_palavras = list()

  while True:

    opcao_escolhida = selecionar_opcao()

    while opcao_escolhida not in [0, 1, 2]:
      print('Opção inválida!')
      opcao_escolhida = selecionar_opcao()

    if opcao_escolhida == 1:

      acertou = False
      enforcou = False
      numero_erros = 0

      palavra_secreta = gerar_palavra_secreta(lista_palavras)

      if palavra_secreta:
        palavra_secreta_mascarada = mascarar_palavra_secreta(palavra_secreta)

        palpites_errados = list()
        palpites_corretos = list()
        quantidade_palpites_dados = 0
        while not acertou and not enforcou:

          print(f'\n{palavra_secreta_mascarada}')

          palpite = dar_palpite()

          if palpite in palavra_secreta:
            if palpite in palpites_corretos:
              print(f'Você já usou {palpite} como palpite!')
            else:
              index = 0
              for letra in palavra_secreta:
                if palpite == letra:
                  quantidade_palpites_dados += 1
                  palpites_corretos.append(letra)
                  palavra_secreta_mascarada[index] = palpite
                index += 1
          else:
            if palpite in palpites_errados:
              print(f'Você já usou {palpite} como palpite!')
            else:
              numero_erros += 1
              quantidade_palpites_dados += 1
              palpites_errados.append(palpite)
              print(
                f'Você ainda possui {len(palavra_secreta) - numero_erros} chances!'
              )

          acertou = verificar_vitoria(palavra_secreta_mascarada)
          enforcou = verificar_derrota(numero_erros, palavra_secreta)
        if acertou:
          imprimir_mensagem_vitoria()
        else:
          imprimir_mensagem_derrota(palavra_secreta)
      else:
        print("A palavra não foi definida!")
    elif opcao_escolhida == 2:
      cadastrar_nova_palavra(lista_palavras)
    else:
      encerrar_jogo()

jogar() # invocação da função jogar(), que contém todas as demais funções e, consequentemente, toda a rotina do jogo

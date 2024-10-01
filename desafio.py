
import random
lista_sinais = ['pedra', 'papel', 'tesoura']

# DECIDI  USAR FUNÇÕES PARA DEIXAR O CODIGO MAIS LEGÍVEL

# FUNÇÃO QUE EXIBE O PLCAR E O TOTAL DE PARTIDAS
def placar(contadorM , contadorU,total): 
  print('---------- PLACAR ----------')
  print('PONTOS MÁQUINA: ', contadorM)
  print('PONTOS USUÁRIO: ', contadorU)
  print('\nTOTAL DE PARTIDAS JOGADAS: ',total)


# A EXECUÇÃO DO JOGO É FEITA AQUI
def execucao_jogo(contadorM, contadorU):# AQUI
  total = 0
  while(True):
    print('\nEscreva qual sinal você deseja seguido de enter: Pedra, Papel ou Tesoura? Para sair e abandonar o jogo digite 0\n')
    sinalU = input()
    if sinalU.lower() in lista_sinais: # OBRIGANDO AO USUÁRIO DIGITAR UM PALAVRA DA LISTA, CASO NÃO, O PROGRAMA PEDE PRA DIGITAR MAIS UMA VEZ
     total += 1
     sinalM = random.choice(lista_sinais)
     print('\nO sinal escolhido por mim foi: ', sinalM)
     if sinalU.lower() == sinalM.lower():
      print('\nSenhoras e senhores temos um empate!!!\n')
      print('Nenhum dos dois levam pontos\n')
     else:
      if (sinalU.lower() == 'pedra' and sinalM.lower() == 'tesoura') or (sinalU.lower() == 'tesoura' and sinalM.lower() == 'papel') or (sinalU.lower() == 'papel' and sinalM.lower() == 'pedra'):
            contadorU += 1
            print('\nPONTO PARA VOCÊ !!!!\n')
      elif (sinalM.lower() == 'pedra' and sinalU.lower() == 'tesoura') or (sinalM.lower() == 'tesoura' and sinalU.lower() == 'papel') or (sinalM.lower() == 'papel' and sinalU.lower() == 'pedra'):
            contadorM += 1
            print('\nPONTO PARA MIM !!!!\n')  
     placar(contadorM,contadorU,total)          
    elif sinalU == '0':
      break
    else:
      print('\nPalavra inválida, tente novamente !\n')
    

# INICIO DO PROGRAMA
while(True):
  print('\n--------> BEM VINDO AO TORNEIO DE JOKENPO <--------\n')
  print('Digite o número de acordo com  opção que você deseja e em seguida aperte enter: \n') 
  print('1 - Começar nova partida\n')
  print('0 - sair do jogo\n')

  opcao = input()

  if opcao == '0':
    print('\nOBRIGADO, VOLTE SEMPRE')
    break
  elif opcao == '1':
    print('\nComeçando.....\n')
    execucao_jogo(contadorM=0,contadorU=0)    
  else:
    print('\nOpção inválida, tente novamente\n')

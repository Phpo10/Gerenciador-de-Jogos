import time

#variável para deixar o código mais "bonito".
linha = "-" * 20 

#variáveis para escolha e contar os jogos registrados.
esc = 10
gamecont = 0

#lista para os jogos e as notas registradas.
listagame = []
listanota = []

#loop com escolha do usuário de sair.
while esc != 0:
    if esc == 10:
        print(f"{linha}""Gerenciador de Jogos"f"{linha}")
        esc = int(input("Escolha uma das opções abaixo: \n[1] Avaliar um jogo\n[2] Verificar os jogos salvos\n[3] Remover um jogo da lista\n[4] Atualizar a nota de um jogo\n[0] Sair\nEscolha: "))
        print(linha * 2)

    #escolha para os jogos e suas notas.
    elif esc == 1:

        #escolhe o nome do jogo, adiciona na lista de jogos e conta o tanto de jogos que foi colocado.
        game = input("Diga o nome de um game: ")
        listagame.append(game)
        gamecont = gamecont + 1

        #notas para o jogo
        nota1 = int(input("Gráficos: "))
        nota2 = int(input("Jogabilidade: "))
        nota3 = int(input("História: "))
        nota4 = int(input("Trilha Sonora: "))

        #calcula a media e coloca na lista de media.
        media = (nota1 + nota2 + nota3 + nota4) / 4
        listanota.append(media)
        esc = 10
    
    #verifica se tem jogos salvos ou não 
    elif esc == 2:
        if gamecont > 0:
            print("Jogos salvos:")
            #mostra a pocisão, o nome e a média dos jogos dito pelo usuário.
            for i, (game, media) in enumerate(zip(listagame, listanota), 1):
                print(f"[{i}] {game}, nota: {media:.2f}")
            esc = 10
        else:
            print("Nenhum jogo salvo ainda. Por favor, insira um jogo antes.")
            esc = 10
    
    #remove um jogo colocado na lista de jogos pelo usuário.
    elif esc == 3:
        if gamecont >= 1:

            #mostra os jogos salvos no momento e a númeração deles, para o usuário saber qual jogo estará removendo.
            print("Jogos salvos: ")
            for i, game in enumerate(listagame, 1):
                print(f"[{i}] {game}")
            print(linha * 2)
            rem = int(input("Digite o número do jogo para removê-lo da lista: "))

            #verifica se o rem(remover) está entre o 1 e o gamecont.
            if 1 <= rem <= gamecont:
                listagame.pop(rem - 1)
                listanota.pop(rem - 1)
                gamecont -= 1
                print("Jogo removido com sucesso!")
                esc = 10
            else:
                #um loop até o usuário colocar uma escolhada válida
                while True:
                    print(linha * 2)
                    print("Escolha não reconhecida.")
                    esc2 = int(input("O que deseja fazer:\n[1] Voltar para o menu\n[2] Retomar a remoção de jogo\nEscolha: "))
                    if esc2 == 1:
                        print("Retornando ao menu principal...")
                        time.sleep(2)
                        esc = 10
                        break
                    elif esc2 == 2:
                        print("Retornando a remoção de jogo...")
                        time.sleep(2)
                        print(linha * 2)
                        break
                    else: 
                        print("Escolha não reconhecida. Tente novamente.")
        else: 
            print("Nenhum jogo salvo ainda. Por favor, insira um jogo antes.")
            esc = 10

    #atualiza a nota de qualquer jogo escolhido pelo usuário
    elif esc == 4:
        if gamecont >= 1:
            print("Jogos salvos: ")
            for i, game in enumerate(listagame, 1):
                print(f"[{i}] {game}")
            print(linha * 2)
            atul = int(input("Digite o número do jogo para atualizar sua nota: "))

            #verifica se o atul(atualização) está entre o 1 e o gamecont.
            if 1 <= atul <= gamecont:
                nota1 = int(input("Gráficos: "))
                nota2 = int(input("Jogabilidade: "))
                nota3 = int(input("História: "))
                nota4 = int(input("Trilha Sonora: "))
                media = (nota1 + nota2 + nota3 + nota4) / 4
                listanota[atul - 1] = media
                print("Nota do jogo atualizada com sucesso!")
                esc = 10
            else:
                #um loop até o usuário colocar uma escolhada válida
                while True:
                    print("Escolha não reconhecida.")
                    esc2 = int(input("O que deseja fazer:\n[1] Voltar para o menu\n[2] Retomar a atualização da nota.\nEscolha: "))
                    if esc2 == 1:
                        print("Retornando ao menu principal...")
                        time.sleep(2)
                        esc = 10
                        break
                    elif esc == 2:
                        print("Retornando a atualização da nota...")
                        time.sleep(2)
                        print(linha * 2)
                        break
                    else:
                        print("Escolha não reconhecida. Tente novamente.")
        else:
            print("Nenhum jogo salvo ainda. Por favor, insira um jogo antes.")
            esc = 10

    #caso a escolha não for valida, ele voltará para o menu principal
    else:
        print("Escolha não reconhecida.\nVoltando para o menu...")
        time.sleep(2)
        esc = 10
    
print("Programa fechado com sucesso.")



import homemEnforcado as hm

def main():
    game = hm.homemEnforcado()

    #Enquanto você NÃO perder (6 letras erradas), execute o Game!
    while not (game.gameOver()):

        # Coleta a pilha de letras Erradas e Corretas
        letrasErradas = game.getLetrasErradas()
        letrasCorretas = game.getLetrasCorretas()
        # Mostra na tela a situação atual do game
        print(game)
        # Como a entrada será alfanumérica, não é necessário tratamento.
        letra = input("Digite uma letra: ")

        if letra in game.getPalavra():
            letrasCorretas.append(letra)
            game.setMensagem("Essa letra existe! Parabéns!")
            game.setPalavraMontada(letra)
        else:
            game.setTabuleiro(len(letrasErradas)+1)
            letrasErradas.append(letra)
            game.setMensagem("Letra errada! Você tem mais %s chance(s)" %(6 - len(letrasErradas)))

        if game.voceGanhou():
            print(game)
            print("Você ganhou! A palavra correta é: " + game.palavra)
            print("==================================================================================================")
            break
        elif game.gameOver():
            print(game)
            print("Você perdeu! Não foi desta vez...")
            print("==================================================================================================")

if __name__ == "__main__":
    main()
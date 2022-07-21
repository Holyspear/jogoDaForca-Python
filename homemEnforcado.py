
import random
import tabuleiro as tb

class homemEnforcado:
    def __init__(self):
        self.palavra = ""
        self.__letrasErradas = []
        self.__letrasCorretas = []
        self.__palavraMontada = {}
        self.__tabuleiro = tb.tabuleiro[0]
        self.mensagem = "Jogo iniciado!"
        self.buscaPalavra()
        self.iniciaPalavraMontada()

    def iniciaPalavraMontada(self):
        for x in list(self.palavra):
            self.__palavraMontada[x] = "_"

    def buscaPalavra(self):
        try:
            with open("palavras.txt", "rt", encoding="UTF-8") as f:
                palavra = f.readlines()
            self.palavra = palavra[random.randint(0, len(palavra))].strip()
        except IndexError:
            print("O banco de palavras acabou! Reinicie o Game para novas palavras.")

    def getPalavra(self):
        return self.palavra

    def getLetrasErradas(self):
        return self.__letrasErradas

    def setLetrasErradas(self, letra):
        self.__letrasErradas.append(letra)

    def getLetrasCorretas(self):
        return self.__letrasCorretas

    def setLetrasCorretas(self, letra):
        self.__letrasCorretas.append(letra)

    def getPalavraMontada(self):
        return self.__palavraMontada

    def setPalavraMontada(self, letra):
        for x in list(self.palavra):
            # Se a letra foi encontrada, atualiza o índice do dicionario
            # Substituindo o traço pela letra.
            if x == letra:
                self.__palavraMontada.update({x:letra})

    def getTabuleiro(self):
        return self.__tabuleiro

    def setTabuleiro(self, index):
        self.__tabuleiro = tb.tabuleiro[index]

    def setMensagem(self, mensagem):
        self.mensagem = mensagem

    def getMensagem(self):
        return self.mensagem

    def __str__(self):
        # Monta a saída do Game em forma de STRING
        return self.__tabuleiro + \
        "\n Status: " + self.mensagem + \
        "\n Palavra: " + " ".join(self.__palavraMontada.values()) + \
        "\n Letras Erradas: " + " ".join(self.__letrasErradas) + \
        "\n Letras Corretas: " + " ".join(self.__letrasCorretas)

    def voceGanhou(self):
        # Filtra a quantidade de traços e faz a contagem
        qtdTracos = len(list(filter(lambda y : y == "_", self.__palavraMontada.values())))
        # Se não houver mais traços, WIN!!!
        if qtdTracos == 0:
            return True
        else:
            return False

    def gameOver(self):
        #Se você tem 6 letras erradas, você perdeu
        return len(self.__letrasErradas) == 6
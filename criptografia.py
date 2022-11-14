from string import printable
from math import floor


def criptografar(texto, chave):
    lista = printable[0: 75]
    
    if chave == 0:
        return texto
    else:
        for i in range(0, len(texto)):
            if(texto[i] == " "):
                texto = texto[:i] + "~" + texto[i + 1:]

            if(texto[i] != "~"):
                posicao = buscarPosicao(texto[i], lista)
                if (posicao + 1 >= len(lista)):
                    posicao = calcularPosicao(posicao)

                texto = texto[:i] + lista[posicao + 1] + texto[i + 1:]
        return criptografar(texto, chave - 1)

def buscarPosicao(letra, lista):
    return lista.index(letra)

def calcularPosicao(numero):
    while True:
        if numero - 73 > 0:
            return numero - 73              
        else:
            numero += 73

def descriptografar(texto, chave):
    lista = printable[0: 75]
    if chave == 0:
        return texto
    else:
        for i in range(0, len(texto)):

            if(texto[i] == "~"):
                texto = texto[:i] + " " + texto[i + 1:]

            if (texto[i] != " "):
                posicao = buscarPosicao(texto[i], lista)
                if (posicao - 1 < 0):
                    posicao = calcularPosicao(posicao)

                texto = texto[:i] + lista[posicao - 1] + texto[i + 1:]
        return descriptografar(texto, chave - 1)

def menu():
    operacao = int(input("Informe 0 para criptografar e 1 para descriptografar: "))
    chave = int(input("Informe uma chave positiva que deseja utilizar: "))
    while chave < 0:
        chave = int(input("Informe uma chave positiva válida que deseja utilizar: "))

    arquivo = open('texto_secreto.txt', 'r')
    conteudo = str(arquivo.readlines())
    textoSecreto = conteudo[2: len(conteudo) - 2]

    if operacao == 0:
        retorno = criptografar(textoSecreto, chave)
    else:
        retorno = descriptografar(textoSecreto, chave)

    arquivo = open('texto_secreto.txt', 'w')

    listaRetorno = []

    arquivo.write(retorno)

    arquivo.close()

menu()

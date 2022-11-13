from string import printable
from math import floor


def criptografar(texto, chave):
    lista = printable[0: 93]
    if chave == 0 or chave % 2 == 0:
        return texto
    else:
        for i in range(0, len(texto)):

            if(texto[i] == " "):
                texto = texto[:i] + "~" + texto[i + 1:]

            else:
                posicao = buscarPosicao(texto[i], lista)

                if (posicao + 1 >= len(lista)):
                    posicao = calcularPosicao(i)

                texto = texto[:i] + lista[posicao + 1] + texto[i + 1:]
        return criptografar(texto, chave - 1)


def buscarPosicao(letra, lista):
    return lista.index(letra)


def calcularPosicao(numero):
    numeroString = str(numero)
    casasNumero = len(numeroString)
    resultado = int(numeroString[floor(casasNumero / 2):casasNumero])
    return resultado


def descriptografar(texto, chave):
    lista = printable[0: 93]
    if chave == 0 or chave % 2 == 0:
        return texto
    else:
        for i in range(0, len(texto)):

            if(texto[i] == "~"):
                texto = texto[:i] + " " + texto[i + 1:]
                print(texto)

            else:
                posicao = buscarPosicao(texto[i], lista)
                if (posicao - 1 < 0):
                    posicao = calcularPosicao(i)
                texto = texto[:i] + lista[posicao - 1] + texto[i + 1:]
        return descriptografar(texto, chave - 1)


arquivo = open('texto_secreto.txt', 'r')
conteudo = str(arquivo.readlines())
textoSecreto = conteudo[2: len(conteudo) - 2]

retorno = criptografar(textoSecreto, 184)
#retorno = descriptografar(textoSecreto, 1)

arquivo = open('texto_secreto.txt', 'w')

listaRetorno = []

arquivo.write(retorno)

arquivo.close()

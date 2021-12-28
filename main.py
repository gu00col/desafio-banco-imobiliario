from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker, Session
from marshmallow import Schema, fields
import simplejson as json

# Imports das Funções
from funcs import Dados, Tabuleiro, reset, Jogadores, Resultados, reset_resultados, main

# Connexão com o banco
engine = create_engine('sqlite:///BaseDeDados.db')

# Inicio da sessão do banco
session = Session(engine)



# Variaveis do jogo
numeros_de_testes = 300
maximo_rodadas_por_jogo  = 1000

        
# Resultados
resultados = []

# Execução
pergunta_debug = input('Antes de iniciar o teste você gostaria de ver todas as mensagens do teste? ex player 1 está na casa x e comprou a casa x? se sim digite 1 se não digite 2: ')
try:
    pergunta_debug = int(pergunta_debug)
    if pergunta_debug == 1:
        debug = True
    elif pergunta_debug == 2:
        debug = False
    else:
        print('O valor que você digitou não está no padrão esperado iremos considerar como Não!')
        debug = False
except:
    pergunta_debug = input('Você digitou um valor que não é numerico ou não está dentro do esperado por favor digite 1 para sim 2 para não:')
    pergunta_debug = int(pergunta_debug)
    if pergunta_debug == 1:
        debug = True
    elif pergunta_debug == 2:
        debug = False
    else:
        print('O valor que você digitou não está no padrão esperado iremos considerar como Não!')
        debug = False
main(numeros_de_testes,maximo_rodadas_por_jogo,debug)
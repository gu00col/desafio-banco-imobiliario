from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker, Session
from marshmallow import Schema, fields
import simplejson as json

# Imports das Funções
from funcs import Dados, Tabuleiro, reset, Jogadores, Resultados, reset_resultados

# Connexão com o banco
engine = create_engine('sqlite:///BaseDeDados.db')

# Inicio da sessão do banco
session = Session(engine)



# Variaveis do jogo
numeros_de_testes = 100
maximo_rodadas_por_jogo  = 500

        
# Resultados
resultados = []

# Execução

# Seleção de ordem de jogo


time_out = 0
contador_teste = 0
reset_resultados()
while contador_teste < numeros_de_testes:

    reset()
    contador_teste += 1
    print(f'\nRodada de teste: {contador_teste}')


    jogadores = Jogadores().list()
    faliu = []
    # Inicia o jogo
    contador_rodada = 0
    while contador_rodada < maximo_rodadas_por_jogo:
        
        for jogador in jogadores:
            
            if jogador['id'] in faliu:
                continue
            # Contador da partida
            contador_rodada += 1
    
            print(f'\nRodada {contador_rodada}')

            if len(faliu) == 3:
                print('\n\nO jogo cabou por falta de players calculando resultado ....')
                vencedor = Jogadores().vencedor()
                Resultados().novo(contador_teste,contador_rodada,vencedor['perfil'],0,vencedor['id'])
                contador_rodada += 2000
                break

            
            # Variaveis Fixas
            id_jogador = jogador['id'] 
            perfil = jogador['perfil']
            
            print(f'\nJogador jogando {id_jogador}')
            
            # Variaveis Dinamicas
            caixa  = Tabuleiro().caixa_atual(id_jogador)
            posicao = Tabuleiro().posicao_atual(id_jogador)
            posicao_tabuleiro = Tabuleiro().posicao_tabuleiro(posicao)
            print(f'Caixa: {caixa}')
            print(f'Perfil: {perfil}')
            print(f'\nPosição atual: {posicao_tabuleiro["nome"]}')
            print(f'Preço de compra: {posicao_tabuleiro["valor_venda"]}')
            print(f'Aluguel: {posicao_tabuleiro["valor_aluguel"]}')
            print(f'Proprietario: {posicao_tabuleiro["proprietario"]}\n')
            # Variaveis do jogador por rodada
            dados = Dados.rolar()
            
            # Saida contadores
            print(f'--Tirou {dados} no dado!')
            nova_posicao = Tabuleiro().posicao(id_jogador, dados)
            posicao_tabuleiro = Tabuleiro().posicao_tabuleiro(nova_posicao)
            print(f'\nPosição atual: {posicao_tabuleiro["nome"]}')
            print(f'Preço de compra: {posicao_tabuleiro["valor_venda"]}')
            print(f'Aluguel: {posicao_tabuleiro["valor_aluguel"]}')
            print(f'Proprietario: {posicao_tabuleiro["proprietario"]}')

            # Validação se tem ou não proprietario
            if posicao_tabuleiro['proprietario'] != None and posicao_tabuleiro['proprietario'] != id_jogador:
                # Se tem dono e ele não é o dono deve pagar o valor do aluguel

                # Valida se o jogador ainda está no game
                val_proprietario = Tabuleiro().verifica_propriedade(posicao_tabuleiro['id'])
                if val_proprietario:
                    # Saque
                    saque = Tabuleiro().saque(id_jogador,posicao_tabuleiro['id'])
                    if Tabuleiro().caixa_atual(id_jogador) < 0:
                        print('Jogador faliu! está fora do jogo!')
                        Tabuleiro().vende_todas(id_jogador)
                        faliu.append(id_jogador)
                        continue
                else:
                    # Propriedade sem dono
                    compra = Tabuleiro().compra(id_jogador,posicao_tabuleiro['id'])
                    pass
            elif posicao_tabuleiro['id'] != 1 and posicao_tabuleiro['proprietario'] == None:
                    # Propriedade sem dono
                compra = Tabuleiro().compra(id_jogador,posicao_tabuleiro['id'])
            else:
                pass

            print('\n')
            if contador_rodada == maximo_rodadas_por_jogo:
                print('O jogo acabou por rodadas Calculando o resultado...')
                vencedor = Jogadores().vencedor_timeout()
                Resultados().novo(contador_teste,contador_rodada,vencedor['perfil'],1,vencedor['id'])
                break
    print('\n','#'*30,'\n')

# Resultados 
Resultados().result_timeouts()
Resultados().media_de_rodadas()
Resultados().porcentagem_perfil()
Resultados().perfil_vencedor()
# Imports default 
import random
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker, Session
from marshmallow import Schema, fields
import simplejson as json
from sqlalchemy.sql.expression import func
# Models
from models import Jogadore, Resultado,Tabuleiros,jogador_json,jogadores_json,tabuleiro_json,tabuleiros_json

# Connexão com o banco
engine = create_engine('sqlite:///BaseDeDados.db')

# Inicio da sessão do banco
session = Session(engine)

class Dados():
    def rolar():
        return random.randint(1, 6)

class Jogadores():
    def list(self):
        mixed = []
        jogadores = session.query(Jogadore).order_by(func.random()).order_by(Jogadore.id).all()
        jogadores = jogadores_json.dump(jogadores)
        
        return jogadores

    def vencedor(self):
        jogador = session.query(Jogadore).filter(Jogadore.caixa > -1).first()
        jogador = jogador_json.dump(jogador)
        print(f"O vencedor foi o jogador {jogador['id']} com o perfil {jogador['perfil']} com caixa de {jogador['caixa']}")
        return jogador


    def vencedor_timeout(self):
        try:
            jogador = session.query(Jogadore).filter(Jogadore.caixa > -1).order_by(Jogadore.caixa.desc()).first()
            jogador = jogador_json.dump(jogador)
            print(f"O vencedor foi o jogador {jogador['id']} com o perfil {jogador['perfil']} com caixa de {jogador['caixa']}")
            return jogador
        except Exception as e:
            print(f'ERRO -> {e}')


class Resultados():
    def novo(self, teste,rodada,perfil, timeout,vencedor):
        resultado = Resultado(rodada=rodada, perfil=perfil, timeout=timeout, vencedor=vencedor,teste=teste)
        session.add(resultado)
        session.commit()
        print('Resultado adicionadoa o banco!')
    
    def result_timeouts(self):
        timeouts = session.query(Resultado).filter_by(timeout=1).count()
        print(f'De 300 rodadas {timeouts} partidas terminaram por timeout!')
        return timeouts

    def media_de_rodadas(self):
        media = session.query(func.avg(Resultado.rodada).label('media')).first()
        print(f'A media de rodadas por partida é de {media.media}')
        return media.media
    
    def porcentagem_perfil(self):

        porcentagem = session.query(func.count(Resultado.id).label('porcentagem'), Resultado.perfil).group_by(Resultado.perfil).all()
        print('A porcentagem de vitorias por perfil é:')
        for valor in porcentagem:
            porcent = (valor[0]*100)/300
            perfil = valor[1]
            print(f' - {round(porcent)}% de vitorias para o perfil {perfil}')
        return porcentagem
    
    def perfil_vencedor(self):
        vencedor = session.query(func.sum(Resultado.rodada).label('vencedor'),Resultado.perfil).group_by(Resultado.vencedor).order_by(func.sum(Resultado.rodada).desc()).first()
        print(f'O perfil que mais vence é o {vencedor.perfil}')

class Tabuleiro():
    def posicao(self,jogador_id, posicao):

        # Atualizando os dados dos jogadores

        jogador = session.query(Jogadore).filter_by(id=jogador_id).first()
        json_jogador = jogador_json.dump(jogador)
        
        posicao_atual = json_jogador['posicao']
        caixa_atual = json_jogador['caixa']

        nova_posicao = posicao_atual + posicao

        if nova_posicao > 20:

            # Adiciona 100 ao caixa apos dar a volta no tabuleiro

            novo_caixa = caixa_atual + 100

            jogador.caixa = novo_caixa
            
            print(f'Completou uma volta e recebeu 100 seu saldo anterior era {caixa_atual} seu novo saldo é {novo_caixa}')

            # Corrigindo as posições

            nova_posicao = nova_posicao - 20

            jogador.posicao = nova_posicao
            session.commit()

            print(f'Se move até a casa: {nova_posicao}!')
            return nova_posicao
        else:
            jogador.posicao = nova_posicao
            session.commit()
            print(f'Se move até a casa: {nova_posicao}!')
            return nova_posicao

    def vende_todas(self, id_dono):
        propriedades = session.query(Tabuleiros).filter_by(id=id_dono).all()
        for propriedade in propriedades:
            propriedade.proprietario = None
            session.commit()
            print(f'Todas as propriedades do player {id_dono} foram colocadas a venda!')

        
    def posicao_atual(self, id_jogador):
        # Atualizando os dados dos jogadores

        jogador = session.query(Jogadore).filter_by(id=id_jogador).first()
        json_jogador = jogador_json.dump(jogador)
        
        posicao_atual = json_jogador['posicao']
        return posicao_atual

    def caixa_atual(self,id_jogador):
        jogador = session.query(Jogadore).filter_by(id=id_jogador).first()
        json_jogador = jogador_json.dump(jogador)
        
        caixa_atual = json_jogador['caixa']
        return caixa_atual

    def posicao_tabuleiro(self, posicao):

        tabuleiro = session.query(Tabuleiros).filter_by(id=posicao).first()
        json_tabuleiro = tabuleiro_json.dump(tabuleiro)
        return json_tabuleiro

    def verifica_propriedade(self, id_propriedade):
        propriedade = session.query(Tabuleiros).filter_by(id=id_propriedade).first()
        proprietario = session.query(Jogadore).filter_by(id=propriedade.proprietario).first()
        if proprietario.caixa < 0:
            print('O caixa do dono está negativo. A propriedade foi colocada a venda novamente!')
            propriedade.proprietario = None
            session.commit()
            return False
        else:
            print(f'A propriedade tem dono com caixa positivo {proprietario.id}! ')
            return True

    def saque(self,id_jogador,id_propriedade):
        # Propriedade alvo
        propriedade = session.query(Tabuleiros).filter_by(id=id_propriedade).first()
        valor_aluguel = propriedade.valor_aluguel
        proprietario = propriedade.proprietario
        # Jogador a ser cobrado
        jogador_a_ser_cobrado = session.query(Jogadore).filter_by(id=id_jogador).first()
        # jogador a ser pago
        jogador_a_ser_pago = session.query(Jogadore).filter_by(id=proprietario).first()

        # Saque
        jogador_a_ser_cobrado.caixa = jogador_a_ser_cobrado.caixa - valor_aluguel

        # Deposito
        jogador_a_ser_pago.caixa = jogador_a_ser_pago.caixa + valor_aluguel

        session.commit()
        print(f'Jogador {id_jogador} pagou {valor_aluguel} para o jogador {proprietario} pelo aluguel de {propriedade.nome}!')
        
    def compra(self, id_jogador,id_propriedade):
        # Propriedade alvo
        propriedade = session.query(Tabuleiros).filter_by(id=id_propriedade).first()
        # Jogador que vai comprar
        comprador = session.query(Jogadore).filter_by(id=id_jogador).first()
        if propriedade.valor_venda > comprador.caixa:
            print(f'Jogador não tem dinheiro para comprar valor necessario {propriedade.valor_venda} disponivel {comprador.caixa}!')
            return False
        else:
            # Efetuando a compra

            # Validando os perfis de compra

            perfil = comprador.perfil


            if perfil == 'impulsivo':
                '''
                Regra:
                O jogador impulsivo compra qualquer propriedade sobre a qual ele parar.
                '''
                # sacar o dinheiro
                comprador.caixa = comprador.caixa - propriedade.valor_venda
                # mudar o proprietario
                propriedade.proprietario = comprador.id
                session.commit()
                jogador = session.query(Jogadore).filter_by(id=id_jogador).first()
                print(f'O jogador comprou a propriedade {propriedade.nome} por {propriedade.valor_venda} sobrando em caixa {jogador.caixa}')
                return True
            elif perfil == 'exigente':
                '''
                Regra:
                O jogador exigente compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.
                '''
                if propriedade.valor_venda > 50:
                    # sacar o dinheiro
                    comprador.caixa = comprador.caixa - propriedade.valor_venda
                    # mudar o proprietario
                    propriedade.proprietario = comprador.id
                    session.commit()
                    jogador = session.query(Jogadore).filter_by(id=id_jogador).first()
                    print(f'O jogador comprou a propriedade {propriedade.nome} por {propriedade.valor_venda} sobrando em caixa {jogador.caixa}')
                    return True
                else:
                    return False
            elif perfil == 'cauteloso':
                '''
                Regra:
               O jogador cauteloso compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando
depois de realizada a compra.
                '''
                valor_restante = comprador.caixa - propriedade.valor_venda
                if valor_restante > 80:
                    # sacar o dinheiro
                    comprador.caixa = comprador.caixa - propriedade.valor_venda
                    # mudar o proprietario
                    propriedade.proprietario = comprador.id
                    session.commit()
                    jogador = session.query(Jogadore).filter_by(id=id_jogador).first()
                    print(f'O jogador comprou a propriedade {propriedade.nome} por {propriedade.valor_venda} sobrando em caixa {jogador.caixa}')
                    return True
                else:
                    return False
            else:
                '''
                Regra:
                O jogador aleatório compra a propriedade que ele parar em cima com probabilidade de 50%.
                '''
                if Dados.rolar() > 3:
                    # sacar o dinheiro
                    comprador.caixa = comprador.caixa - propriedade.valor_venda
                    # mudar o proprietario
                    propriedade.proprietario = comprador.id
                    session.commit()
                    jogador = session.query(Jogadore).filter_by(id=id_jogador).first()
                    print(f'O jogador comprou a propriedade {propriedade.nome} por {propriedade.valor_venda} sobrando em caixa {jogador.caixa}')
                    return True
                else:
                    return False


def reset_resultados():
    consulta = session.query(Resultado).delete()
    session.commit()

            

def reset():
    jogadores = session.query(Jogadore).all()
    for jogador in jogadores:
        jogador.caixa = 300
        jogador.posicao = 1

    
    casas = session.query(Tabuleiros).all()
    for casa in casas:
        casa.proprietario = None
        session.commit()

    print('Iniciando nova rodada de teste parametros dos jogadores zerada!')    
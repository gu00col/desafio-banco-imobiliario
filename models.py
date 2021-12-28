# coding: utf-8
from sqlalchemy import Column, Float, Integer, MetaData, Table, Text
from sqlalchemy.schema import FetchedValue
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base
from marshmallow import Schema, fields

Base = declarative_base()
metadata = Base.metadata



class Jogadore(Base):
    __tablename__ = 'jogadores'

    id = Column(Integer, primary_key=True)
    caixa = Column(Float, nullable=False)
    posicao = Column(Integer, nullable=False)
    perfil = Column(Text(255), nullable=False)

class JogadoreSchema(Schema):
    class Meta:
        ordered = False
        fields = ('id', 'caixa', 'posicao','perfil')

jogador_json = JogadoreSchema()
jogadores_json = JogadoreSchema(many=True)

class Resultado(Base):
    __tablename__ = 'resultados'

    id = Column(Integer, primary_key=True)
    rodada = Column(Integer, nullable=False)
    vencedor = Column(Integer, nullable=False)
    perfil = Column(Text, nullable=False)
    timeout = Column(Integer, nullable=False, server_default=FetchedValue())
    teste = Column(Integer, nullable=False)

class Tabuleiros(Base):
    __tablename__ = 'tabuleiro'

    id = Column(Integer, primary_key=True)
    nome = Column(Text)
    tipo = Column(Text)
    valor_venda = Column(Float)
    valor_aluguel = Column(Float)
    proprietario = Column(Text)
    tag = Column(Text)

class TabuleirosSchema(Schema):
    class Meta:
        ordered = True
        fields = ('id','nome', 'tipo', 'valor_venda', 'valor_aluguel', 'proprietario', 'tag')

tabuleiro_json = TabuleirosSchema()
tabuleiros_json = TabuleirosSchema(many=True)
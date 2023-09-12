import db
from sqlalchemy import Column, VARCHAR, BLOB, Integer, FLOAT

# ORM

class ProdutoDB(db.Base):
    __tablename__ = 'tb_produto'

    id_produto = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    descricao = Column(VARCHAR(200), nullable=False)
    foto = Column(BLOB, nullable=True)
    valor_unitario = Column(FLOAT, nullable=False)

    def __init__(self, id_produto, nome, descricao, valor_unitario, foto):
        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.valor_unitario = valor_unitario
        self.foto = foto
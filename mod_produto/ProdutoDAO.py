# import da persistência
import db
from mod_produto.ProdutoModel import ProdutoDB

from mod_produto.Produto import Produto

from fastapi import APIRouter

# import da segurança
from fastapi import Depends
import security

router = APIRouter(dependencies=[Depends(security.verify_token), Depends(security.verify_key)])

# Criar as rotas/endpoints: GET, POST, PUT, DELETE
@router.get("/Produto/", tags=["Produto"])
def get_Produto():
    try:
        session = db.Session()
        # busca todos
        dados = session.query(ProdutoDB).all()
        return dados, 200
    
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()
    

@router.get("/Produto/{id}", tags=["Produto"])
def get_Produto(id: int):
    try:
        session = db.Session()
        # busca um com filtro
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).all()
        return dados, 200
    
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()


@router.post("/Produto/", tags=["Produto"])
def post_Produto(corpo: Produto):
    try:
        session = db.Session()

        dados = ProdutoDB(None, corpo.nome, corpo.descricao, corpo.valor_unitario, corpo.foto)

        session.add(dados)

        session.commit()

        return {"id": dados.id_produto, "nome": dados.nome}, 200
    
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    
    finally:
        session.close()


@router.put("/Produto/{id}", tags=["Produto"])
def put_Produto(id: int, corpo: Produto):
    try:
        session = db.Session()

        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one()

        dados.nome = corpo.nome
        dados.descricao = corpo.descricao
        dados.valor_unitario = corpo.valor_unitario
        dados.foto #

        session.add(dados)
        session.commit()

        return {"id": dados.id_produto, "nome": dados.nome}, 200
    
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    
    finally:
        session.close()


@router.delete("/Produto/{id}", tags=["Produto"])
def delete_Produto(id: int):
    try:
        session = db.Session()

        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one()
        session.delete(dados)
        session.commit()

        return {"id": dados.id_produto, "nome": dados.nome}, 200
    
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    
    finally:
        session.close()
from mod_produto.Produto import Produto

from fastapi import APIRouter
router = APIRouter()

# Criar as rotas/endpoints: GET, POST, PUT, DELETE
@router.get("/Produto/", tags=["Produto"])
def get_Produto():
    return {"msg": "get todos executado"}, 200

@router.get("/Produto/{id}", tags=["Produto"])
def get_Produto(id: int):
    return {"msg": "get um executado"}, 200

@router.post("/Produto/", tags=["Produto"])
def post_Produto(p: Produto):
    return {"msg": "post executado", "nome": p.nome, "descrição": p.descricao}, 200


@router.put("/Produto/{id}", tags=["Produto"])
def put_Produto(id: int, p: Produto):
    return {"msg": "put executado", "id": id, "nome": p.nome, "descrição": p.descricao}, 201


@router.delete("/Produto/{id}", tags=["Produto"])
def delete_Produto(id: int):
    return {"msg": "delete executado"}, 201
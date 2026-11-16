
from fastapi import APIRouter, Depends, status, HTTPException
from entidades.models import CategoriaEquipamento
from sqlmodel import Session

from dependencies.dependencies import database
from dependencies.auth import verifica_permissao
from controllers import CategoriaEquipamentosController


categoria_equipamento_router = APIRouter()


@categoria_equipamento_router.get(
    "/categorias",
    response_model=list[CategoriaEquipamento],
    status_code=status.HTTP_200_OK
)
def listarCategorias(
    db: Session = Depends(database.get_db),
    usuario_atual=Depends(
        verifica_permissao("ADMIN", "GESTOR", "DISCENTE")
    )
):
    try:
<<<<<<< HEAD
        categorias = CategoriaEquipamentosController.buscar_todas_categoria_equipamento(db)

        if not categorias:
            return []

        return categorias
=======
        categorias = (
            CategoriaEquipamentosController
            .buscar_todas_categoria_equipamento(db)
        )

        return categorias if categorias else []
>>>>>>> 8523117e1e0455c08d5d444c88f423bffd05872a

    except RuntimeError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@categoria_equipamento_router.post(
    "/categorias",
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaEquipamento
)
def inserir(
    categoria: CategoriaEquipamento,
    db: Session = Depends(database.get_db),
<<<<<<< HEAD
    usuario_atual=Depends(
        verifica_permissao("ADMIN", "GESTOR")
    )
):
    try:
        categoria_cadastrada = CategoriaEquipamentosController.inserir_categoria(
            categoria,
            db
        )
        return categoria_cadastrada

    except RuntimeError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
=======
    usuario_atual=Depends(verifica_permissao("ADMIN", "GESTOR"))
):
    try:
        return CategoriaEquipamentosController.inserir_categoria(
            categoria,
            db
        )

    except RuntimeError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@categoria_equipamento_router.put(
    "/categorias/{categoria_id}",
    status_code=status.HTTP_200_OK,
    response_model=CategoriaEquipamento
)
def AtualizarCategoria(
    categoria_id: int,
    categoria_data: CategoriaEquipamento,
    db: Session = Depends(database.get_db),
    usuario_atual=Depends(verifica_permissao("ADMIN", "GESTOR"))
):
    try:
        return CategoriaEquipamentosController.atualizar_categoria(
            db,
            categoria_id,
            categoria_data
        )

    except KeyError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
>>>>>>> 8523117e1e0455c08d5d444c88f423bffd05872a
            detail=str(e)
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
<<<<<<< HEAD


@categoria_equipamento_router.put(
    "/categorias/{categoria_id}",
    status_code=status.HTTP_200_OK,
    response_model=CategoriaEquipamento
)
def AtualizarCategoria(
    categoria_id: int,
    categoria_data: CategoriaEquipamento,
    db: Session = Depends(database.get_db),
    usuario_atual=Depends(
        verifica_permissao("ADMIN", "GESTOR")
    )
):
    try:
        return CategoriaEquipamentosController.atualizar_categoria(
            db,
            categoria_id,
            categoria_data
        )

    except KeyError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

    except RuntimeError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


=======

    except RuntimeError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


>>>>>>> 8523117e1e0455c08d5d444c88f423bffd05872a
@categoria_equipamento_router.delete(
    "/categorias/{categoria_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def deletar_categoria(
    categoria_id: int,
    db: Session = Depends(database.get_db),
<<<<<<< HEAD
    usuario_atual=Depends(
        verifica_permissao("ADMIN", "GESTOR")
    )
=======
    usuario_atual=Depends(verifica_permissao("ADMIN", "GESTOR"))
>>>>>>> 8523117e1e0455c08d5d444c88f423bffd05872a
):
    try:
        CategoriaEquipamentosController.deletar_categoria(
            db,
            categoria_id
        )

    except KeyError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )

    except RuntimeError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

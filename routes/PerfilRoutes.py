<<<<<<< HEAD

from fastapi import APIRouter, Depends, status, HTTPException
from entidades.models import Perfil
from sqlmodel import Session

from dependencies.dependencies import database
from dependencies.auth import verifica_permissao
from controllers import PerfilController

=======

from fastapi import APIRouter, Depends, status, HTTPException
from entidades.models import Perfil
from sqlmodel import Session

from dependencies.dependencies import database
from dependencies.auth import verifica_permissao
from controllers import PerfilController


>>>>>>> 8523117e1e0455c08d5d444c88f423bffd05872a
perfil_router = APIRouter()


@perfil_router.get(
    "/perfis",
    response_model=list[Perfil],
    status_code=status.HTTP_200_OK
)
<<<<<<< HEAD
def listarperfis(
=======
def listar_perfis(
>>>>>>> 8523117e1e0455c08d5d444c88f423bffd05872a
    db: Session = Depends(database.get_db),
    usuario_atual=Depends(verifica_permissao("ADMIN"))
):
    try:
        perfis = PerfilController.buscar_todos_os_perfis(db)
<<<<<<< HEAD

        if not perfis:
            return []

        return perfis
=======
        return perfis if perfis else []
>>>>>>> 8523117e1e0455c08d5d444c88f423bffd05872a

    except RuntimeError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@perfil_router.post(
    "/perfis",
    status_code=status.HTTP_201_CREATED,
    response_model=Perfil
)
def inserir_perfil(
    perfil: Perfil,
    db: Session = Depends(database.get_db),
    usuario_atual=Depends(verifica_permissao("ADMIN"))
):
    try:
<<<<<<< HEAD
        perfil_cadastrado = PerfilController.inserir_perfil(
            perfil,
            db
        )
        return perfil_cadastrado
=======
        return PerfilController.inserir_perfil(perfil, db)
>>>>>>> 8523117e1e0455c08d5d444c88f423bffd05872a

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


@perfil_router.put(
    "/perfis/{perfil_id}",
    status_code=status.HTTP_200_OK,
    response_model=Perfil
)
def atualizar_perfil(
    perfil_id: int,
    perfil_data: Perfil,
    db: Session = Depends(database.get_db),
    usuario_atual=Depends(verifica_permissao("ADMIN"))
):
<<<<<<< HEAD
    try:
        return PerfilController.atualizar_perfil(
            db,
            perfil_id,
            perfil_data
        )
=======
    try:
        return PerfilController.atualizar_perfil(
            db,
            perfil_id,
            perfil_data
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


@perfil_router.delete(
    "/perfis/{perfil_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def deletar_perfil(
    perfil_id: int,
    db: Session = Depends(database.get_db),
    usuario_atual=Depends(verifica_permissao("ADMIN"))
):
    try:
        PerfilController.deletar_perfil(db, perfil_id)
>>>>>>> 8523117e1e0455c08d5d444c88f423bffd05872a

    except KeyError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

    except ValueError as e:
        raise HTTPException(
<<<<<<< HEAD
            status_code=status.HTTP_400_BAD_REQUEST,
=======
            status_code=status.HTTP_409_CONFLICT,
>>>>>>> 8523117e1e0455c08d5d444c88f423bffd05872a
            detail=str(e)
        )

    except RuntimeError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
<<<<<<< HEAD


@perfil_router.delete(
    "/perfis/{perfil_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def deletar_perfil(
    perfil_id: int,
    db: Session = Depends(database.get_db),
    usuario_atual=Depends(verifica_permissao("ADMIN"))
):
    try:
        PerfilController.deletar_perfil(
            db,
            perfil_id
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
=======
>>>>>>> 8523117e1e0455c08d5d444c88f423bffd05872a

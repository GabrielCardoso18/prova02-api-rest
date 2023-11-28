import random

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlmodel import select

from src.config.database import get_session
from src.models.reservas_model import Reserva
from src.models.voos_model import Voo

reservas_router = APIRouter(prefix="/reservas")


@reservas_router.get("/{id_voo}")
def lista_reservas_voo(id_voo: int):
    with get_session() as session:
        statement = select(Reserva).where(Reserva.voo_id == id_voo)
        reservas = session.exec(statement).all()
        return reservas


@reservas_router.post("")
def cria_reserva(reserva: Reserva):
    with get_session() as session:
        voo = session.exec(select(Voo).where(Voo.id == reserva.voo_id)).first()

        if not voo:
            return JSONResponse(
                content={"message": f"Voo com id {reserva.voo_id} não encontrado."},
                status_code=404,
            )

        # TODO - Validar se existe uma reserva para o mesmo documento
        for reservas_voo in voo.reservas:
            if reservas_voo.documento == reserva.documento:
                return JSONResponse(
                    content={"message": f"O código {reserva.codigo_reserva} já está cadastrado."},
                    status_code=400,
                )

        codigo_reserva = "".join(
            [str(random.randint(0, 999)).zfill(3) for _ in range(2)]
        )

        reserva.codigo_reserva = codigo_reserva
        session.add(reserva)
        session.commit()
        session.refresh(reserva)
        return reserva


@reservas_router.post("/{codigo_reserva}/checkin/{num_poltrona}")
def faz_checkin(codigo_reserva: str, num_poltrona: int):
    # TODO - Implementar reserva de poltrona
     with get_session() as session:
        reserva = session.exec(select(Reserva).where(Reserva.codigo_reserva == codigo_reserva)).first()

        if not reserva:
            return JSONResponse(
                content={"message": f"Reserva com o código {codigo_reserva} não encontrado."},
                status_code=404,
            )
        
        voo = session.exec(select(Voo).where(Voo.id == reserva.voo_id)).first()
        
        if not voo:
            return JSONResponse(
                content={"message": f"Voo com id {reserva.voo_id} não encontrado."},
                status_code=404,
            )
        
        if voo.poltrona_1 is None:
           voo.poltrona_1 = num_poltrona
           session.add(voo)
           session.commit()
           session.refresh(voo)
           return voo
        elif voo.poltrona_2 is None:
           voo.poltrona_2 = num_poltrona
           reserva.codigo_reserva = codigo_reserva
           session.add(voo)
           session.commit()
           session.refresh(voo)
           return voo
        elif voo.poltrona_3 is None:
           voo.poltrona_3 = num_poltrona
           session.add(voo)
           session.commit()
           session.refresh(voo)
           return voo
        elif voo.poltrona_4 is None:
           voo.poltrona_4 = num_poltrona
           session.add(voo)
           session.commit()
           session.refresh(voo)
           return voo
        elif voo.poltrona_5 is None:
           voo.poltrona_5 = num_poltrona
           session.add(voo)
           session.commit()
           session.refresh(voo)
           return voo
        elif voo.poltrona_6 is None:
           voo.poltrona_6 = num_poltrona
           session.add(voo)
           session.commit()
           session.refresh(voo)
           return voo
        elif voo.poltrona_7 is None:
           voo.poltrona_7 = num_poltrona
           session.add(voo)
           session.commit()
           session.refresh(voo)
           return voo
        elif voo.poltrona_8 is None:
           voo.poltrona_8 = num_poltrona
           session.add(voo)
           session.commit()
           session.refresh(voo)
           return voo
        elif voo.poltrona_9 is None:
           voo.poltrona_9 = num_poltrona 
           session.add(voo)
           session.commit()
           session.refresh(voo)
           return voo
        
# TODO - Implementar troca de reserva de poltrona
@reservas_router.patch("/{id_reserva}/checkin/{num_poltrona}")
def faz_checkin(id_reserva: int, num_poltrona: int):
        with get_session() as session:
            reserva = session.exec(select(Reserva).where(Reserva.id == id_reserva)).first()

            if not reserva:
                return JSONResponse(
                    content={"message": f"Reserva com o id {id_reserva} não encontrado."},
                    status_code=404,
                )
            
            voo = session.exec(select(Voo).where(Voo.id == reserva.voo_id)).first()
            
            if not voo:
                return JSONResponse(
                    content={"message": f"Voo com id {reserva.voo_id} não encontrado."},
                    status_code=404,
                )
            
            if num_poltrona == 1:
                if voo.poltrona_1 is None:
                    voo.poltrona_1 = num_poltrona
                    session.add(voo)
                    session.commit()
                    session.refresh(voo)
                    return voo
                else:
                    return JSONResponse(
                        content={"message": "Poltrona ocupada."},
                        status_code=403,
                    )
            if num_poltrona == 2:
                if voo.poltrona_2 is None:
                    voo.poltrona_2 = num_poltrona
                    session.add(voo)
                    session.commit()
                    session.refresh(voo)
                    return voo
                else:
                    return JSONResponse(
                        content={"message": "Poltrona ocupada."},
                        status_code=403,
                    )
            if num_poltrona == 3:
                if voo.poltrona_3 is None:
                    voo.poltrona_3 = num_poltrona
                    session.add(voo)
                    session.commit()
                    session.refresh(voo)
                    return voo
                else:
                    return JSONResponse(
                        content={"message": "Poltrona ocupada."},
                        status_code=403,
                    )
            if num_poltrona == 4:
                if voo.poltrona_4 is None:
                    voo.poltrona_4 = num_poltrona
                    session.add(voo)
                    session.commit()
                    session.refresh(voo)
                    return voo
                else:
                    return JSONResponse(
                        content={"message": "Poltrona ocupada."},
                        status_code=403,
                    )
            if num_poltrona == 5:
                if voo.poltrona_5 is None:
                    voo.poltrona_5 = num_poltrona
                    session.add(voo)
                    session.commit()
                    session.refresh(voo)
                    return voo
                else:
                    return JSONResponse(
                        content={"message": "Poltrona ocupada."},
                        status_code=403,
                    )
            if num_poltrona == 6:
                if voo.poltrona_6 is None:
                    voo.poltrona_6 = num_poltrona
                    session.add(voo)
                    session.commit()
                    session.refresh(voo)
                    return voo
                else:
                    return JSONResponse(
                        content={"message": "Poltrona ocupada."},
                        status_code=403,
                    )
            if num_poltrona == 7:
                if voo.poltrona_7 is None:
                    voo.poltrona_7 = num_poltrona
                    session.add(voo)
                    session.commit()
                    session.refresh(voo)
                    return voo
                else:
                    return JSONResponse(
                        content={"message": "Poltrona ocupada."},
                        status_code=403,
                    )
            if num_poltrona == 8:
                if voo.poltrona_8 is None:
                    voo.poltrona_8 = num_poltrona
                    session.add(voo)
                    session.commit()
                    session.refresh(voo)
                    return voo
                else:
                    return JSONResponse(
                        content={"message": "Poltrona ocupada."},
                        status_code=403,
                    )
            if num_poltrona == 9:
                if voo.poltrona_9 is None:
                    voo.poltrona_9 = num_poltrona 
                    session.add(voo)
                    session.commit()
                    session.refresh(voo)
                    return voo
                else:
                    return JSONResponse(
                        content={"message": "Poltrona ocupada."},
                        status_code=403,
                    )
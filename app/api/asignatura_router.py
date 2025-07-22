from fastapi import APIRouter, HTTPException
from app.models import Asignatura
from app.services import AsignaturaService

router = APIRouter(prefix="/asignaturas", tags=["Asignaturas"])
asignatura_service = AsignaturaService()

@router.post("/", response_model=Asignatura)
def crear_asignatura(asignatura: Asignatura):
    try:
        return asignatura_service.crear_asignatura(asignatura)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{id}", response_model=Asignatura)
def obtener_asignatura(id: str):
    try:
        return asignatura_service.obtener_asignatura(id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{id}", response_model=Asignatura)
def actualizar(id: str, datos: Asignatura):
    try:
        return asignatura_service.actualizar_asignatura(id, datos)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{id}")
def eliminar(id: str):
    try:
        asignatura_service.eliminar_asignatura(id)
        return {"mensaje": "Eliminada correctamente"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

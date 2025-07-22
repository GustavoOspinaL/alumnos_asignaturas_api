from fastapi import APIRouter, HTTPException
from app.models import Alumno, Matricula
from app.services import AlumnoService

router = APIRouter(prefix="/alumnos", tags=["Alumnos"])
alumno_service = AlumnoService()

@router.post("/", response_model=Alumno)
def crear_alumno(alumno: Alumno):
    return alumno_service.crear_alumno(alumno)

@router.get("/{alumno_id}", response_model=Alumno)
def obtener_alumno(alumno_id: str):
    return alumno_service.obtener_alumno(alumno_id)

@router.put("/alumnos/{id}", response_model=Alumno)
def actualizar_alumno(id: str, nuevos_datos: Alumno):
    alumno_actualizado = alumno_service.actualizar_alumno(id, nuevos_datos)
    if not alumno_actualizado:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return alumno_actualizado

@router.delete("/alumnos/{id}")
def eliminar_alumno(id: str):
    eliminado = alumno_service.eliminar_alumno(id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return {"mensaje": "Alumno eliminado correctamente"}

@router.post("/alumnos/{id}/matricular", response_model=Alumno)
def matricular_alumno(id: str, matricula: Matricula):
    alumno = alumno_service.matricular_alumno(id, matricula.asignatura_id, matricula.grupo_id)
    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return alumno

@router.post("/alumnos/{id}/desmatricular", response_model=Alumno)
def desmatricular_alumno(id: str, matricula: Matricula):
    alumno = alumno_service.desmatricular_alumno(id, matricula.asignatura_id, matricula.grupo_id)
    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return alumno
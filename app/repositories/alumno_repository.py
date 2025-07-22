from typing import Optional
from app.models import Alumno, Matricula
import uuid

class AlumnoRepository:
    def __init__(self):
        self.alumnos = {
            "1": Alumno(
                id="1",
                dni="12345678A",
                nombre="Juan",
                apellidos="Pérez",
                asignaturas=[]
            ),
            "2": Alumno(
                id="2",
                dni="87654321B",
                nombre="Ana",
                apellidos="López",
                asignaturas=[]
            )
        }

    def guardar_alumno(self, alumno: Alumno) -> Alumno:
        alumno.id = str(uuid.uuid4())
        self.alumnos[alumno.id] = alumno
        return alumno

    def obtener_alumno_por_id(self, id_alumno: str) -> Optional[Alumno]:
        return self.alumnos.get(id_alumno)

    def actualizar_alumno(self, id_alumno: str, nuevos_datos: Alumno) -> Optional[Alumno]:
        if id_alumno in self.alumnos:
            alumno_existente = self.alumnos[id_alumno]
            alumno_existente.nombre = nuevos_datos.nombre
            alumno_existente.apellidos = nuevos_datos.apellidos
            alumno_existente.dni = nuevos_datos.dni
            return alumno_existente
        return None

    def eliminar_alumno(self, id_alumno: str) -> bool:
        if id_alumno in self.alumnos:
            del self.alumnos[id_alumno]
            return True
        return False

    def matricular_alumno(self, id_alumno: str, asignatura_id: str, grupo_id: str) -> Optional[Alumno]:
        alumno = self.alumnos.get(id_alumno)
        if alumno:
            matricula = Matricula(asignatura_id=asignatura_id, grupo_id=grupo_id)
            if matricula not in alumno.matriculas:
                alumno.matriculas.append(matricula)
            return alumno
        return None

    def desmatricular_alumno(self, id_alumno: str, asignatura_id: str, grupo_id: str) -> Optional[Alumno]:
        alumno = self.alumnos.get(id_alumno)
        if alumno:
            alumno.matriculas = [
                m for m in alumno.matriculas
                if not (m.asignatura_id == asignatura_id and m.grupo_id == grupo_id)
            ]
            return alumno
        return None
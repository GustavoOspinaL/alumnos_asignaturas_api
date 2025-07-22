from typing import Optional
from app.models import Alumno, Matricula
from app.repositories import AlumnoRepository

class AlumnoService:
    def __init__(self):
        self.repo = AlumnoRepository()

    def crear_alumno(self, alumno: Alumno) -> Alumno:
        return self.repo.guardar_alumno(alumno)

    def obtener_alumno(self, id_alumno: str) -> Optional[Alumno]:
        return self.repo.obtener_alumno_por_id(id_alumno)

    def actualizar_alumno(self, id_alumno: str, nuevos_datos: Alumno) -> Optional[Alumno]:
        alumno_existente = self.repo.obtener_alumno_por_id(id_alumno)
        if not alumno_existente:
            return None
        alumno_existente.nombre = nuevos_datos.nombre
        alumno_existente.apellidos = nuevos_datos.apellidos
        alumno_existente.dni = nuevos_datos.dni
        return self.repo.actualizar_alumno(id_alumno, alumno_existente)

    def eliminar_alumno(self, id_alumno: str) -> bool:
        return self.repo.eliminar_alumno(id_alumno)

    def matricular_alumno(self, id_alumno: str, asignatura_id: str, grupo_id: str) -> Optional[Alumno]:
        alumno = self.repo.obtener_alumno_por_id(id_alumno)
        if not alumno:
            return None
        nueva_matricula = Matricula(asignatura_id=asignatura_id, grupo_id=grupo_id)
        alumno.matriculas.append(nueva_matricula)
        return self.repo.actualizar_alumno(id_alumno, alumno)

    def desmatricular_alumno(self, id_alumno: str, asignatura_id: str, grupo_id: str) -> Optional[Alumno]:
        alumno = self.repo.obtener_alumno_por_id(id_alumno)
        if not alumno:
            return None
        alumno.matriculas = [
            m for m in alumno.matriculas
            if not (m.asignatura_id == asignatura_id and m.grupo_id == grupo_id)
        ]
        return self.repo.actualizar_alumno(id_alumno, alumno)
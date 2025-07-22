from app.models import Asignatura
from app.repositories import AsignaturaRepository

class AsignaturaService:
    def __init__(self):
        self.repo_asignatura = AsignaturaRepository()

    def crear_asignatura(self, asignatura: Asignatura) -> Asignatura:
        return self.repo_asignatura.guardar_asignatura(asignatura)

    def obtener_asignatura(self, id: str):
        asignatura = self.repo_asignatura.obtener_asignatura(id)
        if not asignatura:
            raise ValueError("Asignatura no encontrada")
        return asignatura

    def actualizar_asignatura(self, id: str, nuevos_datos: Asignatura):
        actualizado = self.repo_asignatura.actualizar_asignatura(id, nuevos_datos)
        if not actualizado:
            raise ValueError("Asignatura no encontrada")
        return nuevos_datos

    def eliminar_asignatura(self, id: str):
        eliminado = self.repo_asignatura.eliminar_asignatura(id)
        if not eliminado:
            raise ValueError("No se pudo eliminar asignatura")
        return True
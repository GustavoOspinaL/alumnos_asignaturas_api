from app.models import Asignatura

class AsignaturaRepository:
    def __init__(self):
        self.asignaturas = {
            "ASIG001": Asignatura(
                id="ASIG001",
                nombre="Matemáticas I",
                creditos=6,
                cuatrimestre=1,
                curso_id="CURSO1"
            ),
            "ASIG002": Asignatura(
                id="ASIG002",
                nombre="Programación",
                creditos=8,
                cuatrimestre=1,
                curso_id="CURSO1"
            ),
            "ASIG003": Asignatura(
                id="ASIG003",
                nombre="Física I",
                creditos=6,
                cuatrimestre=2,
                curso_id="CURSO2"
            ),
            "ASIG004": Asignatura(
                id="ASIG004",
                nombre="Bases de Datos",
                creditos=7,
                cuatrimestre=2,
                curso_id="CURSO2"
            ),
        }

    def guardar_asignatura(self, asignatura: Asignatura):
        self.asignaturas[asignatura.id] = asignatura

    def obtener_asignatura(self, id: str) -> Asignatura | None:
        return self.asignaturas.get(id)

    def eliminar_asignatura(self, id: str) -> bool:
        return self.asignaturas.pop(id, None) is not None

    def actualizar_asignatura(self, id: str, nuevos_datos: Asignatura) -> bool:
        if id in self.asignaturas:
            self.asignaturas[id] = nuevos_datos
            return True
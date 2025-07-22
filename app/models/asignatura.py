from pydantic import BaseModel

class Asignatura(BaseModel):
    id: str
    nombre: str
    creditos: int
    cuatrimestre: int

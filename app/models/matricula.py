from pydantic import BaseModel

class Matricula(BaseModel):
    asignatura_id: str
    grupo_id: str
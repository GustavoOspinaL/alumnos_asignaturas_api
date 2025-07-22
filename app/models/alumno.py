from pydantic import BaseModel
from typing import List, Optional
from app.models.matricula import Matricula

class Alumno(BaseModel):
    id: Optional[str] = None
    nombre: str
    apellidos: str
    dni: str
    matriculas: List[Matricula] = []
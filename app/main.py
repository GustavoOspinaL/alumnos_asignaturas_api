from fastapi import FastAPI
from app.api.alumno_router import router as alumno_router
from app.api.asignatura_router import router as asignatura_router

app = FastAPI(title="API de Gestión de Alumnos")

app.include_router(alumno_router)
app.include_router(asignatura_router)
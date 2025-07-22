# 📚 API de Gestión de Alumnos y Asignaturas

Esta API permite gestionar información de alumnos, asignaturas y su matriculación en cursos y grupos. Implementada con **FastAPI**, es ideal para entornos educativos o sistemas académicos.

---

## 🚀 Tecnologías Usadas

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic

---

## 🔧 Requisitos Previos

- Tener instalado [Python 3.10+](https://www.python.org/downloads/)
- Tener instalado `pip` y Git

---

## ⚙️ Instalación y Ejecución

1. **Clonar el repositorio**

```bash
git clone https://github.com/GustavoOspinaL/alumnos_asignaturas_api/
cd alumnos_asignaturas_api
```

2. **Crear un entorno virtual y activarlo**

```bash
python3 -m venv env
source env/bin/activate  # En Mac/Linux
```

3. **Instalar dependencias**

```bash
pip3 install -r requirements.txt
```

4. **Ejecutar el servidor**

```bash
uvicorn main:app --reload
```

Esto iniciará la API en `http://127.0.0.1:8000`

---

## 📘 Documentación Automática

Una vez levantado el servidor, puedes acceder a la documentación Swagger:

- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

O a la alternativa ReDoc:

- [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 Endpoints Principales

### Alumnos

- `POST /alumnos/`: Crear nuevo alumno
- `GET /alumnos/{id}`: Obtener alumno por ID
- `PUT /alumnos/{id}`: Actualizar datos de un alumno
- `DELETE /alumnos/{id}`: Eliminar alumno
- `POST /alumnos/{id}/matricular`: Matricular alumno
- `POST /alumnos/{id}/desmatricular`: Desmatricular alumno

### Asignaturas

- `POST /asignaturas/`: Crear nueva asignatura
- `GET /asignaturas/{id}`: Obtener asignatura por ID
- `PUT /asignaturas/{id}`: Actualizar asignatura
- `DELETE /asignaturas/{id}`: Eliminar asignatura

---

## 📌 Notas

- La base de datos utilizada actualmente es **en memoria (diccionarios)**.
- Es ideal para pruebas o desarrollo inicial.

---

## 📄 Licencia

MIT License © 2025

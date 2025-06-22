# API CRUD de Alumnos con FastAPI y Excel

Este proyecto implementa una API RESTful usando **FastAPI** que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una "base de datos" de alumnos almacenada en un archivo **Excel (`BDAlumnos.xlsx`)**. Toda la lógica está implementada en el archivo `CRUD.py`.

---

## Cómo ejecutar el servidor

1. Asegúrate de tener el archivo `BDAlumnos.xlsx` en la misma carpeta que `CRUD.py`.
2. Ejecuta el servidor con Uvicorn:

```bash
uvicorn CRUD:app --reload
```

> El parámetro `--reload` permite recargar automáticamente los cambios sin reiniciar el servidor.

3. Abre tu navegador y ve a la documentación interactiva:
   - Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## Estructura esperada del archivo Excel

El archivo `BDAlumnos.xlsx` debe contener las siguientes columnas:

- `MATRICULA` (int)
- `NOMBRE` (str)
- `EDAD` (int)
- `FACULTAD` (str)
- `INSCRIPCION` (str)
- `GRADO` (str)
- `CARRERA` (str)
- `CORREO` (str)
- `MATERIA` (str)
- `GENERO` (str)

---

## Endpoints disponibles

### 📥 `GET /Alumno/`
Obtiene todos los alumnos registrados.

---

### ➕ `POST /Alumno/`
Agrega un nuevo alumno.

- Body (JSON):
```json
{
  "MATRICULA": 101,
  "NOMBRE": "ANA PÉREZ",
  "EDAD": 22,
  "FACULTAD": "Computación",
  "INSCRIPCION": "Regular",
  "GRADO": "5",
  "CARRERA": "Software",
  "CORREO": "ana.perez@correo.com",
  "MATERIA": "Inteligencia Artificial",
  "GENERO": "Femenino"
}
```

---

### `PUT /Alumno/`
Actualiza los datos de un alumno ya registrado.

- Body (JSON): igual al `POST`, pero con una matrícula existente.

---

### `DELETE /Alumno/{matricula}`
Elimina al alumno con la matrícula proporcionada.

- Ejemplo: `DELETE /Alumno/101`

---

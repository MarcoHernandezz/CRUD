import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel


app= FastAPI()
df = pd.read_excel('BDAlumnos.xlsx', engine='openpyxl')

class Alumno(BaseModel):
    MATRICULA: int
    NOMBRE: str
    EDAD: int
    FACULTAD: str
    INSCRIPCION: str
    GRADO: str
    CARRERA: str
    CORREO: str
    MATERIA: str
    GENERO: str

@app.get("/Alumno/")
async def GetAlumnos():
    GetAlumnos = df[['MATRICULA','NOMBRE','EDAD','FACULTAD','INSCRIPCION','GRADO','CARRERA','CORREO','MATERIA','GENERO']]
    return GetAlumnos.to_dict(orient='records')



@app.post("/Alumno/")   
async def PostAlumno(user: Alumno):
    global df

    if user.MATRICULA in df['MATRICULA'].values:
        return {"error": "El usuario ya existe"}

    nuevo_usuario = pd.DataFrame([user.dict()])
    df = pd.concat([df, nuevo_usuario], ignore_index=True)
    df.to_excel('BDAlumnos.xlsx', index=False, engine='openpyxl')

    return {"mensaje": "Usuario agregado", "usuario": user}


@app.put('/Alumno/')
async def PutAlumno(user: Alumno):
    global df
    
    if user.MATRICULA not in df['MATRICULA'].values:
        return {"error": "Alumno no encontrado"}

    index = df[df['MATRICULA'] == user.MATRICULA].index[0]
    df.loc[index] = user.dict()
    df.to_excel('BDAlumnos.xlsx', index=False, engine='openpyxl')

    return {"mensaje": "Alumno actualizado correctamente", "alumno": user}


@app.delete("/Alumno/{matricula}")
async def DeleteAlumno(matricula: int):
    global df

    if matricula not in df['MATRICULA'].values:
        return {"error": "Alumno no encontrado"}

    df = df[df['MATRICULA'] != matricula]

    df.to_excel('BDAlumnos.xlsx', index=False, engine='openpyxl')

    return {"mensaje": f"Alumno con matrícula {matricula} eliminado correctamente"}


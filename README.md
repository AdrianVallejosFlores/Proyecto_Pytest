# Preparar entorno de Python + pytest en Windows

Guía rápida con todos los pasos, comandos exactos y posibles arreglos. Todo se ejecuta en **CMD** salvo que se indique lo contrario.

---

## 1. Verificar qué versiones de Python tienes instaladas

```cmd
py --list
```

Te muestra todas las versiones detectadas por el launcher. El `*` indica cuál es la versión por defecto.

**Alternativa (PowerShell):** el mismo comando funciona igual en PowerShell.

Si `py` no responde nada, prueba:

```cmd
where python
where python3
```

---

## 2. Ver la versión instalada de forma directa

```cmd
python --version
```

o

```cmd
python -V
```

---

## 3. Revisar si hay una actualización disponible (winget)

```cmd
winget list Python.Python.3.14
```

Esto muestra la versión instalada vs. la disponible en una tabla.

---

## 4. Actualizar Python a la última versión (misma rama, ej. 3.14.x)

```cmd
winget upgrade Python.Python.3.14
```

> ⚠️ Esto actualiza el "patch" (ej. 3.14.0 → 3.14.7). Es seguro y no rompe compatibilidad.
> Si quieres cambiar de versión mayor (ej. 3.13 → 3.14), revisa antes que tus librerías sean compatibles.

**Confirmar que se actualizó:**

```cmd
py --list
```

---

## 5. Instalar pytest

```cmd
pip install pytest
```

**Instalar junto con extensiones comunes (opcional, según el proyecto):**

```cmd
pip install pytest pytest-cov pytest-mock
```

| Librería | Para qué sirve |
|---|---|
| `pytest-cov` | Cobertura de código |
| `pytest-mock` | Mockear objetos/funciones |
| `pytest-asyncio` | Probar código `async`/`await` |
| `pytest-xdist` | Correr tests en paralelo |
| `faker` | Generar datos falsos de prueba |

---

## 6. Problema común: "pytest no se reconoce como un comando"

Esto pasa cuando pip instala en una carpeta que no está en el `PATH`, por ejemplo:

```
C:\Users\<usuario>\AppData\Roaming\Python\Python314\Scripts
```

### Arreglo permanente (agregar al PATH)

1. En el buscador de la Maquina escribe **Variables de Entorno**
2. En la Pestaña **Opciones avanzadas** selecciona el botón **Variables de entorno**
3. En "Variables de usuario", selecciona `Path` → **Editar**
4. **Nuevo** → pega la ruta (Fijarse en cambiar el usuario de acuerdo a su propio entorno):
   ```
   C:\Users\<usuario>\AppData\Roaming\Python\Python314\Scripts
   ```
5. Aceptar todo y **cerrar y volver a abrir CMD**

**Confirmar que ya funciona:**

```cmd
pytest --version
```
---

## 7. Guardar dependencias del proyecto

```cmd
pip freeze > requirements.txt
```

**Instalar esas mismas dependencias después (en otra máquina o tras clonar el repo):**

```cmd
pip install -r requirements.txt
```

---

## 9. Correr los tests
 
Desde la carpeta raíz del proyecto:
 
```cmd
pytest
```
 
o si `pytest` no está en el PATH:
 
```cmd
python -m pytest
```
 
---
 
## 8. Código simple para validar que pytest funciona (VS Code)
 
Crea un archivo llamado `test_basico.py` en la raíz del proyecto con esto:
 
```python
# test_basico.py
 
def sumar(a, b):
    return a + b
 
def test_sumar():
    assert sumar(2, 3) == 5
 
def test_sumar_negativos():
    assert sumar(-1, -1) == -2
```
 
### Correrlo desde la terminal de VS Code
 
1. Abre la carpeta del proyecto en VS Code
2. Abre la terminal integrada: `` Ctrl + ` ``
3. Si usas entorno virtual, actívalo primero (ver punto 7)
4. Corre:
```cmd
   pytest
```
   o
```cmd
   python -m pytest
```
 
Si todo salió bien, deberías ver algo como:
 
```
test_basico.py ..                                                      [100%]
2 passed in 0.01s
```
 
## Resumen express (orden recomendado)
 
```cmd
py --list
winget upgrade Python.Python.3.14
python -m venv venv
venv\Scripts\activate
pip install pytest
pip freeze > requirements.txt
pytest
```
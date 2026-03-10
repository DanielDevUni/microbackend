# 🗂️ Microbackend de Tareas en Django + DRF + Swagger

Este repositorio contiene un **microbackend sencillo** para gestionar tareas (to-do list).  
Expone una API REST con endpoints para **listar**, **crear** y **completar** tareas.  
La documentación de la API está disponible en Swagger para facilitar el trabajo del frontend.

---

## 📥 Instalación y ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/DanielDevUni/microbackend.git
cd microbackend_demo
```
### 2. Crear entorno virtual (opcional pero recomendado)
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Migrar base de datos
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Levantar el servidor
```bash
python manage.py runserver
```
#### El backend estará disponible en: http://127.0.0.1:8000/ (Asegurate del puerto que aparezca en consola)
___
## 🌐 Navegación en el backend

### Endpoint

* #### Listar tareas (GET)
    ```bash
    http://127.0.0.1:8000/tasks/
    ```
    Devuelve todas las tareas en formato JSON.

* #### Crear tareas (POST)
    ```bash
    http://127.0.0.1:8000/tasks/create/
    ```
    #### Body esperado en JSON.
    ```bash
    {
    "title": "Estudiar Django"
    }
    ```
* #### Completa tarea (POST)
    ```bash
    http://127.0.0.1:8000/tasks/<id>/complete/
    # Ejemplo
    http://127.0.0.1:8000/tasks/1/complete/
    ```
___
# 📖 Documentación con Swagger
#### Swagger está dispinible en
```bash
http://127.0.0.1:8000/swagger/
```

#### Allí encontrarás:

* Descripción de cada endpoint.
* Ejemplos de los JSON que debe enviar el frontend.
* Respuestas esperadas del backend.

También puedes usar:
```bash
http://127.0.0.1:8000/redoc/
```
para una vista alternativa de la documentación.
___
# 🔎 ¿Por qué este código es un microbackend?
Es importante diferenciarlo de un backend monolítico y de un microservicio por endpoint:

* No es un backend monolítico:  
Un backend tradicional suele manejar múltiples dominios (usuarios, pagos, inventario, notificaciones) en un solo proyecto grande. Aquí, en cambio, este servicio se centra solo en tareas, con independencia del resto del sistema.

* No es un microservicio por endpoint:  
Un microservicio por endpoint sería separar cada acción en un servicio distinto (uno para listar, otro para crear, otro para completar). Eso genera demasiada fragmentación y sobrecarga.
En este caso, todos los endpoints relacionados con tareas están agrupados en un único servicio, lo que mantiene la coherencia funcional.

Es un microbackend porque:

* Tiene una responsabilidad única y clara: gestionar tareas.
* Puede desplegarse y mantenerse de forma independiente.
* Se integra fácilmente con otros microbackends (ej. usuarios, pagos, notificaciones).
* Está documentado y preparado para ser consumido por el frontend sin necesidad de conocer la lógica interna.
___
# ✅ Conclusión
Este microbackend está diseñado para ser simple y modular, ideal para que el frontend pueda:

* Descargar el repositorio.
* Instalar dependencias.
* Levantar el servidor.
* Navegar fácilmente los endpoints documentados en Swagger.
* De esta forma, el trabajo de integración será mucho más rápido y claro.
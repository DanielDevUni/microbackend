from django.http import JsonResponse
from .models import Task
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Task

# Listar tareas
@swagger_auto_schema(
    method="get",
    operation_description="Obtiene la lista completa de tareas registradas.",
    responses={200: "Lista de tareas en formato JSON"}
)
@api_view(["GET"])
def list_tasks(request):
    tasks = list(Task.objects.values())
    return Response(tasks)

# Crear tarea
@swagger_auto_schema(
    method="post",
    operation_description="Crea una nueva tarea. El frontend debe enviar un JSON con el campo 'title'.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING, description='Título de la tarea')
        },
        required=['title']
    ),
    responses={201: "Tarea creada exitosamente"}
)
@api_view(["POST"])
def create_task(request):
    title = request.data.get("title")
    task = Task.objects.create(title=title)
    return Response({"id": task.id, "title": task.title, "completed": task.completed}, status=201)

# Completar tarea
@swagger_auto_schema(
    method="post",
    operation_description="Marca una tarea como completada. El frontend debe enviar el ID de la tarea en la URL.",
    responses={200: "Tarea marcada como completada", 404: "Tarea no encontrada"}
)
@api_view(["POST"])
def complete_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.completed = True
        task.save()
        return Response({"id": task.id, "title": task.title, "completed": task.completed})
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=404)


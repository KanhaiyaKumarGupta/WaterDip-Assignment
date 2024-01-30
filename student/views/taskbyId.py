from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from student.models import Task
from django.core.exceptions import ObjectDoesNotExist

@csrf_exempt
@require_http_methods(["GET"])  
def getTaskById(request, task_id):
    if request.method == "GET":
        try:
            task = Task.objects.get(id=task_id)  
            task_data = {
                "id": task.id,
                "title": task.title,
                "is_completed": task.is_completed
            }
            return JsonResponse({"task": task_data}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({"error": "There is no task at that id"}, status=404)
        except Exception as e:
            return JsonResponse({"error": "Internal Server Error"}, status=500)

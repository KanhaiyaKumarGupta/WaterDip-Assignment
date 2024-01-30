from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from student.models import Task
from django.core.exceptions import ObjectDoesNotExist


@csrf_exempt
@require_http_methods(["DELETE"]) 
def deleteTaskById(request, task_id):
    if request.method == "DELETE":
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
            return JsonResponse({"message": "Task deleted successfully"}, status=200)

        except Task.DoesNotExist:
            return JsonResponse({"error": "Task not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": "Internal Server Error"}, status=500)

    else:
        return JsonResponse({"error": "Invalid Request"}, status=404)

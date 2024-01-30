import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from student.models import Task

@csrf_exempt
@require_http_methods(["PUT"])
def updateTask(request, task_id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            task = Task.objects.get(id=task_id)
            task.title = data.get("title", task.title) 
            task.is_completed = data.get("is_completed", task.is_completed)  
            task.save()
            return JsonResponse({"message": "Task updated successfully"}, status=200)

        except Task.DoesNotExist:
            return JsonResponse({"error": "There is no task at that id"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        except Exception as e:
           return JsonResponse({"error": str(e)}, status=500)
    else :
        return JsonResponse({"error":"Invalid Request"},status = 404)

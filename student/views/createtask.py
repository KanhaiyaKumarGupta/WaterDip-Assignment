from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt 
from student.models import Task
import json

@csrf_exempt  
def createTask(request):
    if request.method == "POST":
        try:
          data = json.loads(request.body)
          task = Task(title=data["title"], is_completed=data["is_completed"])
          task.save()

          return JsonResponse({"id": task.id}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    else:
        return JsonResponse({"error": "Invalid Request"}, status=400)


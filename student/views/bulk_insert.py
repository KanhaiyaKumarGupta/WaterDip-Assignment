import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from student.models import Task


@csrf_exempt
def bulk_insert_tasks(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            task_data = data.get("tasks", [])

            tasks = [
                Task(title=task["title"], is_completed=task["is_completed"])
                for task in task_data
            ]
            created_tasks = Task.objects.bulk_create(tasks, ignore_conflicts=True)
            task_ids = [{"id": task.id} for task in created_tasks]
            return JsonResponse({"tasks": task_ids}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except KeyError as e:
            return JsonResponse({"error": f"Missing key in the data: {e}"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)

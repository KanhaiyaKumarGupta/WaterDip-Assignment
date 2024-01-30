from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from student.models import Task


@csrf_exempt
@require_http_methods(["GET"])  
def getAllTasks(request):
    if request.method == 'GET':
        try:
            tasks = Task.objects.all()  # Retrieves all Task objects
            task_list = [
                {
                    'id': task.id,
                    'title': task.title,
                    'is_completed': task.is_completed
                } for task in tasks
            ]
            return JsonResponse({'tasks': task_list}, status=200)
        
        except Exception as e:
            return JsonResponse({"message": "Error retrieving tasks"}, status=500)
    else:
        
        return JsonResponse({"message": "Invalid Request"}, status=405)

from django.shortcuts import render,HttpResponse
import json
from youssef.tasks import scan
from celery.result import AsyncResult



def home(request):
    if request.method == "POST":
        task = scan.delay(host=request.POST['host'])
        context = {
            'task': task,
        }
    else:
        context = {}
    return render(request, 'youssef/base.html', context)

def get_progress(request, task_id=None):
    result = AsyncResult(task_id)
    response_data = {
        'state': result.state,
        'details': result.info,
    }
    return HttpResponse(json.dumps(response_data), content_type='application/json')

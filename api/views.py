# django related imports
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# app related imports
from .models import Worker, WorkOrder, AssignWorker
from .serializers import WorkerSerializer, WorkOrderSerializer

# rest framework related imports
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

@csrf_exempt
@login_required(login_url='/admin/')
def create_utility(request, to_create):
    if request.method == "POST" or request.method == "PUT":
        print(request)
        print(request.__dict__)
        data = JSONParser().parse(request)
        serializer = None

        if to_create == "worker"     : serializer = WorkerSerializer(data=data) 
        if to_create == "work-order" : serializer = WorkOrderSerializer(data=data)
    
        if serializer is None: return HttpResponse("Invalide utility to create. Check that the url is correct", 404)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    return HttpResponse("Invalid request Method for this URL", 405)
        
@csrf_exempt
@login_required(login_url="/admin")
def delete_worker(request, pk):
    try:
        worker = Worker.objects.get(pk=pk)
    except Worker.DoesNotExist:
        return HttpResponse("Worker does not exists", 404)

    if request.method == "DELETE":
        worker.delete()
        return HttpResponse("Deleted worker", status=204)
    else:
        return HttpResponse("Invalid request Method for this URL", 405)


@csrf_exempt
@login_required(login_url='/admin')
def assign_worker_an_order(request, worker_id, work_order_id):
    try:
        worker = Worker.objects.get(pk=worker_id)
        work_order = WorkOrder.objects.get(pk=work_order_id)
    except (Worker.DoesNotExist, WorkOrder.DoesNotExist):
        return HttpResponse("Either the worker or the work order does not exists", 406)

    if request.method == "POST":
        assigned_workers = AssignWorker.objects.filter(work_order=work_order)
        if assigned_workers.exists():
            if assigned_workers.count() >= 5: return HttpResponse("You are not allowed to assign more than 5 workers to a work order", 406)

        if AssignWorker.objects.filter(Q(work_order=work_order) & Q(worker=worker)).exists():
            return HttpResponse("Worker already assigned to this order", 406)

        try:
            AssignWorker(
                worker=worker,
                work_order=work_order,
            ).save()
            return HttpResponse("Successfully assigned worker", 202)
        except Exception as e:
            return HttpResponse(e)
    else:
        return HttpResponse("Invalid request Method for this URL", 405)

@csrf_exempt
@login_required(login_url="/admin")
def get_work_order(request, pk):
    try:
        worker = Worker.objects.get(pk=pk)
    except Worker.DoesNotExist:
        return HttpResponse("Worker does not exists", 406)

    if request.method == "GET":
        work_orders = AssignWorker.objects.filter(worker=worker)
        work_order_ids = []

        for work_order in work_orders:
            work_order_ids.append(work_order.work_order.id)

        work_order = list(WorkOrder.objects.filter(pk__in=work_order_ids).order_by('deadline'))
        serializer = WorkOrderSerializer(work_order, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse("Invalid request Method for this URL", 405)
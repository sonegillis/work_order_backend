# django rest framework related imports
from rest_framework import serializers

# api related imports
from .models import Worker, WorkOrder, AssignWorker


class WorkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Worker
        fields = ("id", "name", "company_name", "email")

class WorkOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkOrder
        fields = ("id", "title", "description", "deadline")

class AssignWorkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AssignWorker
        fields = ("worker", "work_order")
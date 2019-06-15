from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return "{0} ( {1} ) => {2}".format(self.name, self.email, self.company_name)

class WorkOrder(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    deadline = models.DateField()

    def __str__(self):
        return "{0} ( {1} ) => {2}".format(self.title, self.description, self.deadline)

class AssignWorker(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = [["worker", "work_order"]]
    def __str__(self):
        return "{0} => {1}".format(self.worker.name, self.work_order.title)

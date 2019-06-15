"""work_orders URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# django related imports
from django.contrib import admin
from django.urls import path, include

# api related imports
from api.views import create_utility, delete_worker, assign_worker_an_order, get_work_order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create/<str:to_create>/', create_utility), # we use this single url to match a create/worker or create/work-order/,
    path('api/delete-worker/<int:pk>/', delete_worker),
    path('api/assign-worker-an-order/<int:worker_id>/<int:work_order_id>/', assign_worker_an_order),
    path('api/get/work-orders/<int:pk>/', get_work_order) # we use this url to get the work orders of a particular worker
]
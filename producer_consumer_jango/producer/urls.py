from rest_framework.routers import SimpleRouter
from .views import EmployeeAPI

simpleRouterInstance=SimpleRouter()
simpleRouterInstance.register('employee',EmployeeAPI)
urlpatterns=simpleRouterInstance.urls
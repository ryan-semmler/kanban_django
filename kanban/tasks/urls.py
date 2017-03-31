from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/tasks/$', views.view_all_tasks),

]

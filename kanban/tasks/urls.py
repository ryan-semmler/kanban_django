from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/tasks/$', views.view_all_tasks),
    url(r'^api/tasks/(?P<detail_id>[0-9]+)/$', views.view_task_detail),
    url(r'^api/tasks/(?P<detail_id>[0-9]+)/delete/$', views.delete_task),
    url(r'^api/tasks/create/$', views.new_task),
]

from django.urls import include, path

from . import views

app_name = 'projectList'
urlpatterns = [
    path('', views.projectListView.as_view(), name='project_list'),
    path('<slug:pk>', views.projectView.as_view(), name='projects'),
]
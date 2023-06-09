from django.urls import path

from . import views

app_name = 'projectList'
urlpatterns = [
    path('projects/', views.projectListView.as_view(), name='projectlist'),
    path('projects/<int:pk>', views.projectView.as_view(), name='projects'),
]
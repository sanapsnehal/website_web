from django.urls import path
from events import views
from .views import home,registerclient,all_clients,project,project_list





urlpatterns = [
    path('',views.home,name="home"),
    path('registerclient/',views.registerclient,name='registerclient'),
    path('clientlist',views.all_clients,name="listclient"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request,name="login"),
    path("project", views.project,name="project"),
    path('delete/<int:id>', views.delete,name="delete"),
    path('edit/<int:id>', views.edit,name="edit"),
    path('projectlist',views.project_list,name="projectlist"),

]


from django.urls import path

from . import views

urlpatterns = [
    path('', views.allShows),
    path('createShow/', views.createShow),
    path('addShow/', views.addShow),
    path('displayShow/<int:show_id>', views.displayShow),
    path('editShow/<int:show_id>', views.editShow),
    path('updateShow/<int:show_id>', views.updateShow),
    path('deleteShow/<int:show_id>', views.deleteShow),
]

from django.urls import path
from .views import indexView, createView, updateView, deleteView

urlpatterns = [
    path('', indexView, name='index'),
    path('create/', createView, name='create'),
    path('update/<int:id>/', updateView, name='update'),
    path('delete/<int:id>/', deleteView, name='delete'),
]

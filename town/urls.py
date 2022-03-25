from django.urls import path 
from .views import CreateTown, ListTown ,  ListTown , TownViewset

urlpatterns=[
    path("createTown/" , CreateTown.as_view()),
    path("listTown/" , ListTown.as_view({
            'get':'list'
        })),
    path("town/<str:pk>", TownViewset.as_view({
        'put':'update',
        'delete':'delete'
    }))
]
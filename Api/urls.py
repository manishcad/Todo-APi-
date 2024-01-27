from django.urls import path
from .views import Details,All_Todo,Create_Todo,Single_Todo


urlpatterns=[
    path("",Details.as_view(),name="details"),
    path("all",All_Todo.as_view(),name="all"),
    path("create",Create_Todo.as_view(),name="create"),
    path("todo/<str:pk>",Single_Todo.as_view(),name="single_todo"),
]
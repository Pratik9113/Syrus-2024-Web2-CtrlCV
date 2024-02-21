from home.views import index
from home.views import about ,game1,game2
from django.urls import path
# from pratikwebsite import views
urlpatterns = [
    
    path('', index, name = "index"),
    path('about/', about,name = "about"),
    path('game1/', game1, name = "game1"),
    path('game2/', game2, name = "game2"),
]
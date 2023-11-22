from django.urls import path
from .views import homepage, singles

urlpatterns = [

    path('', homepage, name="home"),
    path('<int:id>/', singles, name='id')

]
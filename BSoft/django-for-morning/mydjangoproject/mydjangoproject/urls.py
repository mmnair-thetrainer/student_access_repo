from django.contrib import admin
from django.urls import path

import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myform/', myapp.views.login, name="login"),
    path('mydash/', myapp.views.view_dashboard, name="view_dashboard"),
]

from django.contrib import admin
from django.urls import path
from.views import WorkList
from . import views

urlpatterns = [

    path('',WorkList.as_view(),name='work' ),

    path('<int:pk>', views.WorkDetailView.as_view(), name='Work_details')
]






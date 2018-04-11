from django.contrib import admin
from django.urls import path
from.views import Past_WorkList
from . import views

urlpatterns = [

    path('',Past_WorkList.as_view(),name='pastwork' ),
    path('<int:pk>', views.Past_WorkDetailView.as_view(), name='Past_Work_details')





]

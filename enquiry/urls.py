
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of enquiry : enquiry_list

    path('', views.enquiryListView.as_view(), name='enquiry_list'),

    # Path to create new enquiry : enquiry_new

    path('new/', views.enquiryCreateView.as_view(), name='enquiry_new'),

    # Path to edit enquiry : edit_list

    path('<int:pk>/edit', views.enquiryUpdateView.as_view(), name='enquiry_edit'),

    # Path to delete enquiry : enquiry_delete

    path('<int:pk>/delete', views.enquiryDeleteView.as_view(), name='enquiry_delete'),

    # Path to detail view of enquiry : enquiry_details

    path('<int:pk>', views.enquiryDetailView.as_view(), name='enquiry_details')
]

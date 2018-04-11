
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of contact_us : contact_us_list

    path('', views.contact_usListView.as_view(), name='contact_us_list'),

    # Path to create new contact_us : contact_us_new

    path('new/', views.contact_usCreateView.as_view(), name='contact_us_new'),

    # Path to edit contact_us : edit_list

    path('<int:pk>/edit', views.contact_usUpdateView.as_view(), name='contact_us_edit'),

    # Path to delete contact_us : contact_us_delete

    path('<int:pk>/delete', views.contact_usDeleteView.as_view(), name='contact_us_delete'),

    # Path to detail view of contact_us : contact_us_details

    path('<int:pk>', views.contact_usDetailView.as_view(), name='contact_us_details')
]

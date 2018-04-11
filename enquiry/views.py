# from django.shortcuts import render


from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create enquiry Here

class enquiryCreateView(CreateView):
    model = models.Enquiry
    template_name = 'enquiry/enquiry_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Enquiry_User','Enquiry_Subject','Enquiry_Message']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# enquiry Details Here


class enquiryDetailView(DetailView):
    model = models.Enquiry
    template_name = 'enquiry/enquiry_detail.html'
    login_url = 'login'

# enquiry ListView Here


class enquiryListView(ListView):
    model = models.Enquiry
    template_name = 'enquiry/enquiry_list.html'
    login_url = 'login'

# enquiry Update Here


class enquiryUpdateView(UpdateView):
    model = models.Enquiry

    # Decide fields for editing Here

    fields = ['Enquiry_User','Enquiry_Subject','Enquiry_Message']
    template_name = 'enquiry/enquiry_update.html'
    login_url = 'login'

# enquiry Delete here


class enquiryDeleteView(DeleteView):
    model = models.Enquiry
    template_name = 'enquiry/enquiry_delete.html'
    success_url = reverse_lazy('enquiry_list')
    login_url = 'login'




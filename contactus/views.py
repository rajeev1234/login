# from django.shortcuts import render


from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create contact_us Here

class contact_usCreateView(CreateView):
    model = models.Contact_Us
    template_name = 'contact_us/contact_us_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Contact_Us_User','Contact_Us_Subject','Contact_Us_Message']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# contact_us Details Here


class contact_usDetailView(DetailView):
    model = models.Contact_Us
    template_name = 'contact_us/contact_us_detail.html'
    login_url = 'login'

# contact_us ListView Here


class contact_usListView(ListView):
    model = models.Contact_Us
    template_name = 'contact_us/contact_us_list.html'
    login_url = 'login'

# contact_us Update Here


class contact_usUpdateView(UpdateView):
    model = models.Contact_Us

    # Decide fields for editing Here

    fields = ['Contact_Us_User','Contact_Us_Subject','Contact_Us_Message']
    template_name = 'contact_us/contact_us_update.html'
    login_url = 'login'

# contact_us Delete here


class contact_usDeleteView(DeleteView):
    model = models.Contact_Us
    template_name = 'contact_us/contact_us_delete.html'
    success_url = reverse_lazy('contact_us_list')
    login_url = 'login'




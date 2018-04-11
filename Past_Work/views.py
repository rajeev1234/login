from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView,DetailView
from . import models

# def Past_Work(request):
#     form = Past_Work_form(request.POST)
#     if form.is_valid():
#         form.save()
#     return render(request,'Past_Work.html',{'form':form})


class Past_WorkList(ListView):
    model = models.Past_Work
    template_name = 'Past_Work/Past_Work_List.html'
    login_url = 'login'


class Past_WorkDetailView(LoginRequiredMixin, DetailView):
        model = models.Past_Work
        template_name = 'Past_Work/Past_Work_details.html'
        login_url = 'login'
from django.views.generic import ListView,DetailView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin

# def Past_Work(request):
#     form = Past_Work_form(request.POST)
#     if form.is_valid():
#         form.save()
#     return render(request,'Past_Work.html',{'form':form})


class WorkList(ListView):
    model = models.Work
    template_name = 'Work/Work_List.html'
    login_url = 'login'



class WorkDetailView(LoginRequiredMixin, DetailView):
    model = models.Work
    template_name = 'Work/Work_Details.html'
    login_url = 'login'

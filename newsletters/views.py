
# Create your views here.
from django.shortcuts import render
from .forms import newsform
from .models import news
from django.http import Http404,HttpResponseRedirect

from django.core.mail import send_mail

import uuid
from django.conf import settings

def get_ip(request):
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = ""
    return ip


def get_ref_id():
    ref_id = str(uuid.uuid4())[:11].replace('-' ,'').lower()
    try:
        id_exist = news.objects.get(ref_id=ref_id)
        get_ref_id()
    except:
        return ref_id

def share(request, ref_id):
    try:
        join_obj = news.objects.get(ref_id=ref_id)
        friends_referred = news.objects.filter(friend=join_obj)
        count = join_obj.referral.all().count()
        ref_url=settings.SHARE_URL + str(join_obj.ref_id)
        context = {"ref_id":join_obj.ref_id,"ref_url":ref_url,"count":count}
        template = "share.html"
        return render(request,template,context)
    except:
         raise Http404





def Newsletter(request):
    try:

        join_id = request.session['join_id_ref']
        obj = news.objects.get(id=join_id)
    except:
        obj = None

    #print (request.META.get("REMOTE_ADDR"))
    form = newsform(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit=False)
        name = form.cleaned_data['name']



        email = form.cleaned_data['email']
        new_join_old,created = news.objects.get_or_create(email=email)
        if created:
            new_join_old.ref_id=get_ref_id()
            if not obj == None:
                new_join_old.friend=obj
            new_join_old.ip_address=get_ip(request)
            new_join_old.save()
            subject ='Welcome FORMFILM'
            message = 'Hey welcome to film . ' \
                      'Join Us Here' \
                      'http://workforfilms.com/'
            from_email = settings.EMAIL_HOST_USER
            to_list = [new_join.email]
            send_mail(subject=subject,message=message,from_email=from_email,recipient_list=to_list,fail_silently=False)
        return HttpResponseRedirect("/%s" %(new_join_old.ref_id))
    context = {"form":form}
    template = "newsletter.html"
    return render(request, template , context )


# queryset = news.objects.all()
# data1 = ('my','message','lskajf@gail.com',[queryset])
# data2 = ('my2','message2','lskdsfsdajf@gail.com',[queryset])
# send_mass_mail((data1,data2),fail_silently = False)




from django.shortcuts import render, redirect
from .template_filters.filters import ENV 
import json 
from .forms import *
from django.http import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
import imgkit 
from django.db.models import Q
# Create your views here.

def login_required(func):
    def inner(request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('login')
        return func(request, *args, **kwargs)
    return inner

@login_required
def frame_nft(request):
    if request.method == 'GET':
        form = FrameForm(initial={"template": Template.objects.filter(Q(user=request.user)|Q(user__username='admin'))})
        return render(request, 'framer.html', {"form": form})
    else:
        form = FrameForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            template = form.cleaned_data['template']

            t = ENV.from_string(template.value)    
            template_vars = json.loads(template.variables)
            
            if not template_vars:
                template_vars = {}
            
            html = t.render(**template_vars)
            img_content = imgkit.from_string(html, None)
            return HttpResponse(img_content, content_type='image/png')
        else:
            print("INVALID FORM. Errors: ", form.errors)
            return render(request, 'framer.html', {"form": form})

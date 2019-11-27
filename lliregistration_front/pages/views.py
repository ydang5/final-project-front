from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect


# ---- homepage -----

def index_page(request):

    return render(request,'pages/homepage/index.html',{})



def contact_page(request):
    context = {}

    return render(request,'pages/homepage/contact.html',context)

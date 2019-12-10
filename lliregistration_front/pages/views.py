from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect


# ---- homepage -----

def index_page(request):

    return render(request,'pages/homepage/index.html',{})



def contact_page(request):
    context = {}

    return render(request,'pages/homepage/contact.html',context)


# ---- gateway -----

def login_page(request):
    context = {}

    return render(request,'pages/gateway/login.html',context)


def logout_page(request):
    context = {}

    return render(request,'pages/gateway/logout.html',context)


# ---- platform -----


def platform_page(request):

    context = {}
    return render(request,'pages/platform/platform.html',context)

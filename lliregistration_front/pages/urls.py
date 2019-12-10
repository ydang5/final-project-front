from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

urlpatterns = [
    # homepage
    path('', views.index_page, name='index'),
    path('contact', views.contact_page,name='contact'),
    # gateway
    path('login', views.login_page,name='login'),
    path('logout', views.logout_page,name='logout'),
    # dashboard
    path('platform', views.platform_page, name='platform_page'),

]

urlpatterns = format_suffix_patterns(urlpatterns)

from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import Eleven, Banner, Logo


# Create your views here.

def home_page_view(request):
    eleven_6 = Eleven.objects.all().order_by('name')[0:6]
    banner = Banner.objects.all()
    logo = Logo.objects.all()
    context = {
        'eleven_six' : eleven_6,
        'banner': banner,
        'logo': logo
    }

    return render(request, 'index.html', context)

class ElevenListView(ListView):
    model = Eleven
    template_name = 'shop.html'

class ElevenAboutView(TemplateView):
    template_name = 'about.html'

class ElevenContactView(TemplateView):
    template_name = 'contact.html'

class ElevenDetailView(DetailView):
    model = Eleven
    template_name = 'product-details.html'
    context_object_name = 'eleven'
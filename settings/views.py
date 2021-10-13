from django.shortcuts import render, redirect
from django.contrib import messages

from settings.forms import SendMessageForm
from settings.models import homemodel, About, FitnessMonitor, Team, ImagePost, Founder, Philosophy, Corporate_solve, \
    Pricing, Sub_Pricing, Blog, SocialMedia, Sub_Philosophy, sendMessage


# Kurumsal Alanlar(Kurucu,felsefe,Kurumsal,Çözümlemeler
def about(request):
    template = 'home/homepages/about.html'
    home_data = homemodel.objects.all()
    abouts_data = About.objects.all()
    fitnessmonitor_data = FitnessMonitor.objects.all()
    team_data = Team.objects.all()
    context = {
        'homes': home_data,
        'abouts': abouts_data,
        'fitnessMonitors': fitnessmonitor_data,
        'teams': team_data,

    }
    return render(request=request, template_name=template, context=context)


def founder(request):
    template = 'home/homepages/founder.html'
    home_data = homemodel.objects.all()
    abouts_data = About.objects.all()
    fitnessmonitor_data = FitnessMonitor.objects.all()
    team_data = Team.objects.all()
    founder_data = Founder.objects.all()
    philosophy_data = Philosophy.objects.all()
    corporate_data = Corporate_solve.objects.all()
    pricing_data = Pricing.objects.all()
    sub_pricings = Sub_Pricing.objects.all()
    blog_data = Blog.objects.all()
    social_data = SocialMedia.objects.all()
    context = {
        'homes': home_data,
        'abouts': abouts_data,
        'fitnessMonitors': fitnessmonitor_data,
        'teams': team_data,
        'founders': founder_data,
        'philosophys': philosophy_data,
        'corporates': corporate_data,
        'pricings': pricing_data,
        'subPricings': sub_pricings,
        'blogs': blog_data,
        'socials': social_data,
    }
    return render(request=request, template_name=template, context=context)


def philosophy(request):
    template = 'home/homepages/philosophy.html'
    home_data = homemodel.objects.all()
    fitnessmonitor_data = FitnessMonitor.objects.all()
    philosophys_data=Philosophy.objects.all()
    sphilosopy_data=Sub_Philosophy.objects.all()
    context = {
        'homes': home_data,
        'fitnessMonitors': fitnessmonitor_data,
        'philosophys': philosophys_data,
        'subphilosopys':sphilosopy_data
    }
    return render(request=request, template_name=template, context=context)


def corpsolve(request):
    template = 'home/homepages/corpsolve.html'
    home_data = homemodel.objects.all()
    fitnessmonitor_data = FitnessMonitor.objects.all()
    corpsolve_data=Corporate_solve.objects.all()
    context = {
        'homes': home_data,
        'fitnessMonitors': fitnessmonitor_data,
        'corpsolves':corpsolve_data,

    }
    return render(request=request, template_name=template, context=context)

def fitnessMonitor(request,id):
    template = 'home/homepages/fitnessmonitor.html'
    home_data = homemodel.objects.all()
    fitnessmonitor_data = FitnessMonitor.objects.all()
    fitnessmonitor_filter=FitnessMonitor.objects.filter(id=id)
    context = {
        'homes': home_data,
        'fitnessMonitors': fitnessmonitor_data,
        'monfilters':fitnessmonitor_filter,

    }
    return render(request=request, template_name=template, context=context)


def contact(request):
    template = 'home/homepages/contact.html'
    home_data = homemodel.objects.all()
    fitnessmonitor_data = FitnessMonitor.objects.all()
    context = {
        'homes': home_data,
        'fitnessMonitors': fitnessmonitor_data,

    }
    return render(request=request, template_name=template, context=context)

def contactcreate(request):
    if request.method == 'POST':
        sent_form = SendMessageForm(request.POST)
        if sent_form.is_valid():
            sent_form.save()
            messages.success(request, message='Kayıt Başaraılı')
            return redirect('home-contact')
        else:
            messages.warning(request, 'İşlem başarısız')
            print('***********************************************************************************')
            print(sent_form.errors)
            print('**********************************************************************************')

    return redirect('home-contact')
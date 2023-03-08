from django.shortcuts import render
from main.models import Menu
from django.http import HttpResponse

def home(request):
    menu_objects = Menu.objects.all()
    menu_dict = {'main': menu_objects.filter(parent=None)}
    return render(request, 'home/index.html', context={'menu_dict': menu_dict})

def sections(request, section_path):
    sections = section_path.split('/')
    menu_objects = Menu.objects.all()
    menu_dict = {'main': menu_objects.filter(parent=None), }
    try:
        for section in sections:
            section_pk = menu_objects.get(slug=section).pk
            menu_dict.update({section: menu_objects.filter(parent=section_pk)})
    except Menu.DoesNotExist:
        return HttpResponse(status=404)
    
    return render(request, 'sections/index.html', context={'menu_dict': menu_dict})

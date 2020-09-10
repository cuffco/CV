from django.shortcuts import render


def profil(request):
    """
    :param request: None
    :return: HomePage
    """
    return render(request, 'profil.html', locals())


def services(request):
    """
    :param request: None
    :return: HomePage
    """
    return render(request, 'services.html', locals())

def projets(request):
    """
    :param request: None
    :return: HomePage
    """
    return render(request, 'projets.html', locals())
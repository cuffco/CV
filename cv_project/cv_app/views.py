from django.shortcuts import render


def profil(request):
    """
    :param request: None
    :return: HomePage
    """
    return render(request, 'profil.html', locals())

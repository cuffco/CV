from django.shortcuts import render


def homepage(request):
    """
    :param request: None
    :return: HomePage
    """
    return render(request, 'homepage.html', locals())

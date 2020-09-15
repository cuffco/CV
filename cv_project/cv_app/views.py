from django.shortcuts import render
from .forms import ContactForm, ParagraphErrorList
from .models import Contact


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


def projects(request):
    """
    :param request: None
    :return: HomePage
    """
    return render(request, 'projects.html', locals())


def get_contact(request):
    form = ContactForm(request.POST, error_class=ParagraphErrorList)
    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        phone_number = form.cleaned_data['phone_number']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        contact = Contact.objects.create(first_name=first_name,
                                         last_name=last_name,
                                         phone_number=phone_number,
                                         email=email, message=message)
        contact.save()
        form = ContactForm()
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

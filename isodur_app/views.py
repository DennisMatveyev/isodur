from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView

from .forms import ContactForm
from .models import Project, Partner, Product1


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        from django.utils.translation import get_language_from_request, get_language_from_path, activate
        activate(get_language_from_path(request.path))
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['partners'] = Partner.objects.all()
        return context


class CompanyView(TemplateView):
    template_name = 'company.html'


class ProductListView(ListView):
    model = Product1
    context_object_name = 'products'
    template_name = 'products/product_1.html'


class Product2(TemplateView):
    template_name = 'products/product_2.html'


class Product3(TemplateView):
    template_name = 'products/product_3.html'


class ProjectVideoView(TemplateView):
    template_name = 'project_video.html'


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'project_list.html'


def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            marketing = form.cleaned_data['marketing']
            message = 'From: {}\n{}'.format(name, form.cleaned_data['message'])

            recipients = [settings.EMAIL_HOST_USER]
            try:
                send_mail(marketing, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'contacts_thanks.html')

        else:
            context = {'form': form}
            return render(request, 'contacts.html', context)

    form = ContactForm()

    return render(request, 'contacts.html', {'form': form})



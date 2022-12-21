from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView
# Create your views here.


class Homepage(TemplateView):
    template_name = 'homepage.html'


# def homepage(request):
#     return render(request, "homepage.html")

class Homefilmes(ListView):
    template_name = 'homefilmes.html'
    model = Filme

# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, "homefilmes.html",context)


class Detalhesfilme(DetailView):
    template_name = 'detalhesfilme.html'
    model = Filme

    def get(self, request, *args, **kwargs):
        #Descobrir qual o filme ele ta acessando -
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        return super().get(request, *args, **kwargs) # Redireciona o usuario para a url final

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)
        context['filmes_relacionados'] = filmes_relacionados
        return context

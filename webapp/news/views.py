from django.shortcuts import render
from .models import Artiles
from .forms import ArtilesForm

from django.views.generic import DetailView, UpdateView, DeleteView



def news_home(request):
    news = Artiles.objects.all()
    return render(request, 'news/news_home.html',{'news': news})

class NewDetailView(DetailView):
    model = Artiles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewUpdateView(UpdateView):
    model = Artiles
    template_name = 'news/create.html'

    form_class = ArtilesForm


class NewDeleteView(DeleteView):
    model = Artiles
    success_url = '/news/'
    template_name = 'news/delete.html'



def create(request):
    error = ''
    if request.method == 'POST':
        form = ArtilesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма не верная!'
    form = ArtilesForm()

    data = {
        'form': form,
        'error': error
    }


    return render(request, 'news/create.html', data)

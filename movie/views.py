from django.views import generic 
from django.views.generic.edit import CreateView, ModelFormMixin

from hitcount.views import HitCountDetailView

from movie.forms import AddMovieForm

from .models import Movie


class IndexView(generic.ListView):
    template_name = 'pages/index.html'
    queryset = Movie.objects.published()
    paginate_by = 9


class TagIndexView(generic.ListView):
    template_name = 'pages/index.html'
    model = Movie
    paginate_by = 9

    def get_queryset(self):
        return Movie.objects.filter(tags__slug=self.kwargs.get('slug'))


class MovieDetailView(HitCountDetailView):
    template_name = 'pages/single-Movie.html'
    model = Movie
    count_hit = True


class GeneratePDFView(generic.DetailView):
    model = Movie
    template_name = 'pages/pdf.html'


class AboutMeView(generic.TemplateView):
    template_name = 'pages/author.html'
    
    
class AddMovieView(CreateView):
    template_name = 'pages/add-movie.html'
    model = Movie
    form_class = AddMovieForm
    success_url = '/index/'
    fields = [
        'title',
        'description',
        'trailer',
        'genres',
        'role',
    ]

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     form.send_email()
    #     return super().form_valid(form)
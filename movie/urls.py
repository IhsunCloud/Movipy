from django.urls import path

from .views import (
    IndexView,
    IndexView,
    TagIndexView,
    TagIndexView,
    MovieDetailView,
    AddMovieView,
    GeneratePDFView,
    AboutMeView
)


app_name = 'movie'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('page/<int:page>/', IndexView.as_view(), name='index'),
    path('hashtag/<slug:slug>/', TagIndexView.as_view(), name='hashtag'),
	path('hashtag/<slug:slug>/page/<int:page>/', TagIndexView.as_view(), name="hashtag"),
    
    path('movie/<slug:slug>/', MovieDetailView.as_view(), name='detail'),
    path('add-movie/', AddMovieView.as_view(), name='add-movie'),
    path('generate/pdf/<slug:slug>/', GeneratePDFView.as_view(), name='generate_pdf'),

    path('about-me/', AboutMeView.as_view(), name='about-me'),
]
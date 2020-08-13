from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import PostMainPage,PhotoModel,VideoModel,ONasModel,MusicModel

# Create your views here.
class PostMainPageView(ListView):
    model = PostMainPage
    template_name = 'home.html'

class PhotoModelView(ListView):
    model = PhotoModel
    template_name = 'gallery.html'

class VideoModelView(ListView):
    model = VideoModel
    template_name = 'video.html'

class ONasModelView(ListView):
    model = ONasModel
    template_name = 'onas.html'

class MusicModelView(ListView):
    model = MusicModel
    template_name = 'music.html'
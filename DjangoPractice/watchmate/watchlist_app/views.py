from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse

# Create your views here.

def movielist(request):
    movies=Movie.objects.all()
    data={
        'movies':list(movies.values())
    }
    return JsonResponse(data)

def movie_detail(request,pk):
    movies=Movie.objects.get(pk=pk)
    data={
        'name':movies.name,
        'desc':movies.description,
        'act_flg':movies.active
    }
    return JsonResponse(data)

